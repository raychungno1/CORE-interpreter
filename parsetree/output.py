from tokenizer import TOKEN_MAP, Tokenizer


class Output:
    def __init__(self):
        self.id_list = None

    def parse(self):
        Tokenizer.check_and_skip_token("write", "Output")

        from .id_list import IdList
        self.id_list = IdList()
        self.id_list.parse()

        Tokenizer.check_and_skip_token(";", "Output")

    def print(self, depth = 0, tab = "\t"):
        print(depth * tab + "write ", end = "")
        self.id_list.print()
        print(";")

    def execute(self):
        return self
