import os
import re

from typing import Tuple,Dict
from enum import auto, IntEnum
from textwrap import dedent
from dataclasses import dataclass

from .config_plugin import PLUGIN_MARK


OPEN, CLOSE = '{', '}'

SNIPPETS_TARGET = '"markdown"'



class RefKind(IntEnum):
    Link = auto()
    File = auto()
    Img  = auto()
    Ext  = auto()
    Include = auto()





@dataclass
class AutoCompletion:
    """
    An AutoCompletion instance holds the whole logic to build individual code snippets as
    strings, for a given kind of data.
    """

    kind: RefKind               # Snippet type
    head: str                   # Prefix identifier (used to spot them in the html code)

    snippet_start: str = ''     # Element coming before the "[...]" initial part
    tail_wrap: Tuple[str,str] = '(',')'     # open+close for the last section (after "[...]")
    with_short: bool = True     # Also generate the short snippet version (head+identifier only)
    attrs: str = ""             # string of attributes to always add at the end of the body


    @staticmethod
    def setup_class():
        AutoCompletion.__LINK_BUILDER: Dict[RefKind,AutoCompletion] = {
            formatter.kind: formatter for formatter in [
                VscAutoAddress( RefKind.Link,    '--'),                     # internal links
                VscAutoAddress( RefKind.File,    '++'),                     # any internal file
                VscAutoAddress( RefKind.Img,     '!!', snippet_start='!'),  # images
                VscAutoAddress( RefKind.Ext,      '', tail_wrap=('[',']'), attrs="target=_blank"),  # External links
                VscAutoInclude( RefKind.Include, '::')
        ]}
        AutoCompletion.__POTENTIAL_REF_PATTERN = re.compile(
            '|'.join( re.escape(o.head) for o in AutoCompletion.__LINK_BUILDER.values() if o.head)
        )

    @classmethod
    def href_is_possible_ref(cls, href):
        return cls.__POTENTIAL_REF_PATTERN.match(href)

    @classmethod
    def get_completer_for(cls, kind:RefKind) -> 'AutoCompletion':
        return cls.__LINK_BUILDER[kind]



    def get_final_identifier(self, identifier:str, with_head=True):
        """ Add the "head_link" part to the identifier if needed, and format the identifier
            to avoid they generate warnings during the builds
        """
        return with_head * self.head + identifier


    def build_snippet(self, identifier, src_link, **_):
        """ Generate code snippet entries for the given (bare) identifier, pointing toward the
            given source (which will, in the end, be the targeted element).
            @identifier: the bare identifier, without the "head" part ("!!", "--", ...)
            @src_link is the path of the source, relative to the cwd ("development wise")
            Automatically add the "shorthand" version of the snippet, if the kind requires it.
        """
        raise NotImplementedError("Subclasses must override this method")





#--------------------------------------------------------------------------------





@dataclass
class VscAutoAddress(AutoCompletion):
    """ Build snippets for links, ids, extras, files, images """


    def get_final_identifier(self, identifier:str, with_head=True):

        assets = 'assets/'
        if identifier.startswith(assets):
            identifier = identifier[len(assets):]
        return with_head * self.head + identifier.replace('.','_')


    def build_snippet(self, identifier, src_link, **_):

        clean_id = self.get_final_identifier(identifier, False)
        prefix   = f"{ self.kind.name }.{ clean_id }"       # Img.identifier or so...
        body     = self.__build_body(clean_id)
        yield self._build_snippet(prefix, body, src_link, "Md")

        if self.with_short:
            prefix = self.head + clean_id                   # !!identifier or so...
            body   = f"${ OPEN }0:{ self.head }{ CLOSE }{ clean_id }"
            yield self._build_snippet(prefix, body, src_link, "Reference")


    def __build_body(self, clean_id:str):
        """ helper... """
        L,R     = self.tail_wrap
        content = self._get_content(clean_id)
        body    = self.snippet_start + "[${0:" + content + "}]" + f"{ L }{ self.head }{ clean_id }{ R }"
        if self.attrs:
            body += "{: " + self.attrs + " }"
        return body


    def _get_content(self, clean_id:str):
        if self.kind == RefKind.Ext:
            return clean_id
        return 'content'


    def _build_snippet(self, prefix:str, body:str, src_link:str, name_prefix=''):
        if name_prefix:
            name_prefix += " - "
        json_id = f"{ name_prefix }{ self.kind.name }: { src_link !r}"
        return json_id, dedent(f"""\
            "{ json_id }": { OPEN }
                "prefix": "{ prefix }",
                "scope": { SNIPPETS_TARGET },
                "body": ["{ body }"],
                "description": "{ PLUGIN_MARK }"
            { CLOSE }""")






@dataclass
class VscAutoInclude(VscAutoAddress):
    """ Build snippets for markdown code inclusions (ie: "--8<--" ) """


    # pylint: disable-next=arguments-differ
    def build_snippet(self, identifier:str, src_link:str, *, root_inclusion:str): #, inclusions_with_root:bool):
        # root_inclusion: one of the path s given in plugin.inclusions (as uri)

        #i_truncate = len(root_inclusion)+(not inclusions_with_root)   # Extra slash to account for
        i_truncate = len(root_inclusion) + 1   # extra slash to account for
        _, ext     = os.path.splitext(identifier)
        short_uri  = identifier[i_truncate:]
        body       = f'--8<-- \\"{ identifier }\\"'
        prefix     = f"{ self.head }{ ext.strip('.') } { short_uri }"
        snippet    = self._build_snippet(prefix, body, identifier)
        yield snippet




AutoCompletion.setup_class()         # Trigger global definitions in the top level class
