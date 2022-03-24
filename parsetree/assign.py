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
            raise IdMissingError(self.id)

        Tokenizer.check_and_skip_token("=", "Assign")

        from .exp import Exp
        self.exp = Exp()
        self.exp.parse()

        Tokenizer.check_and_skip_token(";", "Assign")

    def print(self, depth=0, tab="\t"):
        print(depth * tab + self.id + " = ", end="")
        self.exp.print()
        print(";")

    def execute(self):
        from .id import Id
        Id.set_id(self.id, self.exp.execute())
