from error import GrammarError
from tokenizer import TOKEN_MAP, Tokenizer


class Op:
    def __init__(self):
        self.alt_no = 1
        self.int = None
        self.id = None
        self.exp = None

    def parse(self):
        first_token = Tokenizer.get_token()

        if first_token == TOKEN_MAP["integer"]:
            self.int = Tokenizer.int_val()
            Tokenizer.skip_token()

        elif first_token == TOKEN_MAP["id"]:
            self.alt_no = 2
            self.id = Tokenizer.id_name()
            Tokenizer.skip_token()

        elif first_token == TOKEN_MAP["("]:
            self.alt_no = 3
            Tokenizer.skip_token()
            from .exp import Exp
            self.exp = Exp()
            self.exp.parse()

            Tokenizer.check_and_skip_token(")", "Op")

        else:
            raise GrammarError("<id> / <int> / (", "Op")

    def print(self):
        if self.alt_no == 1:
            print(self.int, end = "")
        elif self.alt_no == 2:
            print(self.id, end = "")
        else:
            print("(", end = "")
            self.exp.print()
            print(")", end = "")

    def execute(self):
        return self
