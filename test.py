from lexer import *

def main():
    test = "+ - #This is a comment! \n */"
    lexer = Lexer(test)
    token = lexer.getToken()

    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()

main()
