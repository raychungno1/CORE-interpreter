from error import GrammarError, IdMissingError
from tokenizer import TOKEN_MAP, Tokenizer


class IdList:
    def __init__(self):
        self.alt_no = 1
        self.id = None
        self.id_list = None

    def parse(self):
        if (Tokenizer.get_token() == TOKEN_MAP["id"]):
            self.id = Tokenizer.id_name()
            Tokenizer.skip_token()
            
            from .id import Id
            Id.add_id(self.id)
            if not Id.has_id(self.id):
                raise IdMissingError(self.id)

        else:
            raise GrammarError("<id>", "Id List")

        if (Tokenizer.get_token() == TOKEN_MAP[","]):
            Tokenizer.skip_token()
            self.alt_no = 2
            self.id_list = IdList()
            self.id_list.parse()

    def print(self):
        print(self.id, end = "")
        if self.alt_no == 2:
            print(", ", end = "")
            self.id_list.print()

    def execute(self):
        return self
