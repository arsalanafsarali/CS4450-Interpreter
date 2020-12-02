from lexer import *

def main():
    test = "+- */"
    lexer = Lexer(test)
    token = lexer.getToken()

    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()

main()
