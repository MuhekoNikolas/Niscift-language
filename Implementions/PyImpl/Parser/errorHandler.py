

from antlr4.error.ErrorListener import ErrorListener
from colorama import Fore, Back, Style, init

init(autoreset=True)

class MyVisitorErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Syntax error at line {line}, column {column}: {msg}", offendingSymbol)
        exit()

class MyErrorManager():
    def __init__(self):
        pass 

    def constructErrorInvokationHeader(self, line, column, errorType, errorMessage):
        return f"""{f'{Fore.RED}{Style.BRIGHT}Line:{Fore.WHITE}{line}{Fore.RED} Col:{Fore.WHITE}{column}{Fore.RED}'} {Fore.YELLOW}{
            errorType
        }{Fore.RED}: {
            errorMessage
        }"""

    def invokeError(self, errorType=None, errorMessage=None, errorCtx=None):
        token = errorCtx.start
        tokenInputStream = token.getInputStream()

        thisCulpritText = tokenInputStream.getText(errorCtx.start.start, errorCtx.stop.stop)
        thisCuplritTextLength = len(thisCulpritText)

        tokenInputStreamMoreChars = tokenInputStream.getText(token.start+thisCuplritTextLength, token.stop+5)

        thisCtxFullLineText = tokenInputStream.getText(token.start-25, token.start-1) # - thisCuplritTextLength)
        thisErrorInvocationHeader = self.constructErrorInvokationHeader(line=errorCtx.start.line, column=errorCtx.start.column, errorType=errorType, errorMessage=errorMessage)

        print(f"\n{thisErrorInvocationHeader}\n\n{Fore.RESET}{Style.RESET_ALL}{thisCtxFullLineText}{Fore.RED}{thisCulpritText}{Fore.RESET}{tokenInputStreamMoreChars}")

        exit()