from tokenizer import TOKEN_MAP, Tokenizer


class Decl:
    def __init__(self):
        self.id_list = None

    def parse(self):
        Tokenizer.check_and_skip_token("int", "Declaration")

        from .id_list import IdList
        self.id_list = IdList()
        self.id_list.parse()

        Tokenizer.check_and_skip_token(";", "Declaration")

    def print(self):
        return self

    def execute(self):
        return self
