from lib2to3.pgen2.grammar import Grammar
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

        if first_token == TOKEN_MAP["int"]:
            self.int = Tokenizer.int_val()
            Tokenizer.skip_token()

        elif first_token == TOKEN_MAP["id"]:
            self.id = Tokenizer.id_name()

        elif first_token == TOKEN_MAP["("]:
            Tokenizer.skip_token()
            from .exp import Exp
            self.exp = Exp()
            self.exp.parse()

            Tokenizer.check_and_skip_token("(", "Op")

        else:
            raise GrammarError("<id> / <int> / (", "Op")

    def print(self):
        return self

    def execute(self):
        return self
