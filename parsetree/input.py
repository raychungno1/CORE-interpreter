from tokenizer import TOKEN_MAP, Tokenizer


class Input:
    def __init__(self):
        self.id_list = None

    def parse(self):
        Tokenizer.check_and_skip_token("read", "Input")

        from .id_list import IdList
        self.id_list = IdList()
        self.id_list.parse()

        Tokenizer.check_and_skip_token(";", "Input")

    def print(self):
        return self

    def execute(self):
        return self
