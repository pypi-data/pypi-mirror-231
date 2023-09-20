from antlr4.error.ErrorListener import ErrorListener
from happy_python import HappyPyException


class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        msg = 'Calculator.Antlr4.SyntaxError->第%s行%s列: %s' % (line, column, msg)
        raise HappyPyException(msg)
