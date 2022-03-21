from tokenizer import TOKEN_MAP, Tokenizer


class Loop:
    def __init__(self):
        self.cond = None
        self.stmt_seq = None

    def parse(self):
        if (Tokenizer.get_token() == TOKEN_MAP["while"]):
            Tokenizer.skip_token()
        else:
            print("Missing \"while\" keyword in loop statement")
            return

        from .cond import Cond
        self.cond = Cond()
        self.cond.parse()

        if (Tokenizer.get_token() == TOKEN_MAP["loop"]):
            Tokenizer.skip_token()
        else:
            print("Missing \"loop\" keyword in loop statement")
            return

        from .stmt_seq import StmtSeq
        self.stmt_seq = StmtSeq()
        self.stmt_seq.parse()

        if (Tokenizer.get_token() == TOKEN_MAP["end"]):
            Tokenizer.skip_token()
        else:
            print("Missing \"end\" keyword in loop statement")

        if (Tokenizer.get_token() == TOKEN_MAP[";"]):
            Tokenizer.skip_token()
        else:
            print("Missing \";\" keyword in loop statement")
            return

    def print(self):
        return self

    def execute(self):
        return self
