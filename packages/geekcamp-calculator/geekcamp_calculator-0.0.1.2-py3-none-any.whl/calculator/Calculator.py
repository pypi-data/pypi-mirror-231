from antlr4 import InputStream, CommonTokenStream
from happy_python import HappyPyException

from calculator.antlr4.CalculatorParser import CalculatorParser
from calculator.common import hlog
from calculator.parser.CalculatorBailLexer import CalculatorBailLexer
from calculator.parser.CustomErrorListener import CustomErrorListener


class Calculator:
    @staticmethod
    def parser(stat: str) -> CalculatorParser | None:
        hlog.info('语法识别：\n\n\t%s\n\n' % stat)

        input_stream = InputStream(stat)
        lexer = CalculatorBailLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(CustomErrorListener())

        stream = CommonTokenStream(lexer)
        parser = CalculatorParser(stream)

        # 自定义错误处理，默认错误信息打印到控制台。自定义后，由hlog处理
        parser.removeErrorListeners()
        parser.addErrorListener(CustomErrorListener())

        try:
            tree = parser.prog()
            hlog.debug('Calculator.Antlr4->语法分析成功')
        except HappyPyException as e:
            hlog.error('Calculator.Antlr4->语法分析因错误而终止：%s' % e)
            return None

        return tree
