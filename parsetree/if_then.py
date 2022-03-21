from tokenizer import TOKEN_MAP, Tokenizer


class IfThen:
    def __init__(self):
        self.alt_no = 1
        self.cond = None
        self.stmt_seq_1 = None
        self.stmt_seq_2 = None

    def parse(self):
        if (Tokenizer.get_token() == TOKEN_MAP["if"]):
            Tokenizer.skip_token()
        else:
            print("Missing \"if\" keyword in if-then statement")
            return

        from .cond import Cond
        self.cond = Cond()
        self.cond.parse()

        if (Tokenizer.get_token() == TOKEN_MAP["then"]):
            Tokenizer.skip_token()
        else:
            print("Missing \"then\" keyword in if-then statement")
            return

        from .stmt import Stmt
        self.stmt_seq_1 = Stmt()
        self.stmt_seq_1.parse()

        if (Tokenizer.get_token() == TOKEN_MAP["else"]):
            Tokenizer.skip_token()
            self.stmt_seq_2 = Stmt()
            self.stmt_seq_2.parse()

        if (Tokenizer.get_token() == TOKEN_MAP["end"]):
            Tokenizer.skip_token()
        else:
            print("Missing \"end\" keyword in if-then statement")

        if (Tokenizer.get_token() == TOKEN_MAP[";"]):
            Tokenizer.skip_token()
        else:
            print("Missing \";\" keyword in if-then statement")
            return

    def print(self):
        return self

    def execute(self):
        return self
