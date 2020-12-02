import enum

class Lexer:
    def __init__(self, input):
        self.source = input + '\n'
        self.curChar = ''
        self.curPos = -1
        self.nextChar()

    def getToken(self):
        token = None

        if self.curChar == '+':
            token = Token(self.curChar, TokenType.PLUS)
        if self.curChar == '-':
            token = Token(self.curChar, TokenType.MINUS)
        if self.curChar == '*':
            token = Token(self.curChar, TokenType.ASTERISK)
        if self.curChar == '/':
            token = Token(self.curChar, TokenType.SLASH)
        if self.curChar == '\n':
            token = Token(self.curChar, TokenType.NEWLINE)
        if self.curChar == '\0':
            token = Token(self.curChar, TokenType.EOF)
        else:
            pass

        self.nextChar()
        return token

    def nextChar(self):
        self.curPos += 1

        if self.curPos >= len(self.source):
            self.curChar = '\0'
        else:
            self.curChar = self.source[self.curPos]

    def lookNext(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'
        else:
            return self.source[self.curPos + 1]

    def abort(self):
        pass

    def ignoreWhiteSpace(self):
        pass

    def ignoreComments(self):
        pass

# Token contains the original text and the type of token.
class Token:   
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText   # The token's actual text. Used for identifiers, strings, and numbers.
        self.kind = tokenKind   # The TokenType that this token is classified as.

# TokenType is our enum for all the types of tokens.
class TokenType(enum.Enum):
	EOF = -1
	NEWLINE = 0
	NUMBER = 1
	IDENT = 2
	STRING = 3
	# Keywords.
	LABEL = 101
	GOTO = 102
	PRINT = 103
	INPUT = 104
	LET = 105
	IF = 106
	THEN = 107
	ENDIF = 108
	WHILE = 109
	REPEAT = 110
	ENDWHILE = 111
	# Operators.
	EQ = 201  
	PLUS = 202
	MINUS = 203
	ASTERISK = 204
	SLASH = 205
	EQEQ = 206
	NOTEQ = 207
	LT = 208
	LTEQ = 209
	GT = 210
	GTEQ = 211