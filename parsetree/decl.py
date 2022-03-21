from tokenizer import TOKEN_MAP, Tokenizer


class Decl:
    def __init__(self):
        self.id_list = None

    def parse(self):
        if (Tokenizer.get_token() == TOKEN_MAP["int"]):
            Tokenizer.skip_token()
        else:
            print(f"Missing \"int\" keyword in declaration statement")
            return

        from .id_list import IdList
        self.id_list = IdList()
        self.id_list.parse()

        if (Tokenizer.get_token() == TOKEN_MAP[";"]):
            Tokenizer.skip_token()
        else:
            print(f"Missing \";\" keyword in declaration statement")
            return

    def print(self):
        return self

    def execute(self):
        return self
