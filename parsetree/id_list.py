from tokenizer import TOKEN_MAP, Tokenizer


class IdList:
    def __init__(self):
        self.alt_no = 1
        self.id = None
        self.id_list = None

    def parse(self):
        if (Tokenizer.get_token() == TOKEN_MAP["id"]):
            self.id = Tokenizer.id_name
            
            from .id import Id
            Id.add_id(self.id)
            Tokenizer.skip_token()
        else:
            print(f"Missing id name in id list")
            return

        if (Tokenizer.get_token() == TOKEN_MAP[","]):
            Tokenizer.skip_token()
            self.alt_no = 2
            self.id_list = IdList()
            self.id_list.parse()

    def print(self):
        return self

    def execute(self):
        return self