from tokenizer import TOKEN_MAP, Tokenizer


class Loop:
    def __init__(self):
        self.cond = None
        self.stmt_seq = None

    def parse(self):
        Tokenizer.check_and_skip_token("while", "Loop")

        from .cond import Cond
        self.cond = Cond()
        self.cond.parse()

        Tokenizer.check_and_skip_token("loop", "Loop")

        from .stmt_seq import StmtSeq
        self.stmt_seq = StmtSeq()
        self.stmt_seq.parse()

        Tokenizer.check_and_skip_token("end", "if-then")
        Tokenizer.check_and_skip_token(";", "if-then")

    def print(self):
        return self

    def execute(self):
        return self
