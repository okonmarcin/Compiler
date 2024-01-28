from app.compiler import parser


if __name__ == "__main__":
    exp_parser = parser.Parser("9+2")
    exp_parser.parse()
    print(exp_parser.get_output())

    exp_parser = parser.Parser("5-0")
    exp_parser.parse()
    print(exp_parser.get_output())

