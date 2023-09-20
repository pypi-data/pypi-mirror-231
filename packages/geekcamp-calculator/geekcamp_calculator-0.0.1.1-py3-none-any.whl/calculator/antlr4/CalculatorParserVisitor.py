# Generated from calculator/grammar/CalculatorParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete generic visitor for a parse tree produced by CalculatorParser.

class CalculatorParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculatorParser#prog.
    def visitProg(self, ctx:CalculatorParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#expr2.
    def visitExpr2(self, ctx:CalculatorParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#expr1.
    def visitExpr1(self, ctx:CalculatorParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#asterisk.
    def visitAsterisk(self, ctx:CalculatorParser.AsteriskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#plus.
    def visitPlus(self, ctx:CalculatorParser.PlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#hyphen.
    def visitHyphen(self, ctx:CalculatorParser.HyphenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#slash.
    def visitSlash(self, ctx:CalculatorParser.SlashContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#semicolon.
    def visitSemicolon(self, ctx:CalculatorParser.SemicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#equals.
    def visitEquals(self, ctx:CalculatorParser.EqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#digit.
    def visitDigit(self, ctx:CalculatorParser.DigitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#lineFeed.
    def visitLineFeed(self, ctx:CalculatorParser.LineFeedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#upperAlphabet.
    def visitUpperAlphabet(self, ctx:CalculatorParser.UpperAlphabetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#openParenthesis.
    def visitOpenParenthesis(self, ctx:CalculatorParser.OpenParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#closeParenthesis.
    def visitCloseParenthesis(self, ctx:CalculatorParser.CloseParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#twoEquals.
    def visitTwoEquals(self, ctx:CalculatorParser.TwoEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#digits.
    def visitDigits(self, ctx:CalculatorParser.DigitsContext):
        return self.visitChildren(ctx)



del CalculatorParser