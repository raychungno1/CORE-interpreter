from tokenizer import TOKEN_MAP, Tokenizer


class StmtSeq:
    def __init__(self):
        self.alt_no = 1
        self.stmt = None
        self.stmt_seq = None

    def parse(self):
        from .stmt import Stmt
        self.stmt = Stmt()
        self.stmt.parse()

        if TOKEN_MAP[Tokenizer.get_token()] in ["id", "if", "while", "read", "write"]:
            self.alt_no = 2
            self.stmt_seq = StmtSeq()
            self.stmt_seq.parse()

    def print(self):
        return self

    def execute(self):
        return self
