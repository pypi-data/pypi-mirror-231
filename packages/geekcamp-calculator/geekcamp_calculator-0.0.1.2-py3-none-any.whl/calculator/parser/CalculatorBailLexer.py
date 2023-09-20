from antlr4 import RecognitionException
from happy_python import HappyPyException

from calculator.antlr4.CalculatorLexer import CalculatorLexer


class CalculatorBailLexer(CalculatorLexer):
    def recover(self, re: RecognitionException):
        raise HappyPyException('Calculator.Antlr4.recover')
