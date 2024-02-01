from lex import *
from parse import *
from emit import *
import sys 
def main():
    print("my own compiler ")
    if len(sys.argv) != 2:
        sys.exit ("Error : compiler needs source file as an argument ")
    with open(sys.argv[1],'r') as inputFile:
        source = inputFile.read()
    
    lexer = Lexer(source)
    emitter = Emitter("out.c")
    parser= Parser(lexer,emitter)
    parser.program()
    emitter.writeFile()
    print("compiling completed")
main()