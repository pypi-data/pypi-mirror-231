# Generated from calculator/grammar/CalculatorParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete listener for a parse tree produced by CalculatorParser.
class CalculatorParserListener(ParseTreeListener):

    # Enter a parse tree produced by CalculatorParser#prog.
    def enterProg(self, ctx:CalculatorParser.ProgContext):
        pass

    # Exit a parse tree produced by CalculatorParser#prog.
    def exitProg(self, ctx:CalculatorParser.ProgContext):
        pass


    # Enter a parse tree produced by CalculatorParser#expr2.
    def enterExpr2(self, ctx:CalculatorParser.Expr2Context):
        pass

    # Exit a parse tree produced by CalculatorParser#expr2.
    def exitExpr2(self, ctx:CalculatorParser.Expr2Context):
        pass


    # Enter a parse tree produced by CalculatorParser#expr1.
    def enterExpr1(self, ctx:CalculatorParser.Expr1Context):
        pass

    # Exit a parse tree produced by CalculatorParser#expr1.
    def exitExpr1(self, ctx:CalculatorParser.Expr1Context):
        pass


    # Enter a parse tree produced by CalculatorParser#asterisk.
    def enterAsterisk(self, ctx:CalculatorParser.AsteriskContext):
        pass

    # Exit a parse tree produced by CalculatorParser#asterisk.
    def exitAsterisk(self, ctx:CalculatorParser.AsteriskContext):
        pass


    # Enter a parse tree produced by CalculatorParser#plus.
    def enterPlus(self, ctx:CalculatorParser.PlusContext):
        pass

    # Exit a parse tree produced by CalculatorParser#plus.
    def exitPlus(self, ctx:CalculatorParser.PlusContext):
        pass


    # Enter a parse tree produced by CalculatorParser#hyphen.
    def enterHyphen(self, ctx:CalculatorParser.HyphenContext):
        pass

    # Exit a parse tree produced by CalculatorParser#hyphen.
    def exitHyphen(self, ctx:CalculatorParser.HyphenContext):
        pass


    # Enter a parse tree produced by CalculatorParser#slash.
    def enterSlash(self, ctx:CalculatorParser.SlashContext):
        pass

    # Exit a parse tree produced by CalculatorParser#slash.
    def exitSlash(self, ctx:CalculatorParser.SlashContext):
        pass


    # Enter a parse tree produced by CalculatorParser#semicolon.
    def enterSemicolon(self, ctx:CalculatorParser.SemicolonContext):
        pass

    # Exit a parse tree produced by CalculatorParser#semicolon.
    def exitSemicolon(self, ctx:CalculatorParser.SemicolonContext):
        pass


    # Enter a parse tree produced by CalculatorParser#equals.
    def enterEquals(self, ctx:CalculatorParser.EqualsContext):
        pass

    # Exit a parse tree produced by CalculatorParser#equals.
    def exitEquals(self, ctx:CalculatorParser.EqualsContext):
        pass


    # Enter a parse tree produced by CalculatorParser#digit.
    def enterDigit(self, ctx:CalculatorParser.DigitContext):
        pass

    # Exit a parse tree produced by CalculatorParser#digit.
    def exitDigit(self, ctx:CalculatorParser.DigitContext):
        pass


    # Enter a parse tree produced by CalculatorParser#lineFeed.
    def enterLineFeed(self, ctx:CalculatorParser.LineFeedContext):
        pass

    # Exit a parse tree produced by CalculatorParser#lineFeed.
    def exitLineFeed(self, ctx:CalculatorParser.LineFeedContext):
        pass


    # Enter a parse tree produced by CalculatorParser#upperAlphabet.
    def enterUpperAlphabet(self, ctx:CalculatorParser.UpperAlphabetContext):
        pass

    # Exit a parse tree produced by CalculatorParser#upperAlphabet.
    def exitUpperAlphabet(self, ctx:CalculatorParser.UpperAlphabetContext):
        pass


    # Enter a parse tree produced by CalculatorParser#openParenthesis.
    def enterOpenParenthesis(self, ctx:CalculatorParser.OpenParenthesisContext):
        pass

    # Exit a parse tree produced by CalculatorParser#openParenthesis.
    def exitOpenParenthesis(self, ctx:CalculatorParser.OpenParenthesisContext):
        pass


    # Enter a parse tree produced by CalculatorParser#closeParenthesis.
    def enterCloseParenthesis(self, ctx:CalculatorParser.CloseParenthesisContext):
        pass

    # Exit a parse tree produced by CalculatorParser#closeParenthesis.
    def exitCloseParenthesis(self, ctx:CalculatorParser.CloseParenthesisContext):
        pass


    # Enter a parse tree produced by CalculatorParser#twoEquals.
    def enterTwoEquals(self, ctx:CalculatorParser.TwoEqualsContext):
        pass

    # Exit a parse tree produced by CalculatorParser#twoEquals.
    def exitTwoEquals(self, ctx:CalculatorParser.TwoEqualsContext):
        pass


    # Enter a parse tree produced by CalculatorParser#digits.
    def enterDigits(self, ctx:CalculatorParser.DigitsContext):
        pass

    # Exit a parse tree produced by CalculatorParser#digits.
    def exitDigits(self, ctx:CalculatorParser.DigitsContext):
        pass



del CalculatorParser