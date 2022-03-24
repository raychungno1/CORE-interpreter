from error import GrammarError
from tokenizer import TOKEN_MAP, Tokenizer


class Exp:
    def __init__(self):
        self.alt_no = 1
        self.fac = None
        self.exp = None

    def parse(self):
        from .fac import Fac
        self.fac = Fac()
        self.fac.parse()

        if Tokenizer.get_token() == TOKEN_MAP["+"]:
            self.alt_no = 2
            Tokenizer.skip_token()
            from .exp import Exp
            self.exp = Exp()
            self.exp.parse()

        elif Tokenizer.get_token() == TOKEN_MAP["-"]:
            self.alt_no = 3
            Tokenizer.skip_token()
            from .exp import Exp
            self.exp = Exp()
            self.exp.parse()

    def print(self):
        self.fac.print()
        if self.alt_no == 1:
            return

        if self.alt_no == 2:
            print(" + ", end="")
        else:
            print(" - ", end="")

        self.exp.print()

    def execute(self):
        if self.alt_no == 1:
            return self.fac.execute()

        elif self.alt_no == 2:
            return self.fac.execute() + self.exp.execute()

        else:
            return self.fac.execute() - self.exp.execute()
