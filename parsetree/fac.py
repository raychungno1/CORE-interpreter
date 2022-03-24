from tokenizer import TOKEN_MAP, Tokenizer


class Fac:
    def __init__(self):
        self.alt_no = 1
        self.op = None
        self.fac = None

    def parse(self):
        from .op import Op
        self.op = Op()
        self.op.parse()

        if Tokenizer.get_token() == TOKEN_MAP["*"]:
            self.alt_no = 2
            Tokenizer.skip_token()
            self.fac = Fac()
            self.fac.parse()

    def print(self):
        self.op.print()

        if self.alt_no == 2:
            print(" * ", end="")
            self.fac.print()

    def execute(self):
        if self.alt_no == 1:
            return self.op.execute()

        else:
            return self.op.execute() * self.fac.execute()
