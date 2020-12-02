import enum

class Lexer:
    def __init__(self, input):
        self.source = input + '\n'
        self.curChar = ''
        self.curPos = -1
        self.nextChar()

    def getToken(self):
        if self.curChar == '+':
            pass
        if self.curChar == '-':
            pass
        if self.curChar == '*':
            pass
        if self.curChar == '/':
            pass
        if self.curChar == '\n':
            pass
        if self.curChar == '\0':
            pass
        else:
            pass

        self.nextChar()

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
