from tokenizer import TOKEN_MAP, Tokenizer


class Stmt:
    def __init__(self):
        self.alt_no = 1
        self.assign = None
        self.if_then = None
        self.loop = None
        self.input = None
        self.output = None

    def parse(self):
        if (Tokenizer.get_token() == TOKEN_MAP["id"]):
            from .assign import Assign
            self.assign = Assign()
            self.assign.parse()

        elif (Tokenizer.get_token() == TOKEN_MAP["if"]):
            self.alt_no = 2

            from .if_then import IfThen
            self.if_then = IfThen()
            self.if_then.parse()

        elif (Tokenizer.get_token() == TOKEN_MAP["while"]):
            self.alt_no = 3

            from .loop import Loop
            self.loop = Loop()
            self.loop.parse()

        elif (Tokenizer.get_token() == TOKEN_MAP["read"]):
            self.alt_no = 4

            from .input import Input
            self.input = Input()
            self.input.parse()

        elif (Tokenizer.get_token() == TOKEN_MAP["write"]):
            self.alt_no = 5

            from .output import Output
            self.output = Output()
            self.output.parse()

        else:
            print(f"Invalid statement")

    def print(self):
        return self

    def execute(self):
        return self
