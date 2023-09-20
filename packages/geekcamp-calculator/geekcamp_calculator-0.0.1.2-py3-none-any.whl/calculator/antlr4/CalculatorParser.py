# Generated from calculator/grammar/CalculatorParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,93,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,0,4,0,37,8,0,11,0,12,0,38,1,0,
        1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,54,8,2,1,2,1,
        2,5,2,58,8,2,10,2,12,2,61,9,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,
        7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,
        14,1,14,1,14,1,15,4,15,89,8,15,11,15,12,15,90,1,15,0,1,4,16,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,0,82,0,36,1,0,0,0,2,42,
        1,0,0,0,4,45,1,0,0,0,6,62,1,0,0,0,8,64,1,0,0,0,10,66,1,0,0,0,12,
        68,1,0,0,0,14,70,1,0,0,0,16,72,1,0,0,0,18,74,1,0,0,0,20,76,1,0,0,
        0,22,78,1,0,0,0,24,80,1,0,0,0,26,82,1,0,0,0,28,84,1,0,0,0,30,88,
        1,0,0,0,32,33,3,4,2,0,33,34,3,2,1,0,34,35,3,14,7,0,35,37,1,0,0,0,
        36,32,1,0,0,0,37,38,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,40,1,
        0,0,0,40,41,5,0,0,1,41,1,1,0,0,0,42,43,3,28,14,0,43,44,3,4,2,0,44,
        3,1,0,0,0,45,46,6,2,-1,0,46,47,3,30,15,0,47,59,1,0,0,0,48,53,10,
        2,0,0,49,54,3,6,3,0,50,54,3,8,4,0,51,54,3,10,5,0,52,54,3,12,6,0,
        53,49,1,0,0,0,53,50,1,0,0,0,53,51,1,0,0,0,53,52,1,0,0,0,54,55,1,
        0,0,0,55,56,3,4,2,3,56,58,1,0,0,0,57,48,1,0,0,0,58,61,1,0,0,0,59,
        57,1,0,0,0,59,60,1,0,0,0,60,5,1,0,0,0,61,59,1,0,0,0,62,63,5,6,0,
        0,63,7,1,0,0,0,64,65,5,7,0,0,65,9,1,0,0,0,66,67,5,8,0,0,67,11,1,
        0,0,0,68,69,5,9,0,0,69,13,1,0,0,0,70,71,5,10,0,0,71,15,1,0,0,0,72,
        73,5,11,0,0,73,17,1,0,0,0,74,75,5,1,0,0,75,19,1,0,0,0,76,77,5,5,
        0,0,77,21,1,0,0,0,78,79,5,3,0,0,79,23,1,0,0,0,80,81,5,12,0,0,81,
        25,1,0,0,0,82,83,5,13,0,0,83,27,1,0,0,0,84,85,3,16,8,0,85,86,3,16,
        8,0,86,29,1,0,0,0,87,89,3,18,9,0,88,87,1,0,0,0,89,90,1,0,0,0,90,
        88,1,0,0,0,90,91,1,0,0,0,91,31,1,0,0,0,4,38,53,59,90
    ]

class CalculatorParser ( Parser ):

    grammarFileName = "CalculatorParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "' '", "<INVALID>", "'.'", 
                     "'\\n'", "'*'", "'+'", "'-'", "'/'", "';'", "'='", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "DIGIT", "SPACE", "UPPER_ALPHABET", "DOT", 
                      "LINE_FEED", "ASTERISK", "PLUS", "HYPHEN", "SLASH", 
                      "SEMICOLON", "EQUALS", "OPEN_PARENTHESIS", "CLOSE_PARENTHESIS" ]

    RULE_prog = 0
    RULE_expr2 = 1
    RULE_expr1 = 2
    RULE_asterisk = 3
    RULE_plus = 4
    RULE_hyphen = 5
    RULE_slash = 6
    RULE_semicolon = 7
    RULE_equals = 8
    RULE_digit = 9
    RULE_lineFeed = 10
    RULE_upperAlphabet = 11
    RULE_openParenthesis = 12
    RULE_closeParenthesis = 13
    RULE_twoEquals = 14
    RULE_digits = 15

    ruleNames =  [ "prog", "expr2", "expr1", "asterisk", "plus", "hyphen", 
                   "slash", "semicolon", "equals", "digit", "lineFeed", 
                   "upperAlphabet", "openParenthesis", "closeParenthesis", 
                   "twoEquals", "digits" ]

    EOF = Token.EOF
    DIGIT=1
    SPACE=2
    UPPER_ALPHABET=3
    DOT=4
    LINE_FEED=5
    ASTERISK=6
    PLUS=7
    HYPHEN=8
    SLASH=9
    SEMICOLON=10
    EQUALS=11
    OPEN_PARENTHESIS=12
    CLOSE_PARENTHESIS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CalculatorParser.EOF, 0)

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.Expr1Context)
            else:
                return self.getTypedRuleContext(CalculatorParser.Expr1Context,i)


        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.Expr2Context)
            else:
                return self.getTypedRuleContext(CalculatorParser.Expr2Context,i)


        def semicolon(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.SemicolonContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.SemicolonContext,i)


        def getRuleIndex(self):
            return CalculatorParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CalculatorParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.expr1(0)
                self.state = 33
                self.expr2()
                self.state = 34
                self.semicolon()
                self.state = 38 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 40
            self.match(CalculatorParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def twoEquals(self):
            return self.getTypedRuleContext(CalculatorParser.TwoEqualsContext,0)


        def expr1(self):
            return self.getTypedRuleContext(CalculatorParser.Expr1Context,0)


        def getRuleIndex(self):
            return CalculatorParser.RULE_expr2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr2" ):
                listener.enterExpr2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr2" ):
                listener.exitExpr2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)




    def expr2(self):

        localctx = CalculatorParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.twoEquals()
            self.state = 43
            self.expr1(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def digits(self):
            return self.getTypedRuleContext(CalculatorParser.DigitsContext,0)


        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.Expr1Context)
            else:
                return self.getTypedRuleContext(CalculatorParser.Expr1Context,i)


        def asterisk(self):
            return self.getTypedRuleContext(CalculatorParser.AsteriskContext,0)


        def plus(self):
            return self.getTypedRuleContext(CalculatorParser.PlusContext,0)


        def hyphen(self):
            return self.getTypedRuleContext(CalculatorParser.HyphenContext,0)


        def slash(self):
            return self.getTypedRuleContext(CalculatorParser.SlashContext,0)


        def getRuleIndex(self):
            return CalculatorParser.RULE_expr1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr1" ):
                listener.enterExpr1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr1" ):
                listener.exitExpr1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalculatorParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.digits()
            self._ctx.stop = self._input.LT(-1)
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CalculatorParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 48
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 53
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [6]:
                        self.state = 49
                        self.asterisk()
                        pass
                    elif token in [7]:
                        self.state = 50
                        self.plus()
                        pass
                    elif token in [8]:
                        self.state = 51
                        self.hyphen()
                        pass
                    elif token in [9]:
                        self.state = 52
                        self.slash()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 55
                    self.expr1(3) 
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AsteriskContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASTERISK(self):
            return self.getToken(CalculatorParser.ASTERISK, 0)

        def getRuleIndex(self):
            return CalculatorParser.RULE_asterisk

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsterisk" ):
                listener.enterAsterisk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsterisk" ):
                listener.exitAsterisk(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsterisk" ):
                return visitor.visitAsterisk(self)
            else:
                return visitor.visitChildren(self)




    def asterisk(self):

        localctx = CalculatorParser.AsteriskContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_asterisk)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(CalculatorParser.ASTERISK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(CalculatorParser.PLUS, 0)

        def getRuleIndex(self):
            return CalculatorParser.RULE_plus

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlus" ):
                listener.enterPlus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlus" ):
                listener.exitPlus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlus" ):
                return visitor.visitPlus(self)
            else:
                return visitor.visitChildren(self)




    def plus(self):

        localctx = CalculatorParser.PlusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_plus)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(CalculatorParser.PLUS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HyphenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HYPHEN(self):
            return self.getToken(CalculatorParser.HYPHEN, 0)

        def getRuleIndex(self):
            return CalculatorParser.RULE_hyphen

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHyphen" ):
                listener.enterHyphen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHyphen" ):
                listener.exitHyphen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHyphen" ):
                return visitor.visitHyphen(self)
            else:
                return visitor.visitChildren(self)




    def hyphen(self):

        localctx = CalculatorParser.HyphenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_hyphen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(CalculatorParser.HYPHEN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SlashContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(CalculatorParser.SLASH, 0)

        def getRuleIndex(self):
            return CalculatorParser.RULE_slash

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSlash" ):
                listener.enterSlash(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSlash" ):
                listener.exitSlash(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSlash" ):
                return visitor.visitSlash(self)
            else:
                return visitor.visitChildren(self)




    def slash(self):

        localctx = CalculatorParser.SlashContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_slash)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(CalculatorParser.SLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SemicolonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(CalculatorParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CalculatorParser.RULE_semicolon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSemicolon" ):
                listener.enterSemicolon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSemicolon" ):
                listener.exitSemicolon(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSemicolon" ):
                return visitor.visitSemicolon(self)
            else:
                return visitor.visitChildren(self)




    def semicolon(self):

        localctx = CalculatorParser.SemicolonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_semicolon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(CalculatorParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(CalculatorParser.EQUALS, 0)

        def getRuleIndex(self):
            return CalculatorParser.RULE_equals

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquals" ):
                listener.enterEquals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquals" ):
                listener.exitEquals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquals" ):
                return visitor.visitEquals(self)
            else:
                return visitor.visitChildren(self)




    def equals(self):

        localctx = CalculatorParser.EqualsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_equals)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(CalculatorParser.EQUALS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DigitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(CalculatorParser.DIGIT, 0)

        def getRuleIndex(self):
            return CalculatorParser.RULE_digit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDigit" ):
                listener.enterDigit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDigit" ):
                listener.exitDigit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDigit" ):
                return visitor.visitDigit(self)
            else:
                return visitor.visitChildren(self)




    def digit(self):

        localctx = CalculatorParser.DigitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_digit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(CalculatorParser.DIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineFeedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINE_FEED(self):
            return self.getToken(CalculatorParser.LINE_FEED, 0)

        def getRuleIndex(self):
            return CalculatorParser.RULE_lineFeed

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLineFeed" ):
                listener.enterLineFeed(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLineFeed" ):
                listener.exitLineFeed(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLineFeed" ):
                return visitor.visitLineFeed(self)
            else:
                return visitor.visitChildren(self)




    def lineFeed(self):

        localctx = CalculatorParser.LineFeedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_lineFeed)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(CalculatorParser.LINE_FEED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpperAlphabetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPPER_ALPHABET(self):
            return self.getToken(CalculatorParser.UPPER_ALPHABET, 0)

        def getRuleIndex(self):
            return CalculatorParser.RULE_upperAlphabet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpperAlphabet" ):
                listener.enterUpperAlphabet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpperAlphabet" ):
                listener.exitUpperAlphabet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpperAlphabet" ):
                return visitor.visitUpperAlphabet(self)
            else:
                return visitor.visitChildren(self)




    def upperAlphabet(self):

        localctx = CalculatorParser.UpperAlphabetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_upperAlphabet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(CalculatorParser.UPPER_ALPHABET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpenParenthesisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARENTHESIS(self):
            return self.getToken(CalculatorParser.OPEN_PARENTHESIS, 0)

        def getRuleIndex(self):
            return CalculatorParser.RULE_openParenthesis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpenParenthesis" ):
                listener.enterOpenParenthesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpenParenthesis" ):
                listener.exitOpenParenthesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpenParenthesis" ):
                return visitor.visitOpenParenthesis(self)
            else:
                return visitor.visitChildren(self)




    def openParenthesis(self):

        localctx = CalculatorParser.OpenParenthesisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_openParenthesis)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(CalculatorParser.OPEN_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CloseParenthesisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLOSE_PARENTHESIS(self):
            return self.getToken(CalculatorParser.CLOSE_PARENTHESIS, 0)

        def getRuleIndex(self):
            return CalculatorParser.RULE_closeParenthesis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCloseParenthesis" ):
                listener.enterCloseParenthesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCloseParenthesis" ):
                listener.exitCloseParenthesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCloseParenthesis" ):
                return visitor.visitCloseParenthesis(self)
            else:
                return visitor.visitChildren(self)




    def closeParenthesis(self):

        localctx = CalculatorParser.CloseParenthesisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_closeParenthesis)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(CalculatorParser.CLOSE_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TwoEqualsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equals(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.EqualsContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.EqualsContext,i)


        def getRuleIndex(self):
            return CalculatorParser.RULE_twoEquals

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTwoEquals" ):
                listener.enterTwoEquals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTwoEquals" ):
                listener.exitTwoEquals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTwoEquals" ):
                return visitor.visitTwoEquals(self)
            else:
                return visitor.visitChildren(self)




    def twoEquals(self):

        localctx = CalculatorParser.TwoEqualsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_twoEquals)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.equals()
            self.state = 85
            self.equals()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DigitsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def digit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.DigitContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.DigitContext,i)


        def getRuleIndex(self):
            return CalculatorParser.RULE_digits

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDigits" ):
                listener.enterDigits(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDigits" ):
                listener.exitDigits(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDigits" ):
                return visitor.visitDigits(self)
            else:
                return visitor.visitChildren(self)




    def digits(self):

        localctx = CalculatorParser.DigitsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_digits)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 87
                    self.digit()

                else:
                    raise NoViableAltException(self)
                self.state = 90 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr1_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




