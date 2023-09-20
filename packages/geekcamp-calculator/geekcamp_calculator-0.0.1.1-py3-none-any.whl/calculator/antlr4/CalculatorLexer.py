# Generated from calculator/grammar/CalculatorLexer.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,13,53,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,
        1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,
        1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,0,0,13,1,1,3,2,5,3,7,4,
        9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,1,0,2,1,0,48,57,
        1,0,65,90,52,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,
        1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,
        1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,1,27,1,0,0,0,3,29,
        1,0,0,0,5,31,1,0,0,0,7,33,1,0,0,0,9,35,1,0,0,0,11,37,1,0,0,0,13,
        39,1,0,0,0,15,41,1,0,0,0,17,43,1,0,0,0,19,45,1,0,0,0,21,47,1,0,0,
        0,23,49,1,0,0,0,25,51,1,0,0,0,27,28,7,0,0,0,28,2,1,0,0,0,29,30,5,
        32,0,0,30,4,1,0,0,0,31,32,7,1,0,0,32,6,1,0,0,0,33,34,5,46,0,0,34,
        8,1,0,0,0,35,36,5,10,0,0,36,10,1,0,0,0,37,38,5,42,0,0,38,12,1,0,
        0,0,39,40,5,43,0,0,40,14,1,0,0,0,41,42,5,45,0,0,42,16,1,0,0,0,43,
        44,5,47,0,0,44,18,1,0,0,0,45,46,5,59,0,0,46,20,1,0,0,0,47,48,5,61,
        0,0,48,22,1,0,0,0,49,50,5,40,0,0,50,24,1,0,0,0,51,52,5,41,0,0,52,
        26,1,0,0,0,1,0,0
    ]

class CalculatorLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DIGIT = 1
    SPACE = 2
    UPPER_ALPHABET = 3
    DOT = 4
    LINE_FEED = 5
    ASTERISK = 6
    PLUS = 7
    HYPHEN = 8
    SLASH = 9
    SEMICOLON = 10
    EQUALS = 11
    OPEN_PARENTHESIS = 12
    CLOSE_PARENTHESIS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "' '", "'.'", "'\\n'", "'*'", "'+'", "'-'", "'/'", "';'", "'='", 
            "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "DIGIT", "SPACE", "UPPER_ALPHABET", "DOT", "LINE_FEED", "ASTERISK", 
            "PLUS", "HYPHEN", "SLASH", "SEMICOLON", "EQUALS", "OPEN_PARENTHESIS", 
            "CLOSE_PARENTHESIS" ]

    ruleNames = [ "DIGIT", "SPACE", "UPPER_ALPHABET", "DOT", "LINE_FEED", 
                  "ASTERISK", "PLUS", "HYPHEN", "SLASH", "SEMICOLON", "EQUALS", 
                  "OPEN_PARENTHESIS", "CLOSE_PARENTHESIS" ]

    grammarFileName = "CalculatorLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


