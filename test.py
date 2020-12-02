from lexer import *

def main():
    test = "+ - 123 9.8654 * /"
    lexer = Lexer(test)
    token = lexer.getToken()

    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()

main()
