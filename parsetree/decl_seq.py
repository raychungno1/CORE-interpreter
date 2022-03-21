from tokenizer import TOKEN_MAP, Tokenizer


class DeclSeq:
    def __init__(self):
        self.alt_no = 1
        self.decl = None
        self.decl_seq = None

    def parse(self):
        from .decl import Decl
        self.decl = Decl()
        self.decl.parse()

        if Tokenizer.get_token() != TOKEN_MAP["begin"]:
            self.alt_no = 2
            self.decl_seq = DeclSeq()
            self.decl_seq.parse()

        from .id import Id
        Id.declaring = False

    def print(self, depth = 0, tab = "\t"):
        self.decl.print(depth, tab)
        if self.alt_no == 2:
            self.decl_seq.print(depth, tab)

    def execute(self):
        return self
