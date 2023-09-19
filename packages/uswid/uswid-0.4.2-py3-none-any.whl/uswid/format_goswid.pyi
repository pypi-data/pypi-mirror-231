from .container import uSwidContainer as uSwidContainer
from .entity import uSwidEntity as uSwidEntity
from .errors import NotSupportedError as NotSupportedError
from .format import uSwidFormatBase as uSwidFormatBase
from .identity import uSwidIdentity as uSwidIdentity
from .link import uSwidLink as uSwidLink

class uSwidFormatGoswid(uSwidFormatBase):
    def __init__(self) -> None: ...
    def load(self, blob: bytes) -> uSwidContainer: ...
    def save(self, container: uSwidContainer) -> bytes: ...
