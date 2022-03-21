from error import GrammarError, IdMissingError
from tokenizer import TOKEN_MAP, Tokenizer


class Assign:
    def __init__(self):
        self.id = None
        self.exp = None

    def parse(self):
        if Tokenizer.get_token() != TOKEN_MAP["id"]:
            raise GrammarError("<id>", "Assign")

        self.id = Tokenizer.id_name()
        Tokenizer.skip_token()

        from .id import Id
        if not Id.has_id(self.id):
            raise IdMissingError(Tokenizer.id_name())

        Tokenizer.check_and_skip_token("=", "Assign")

        from .exp import Exp
        self.exp = Exp()
        self.exp.parse()

        Tokenizer.check_and_skip_token(";", "Assign")

    def print(self):
        return self

    def execute(self):
        return self
