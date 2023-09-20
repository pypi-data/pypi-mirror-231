from calculator.Calculator import Calculator

def main():
    calculator = Calculator()
    stat = input('请输入表达式： ')

    if calculator.parser(stat) is None:
        exit(1)

    exit(0)

if __name__ == "__main__":
    main()
