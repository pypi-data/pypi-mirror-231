from .container import uSwidContainer as uSwidContainer
from .enums import USWID_HEADER_FLAG_COMPRESSED as USWID_HEADER_FLAG_COMPRESSED, USWID_HEADER_MAGIC as USWID_HEADER_MAGIC
from .errors import NotSupportedError as NotSupportedError
from .format import uSwidFormatBase as uSwidFormatBase
from .format_coswid import uSwidFormatCoswid as uSwidFormatCoswid
from .identity import uSwidIdentity as uSwidIdentity
from _typeshed import Incomplete

class uSwidFormatUswid(uSwidFormatBase):
    compress: Incomplete
    def __init__(self, compress: bool = ...) -> None: ...
    def load(self, blob: bytes) -> uSwidContainer: ...
    def save(self, container: uSwidContainer) -> bytes: ...
