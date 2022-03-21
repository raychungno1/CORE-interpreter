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
        return self

    def execute(self):
        return self
