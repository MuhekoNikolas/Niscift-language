import sys
from enum import Enum
from typing import TextIO
from antlr4 import Parser, TokenStream

class pscriptVersion(Enum):
    Autodetect = 0
    pscript2 = 2
    pscript3 = 3

class pscriptParserBase(Parser):
    def __init__(self, input_stream: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input_stream, output)
        self.__version = pscriptVersion.Autodetect

    @property
    def version(self) -> pscriptVersion:
        return self.__version

    @version.setter
    def version(self, version: pscriptVersion | int):
        if isinstance(version, pscriptVersion):
            self.__version = version
        else:
            self.__version = pscriptVersion(version)

    def CheckVersion(self, version: int) -> bool:
        return self.__version == pscriptVersion.Autodetect or version == self.__version.value

    def SetVersion(self, required_version: int) -> None:
        self.__version = pscriptVersion(required_version)