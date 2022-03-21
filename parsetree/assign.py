from tokenizer import TOKEN_MAP, Tokenizer


class Assign:
    def __init__(self):
        self.id = None
        self.exp = None

    def parse(self):
        from .id import Id
        if (Tokenizer.get_token() == TOKEN_MAP["id"] and Id.has_id(Tokenizer.id_name())):
            self.id = Tokenizer.id_name()
            Tokenizer.skip_token()
        else:
            print("Missing id in assignment statement")
            return

        if (Tokenizer.get_token() == TOKEN_MAP["="]):
            Tokenizer.skip_token()
        else:
            print("Missing \"=\" keyword in assignment statement")
            return

        from .exp import Exp
        self.exp = Exp()
        self.exp.parse()

        if (Tokenizer.get_token() == TOKEN_MAP[";"]):
            Tokenizer.skip_token()
        else:
            print("Missing \";\" keyword in assignment statement")
            return

    def print(self):
        return self

    def execute(self):
        return self
