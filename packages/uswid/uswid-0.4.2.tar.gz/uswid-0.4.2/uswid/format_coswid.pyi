from .container import uSwidContainer as uSwidContainer
from .entity import uSwidEntity as uSwidEntity, uSwidEntityRole as uSwidEntityRole
from .enums import uSwidGlobalMap as uSwidGlobalMap
from .errors import NotSupportedError as NotSupportedError
from .format import uSwidFormatBase as uSwidFormatBase
from .identity import uSwidIdentity as uSwidIdentity
from .link import uSwidLink as uSwidLink, uSwidLinkRel as uSwidLinkRel

class uSwidFormatCoswid(uSwidFormatBase):
    def __init__(self) -> None: ...
    def load(self, blob: bytes) -> uSwidContainer: ...
    def save(self, container: uSwidContainer) -> bytes: ...
