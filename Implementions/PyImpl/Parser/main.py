from antlr4 import InputStream, CommonTokenStream
from libs.pscriptLexer import pscriptLexer
from libs.pscriptParser import pscriptParser

from visitor import MyVisitor
from errorHandler import MyVisitorErrorListener, MyErrorManager

from json import dumps
from zlib import compress
import argparse
import asyncio
from sys import argv

from pprint import pprint

parser = argparse.ArgumentParser(
    prog='pscriptParser',
    description='Processes a .pscript file transforming it into an executable instruction set',
)

parser.add_argument(
    'input', type=argparse.FileType(encoding='utf-8'),
    help='Input file to parse', nargs=1, metavar='I'
)

parser.add_argument(
    '--O', '-output', type=str, dest='output', default='?output.json',
    help='File to output results to', required=False
)

parser.add_argument(
    '--F', '-format', type=str, choices=('json',), dest='format',
    help='Format to save file as', required=False
)

parser.add_argument(
    '--C', '-compress', action='store_true', default=False, dest='compress',
    help='Compresses the parsed file to take up less space', required=False
)

if __name__ == '__main__':
    v = parser.parse_args(argv[1:])
    d = vars(v)

    if not (d['input'] or d['output']):
        parser.print_help()
        exit(0)
    
    if d['output'].startswith('?') and d['compress']:
        d['output'] = d['output'].split('.')[0][1:] + '.Zlib'
    elif d['output'].startswith('?'):
        d['output'] = d['output'][1:]

    if not d['input']:
        print('Error: No input file provided')
        exit(1)
    
    stream = InputStream(d['input'][0].read())
    #print(d['input'][0].read(), "fojfoifj", d['input'][0], argv[1:])
    lexer = pscriptLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = pscriptParser(token_stream)
    parser.addErrorListener(MyVisitorErrorListener())

    visitor = MyVisitor() 
    tree = parser.root()
    
    r = asyncio.run(visitor.visit(tree))

    if d['compress']:
        with open(d['output'], 'wb') as fp:
            compressed_data = dumps(r[0]).encode()
            fp.write(compress(compressed_data))
    else:
        with open(d['output'], 'w') as fp:
            visitedDataDict = r[0]
            fp.write(dumps(visitedDataDict, indent=4))

    visitedDataObj = r[1]

    #print(r, "ghghgh")
    thisRanObj = visitedDataObj.run(MyErrorManager())
    pprint(visitedDataObj.variableScope.variables, indent=4, width=8)

    print('Saved output to:', d['output'])