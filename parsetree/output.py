from tokenizer import TOKEN_MAP, Tokenizer


class Output:
    def __init__(self):
        self.id_list = None

    def parse(self):
        if (Tokenizer.get_token() == TOKEN_MAP["write"]):
            Tokenizer.skip_token()
        else:
            print("Missing \"write\" keyword in output statement")
            return

        from .id_list import IdList
        self.id_list = IdList()
        self.id_list.parse()

        if (Tokenizer.get_token() == TOKEN_MAP[";"]):
            Tokenizer.skip_token()
        else:
            print("Missing \";\" keyword in loop statement")
            return

    def print(self):
        return self

    def execute(self):
        return self
