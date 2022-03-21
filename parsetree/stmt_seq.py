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

        token = Tokenizer.get_token()
        if (token == TOKEN_MAP["id"] or
            token == TOKEN_MAP["if"] or
            token == TOKEN_MAP["while"] or
            token == TOKEN_MAP["read"] or
                token == TOKEN_MAP["write"]):

            self.alt_no = 2
            self.stmt_seq = StmtSeq()
            self.stmt_seq.parse()

    def print(self):
        return self

    def execute(self):
        return self
