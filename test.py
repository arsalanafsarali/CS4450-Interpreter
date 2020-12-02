from lexer import *

def main():
    test = "Interpreter + * x ProJect"
    lexer = Lexer(test)

    while lexer.lookNext() != '\0':
        print(lexer.curChar)
        lexer.nextChar()

main()
