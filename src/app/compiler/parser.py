from typing import List


class Parser:
    def __init__(self, expr: str):
        self.position: int = 0
        self.expr: str = expr
        self.look_ahaed: str = self.expr[0]
        self.parsed_expr: List = []

    def parse(self):
        self.term()
        while self.position < len(self.expr) - 1:
            if self.look_ahaed == "+":
                self.match("+")
                self.term()
                self.parsed_expr.append("+")
            elif self.look_ahaed == "-":
                self.match("-")
                self.term()
                self.parsed_expr.append("-")
            else:
                return

    def term(self):
        if self.look_ahaed.isalnum():
            self.parsed_expr.append(self.look_ahaed)
            self.match(self.look_ahaed)
        else:
            raise ValueError("Syntax Error")

    def match(self, t: str):
        if self.position == len(self.expr) - 1:
            return
        if self.look_ahaed == t:
            self.position += 1
            self.look_ahaed = self.expr[self.position]
        else:
            raise ValueError("Syntax Error")

    def get_output(self) -> str:
        output = "".join(self.parsed_expr)
        self.position = 0
        self.parsed_expr = []
        return output
