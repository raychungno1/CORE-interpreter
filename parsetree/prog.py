from tokenizer import TOKEN_MAP, Tokenizer
from .helper import check_and_skip_token

class Prog:
    def __init__(self):
        if (Tokenizer.instance is None):
            print("Tokenizer not initialized")
            return

        self.decl_seq = None
        self.stmt_seq = None

    def parse(self):
        if (Tokenizer.get_token() == TOKEN_MAP["program"]):
            Tokenizer.skip_token()
        else:
            print(f"Missing \"program\" keyword in program statement")
            return

        from .decl_seq import DeclSeq
        self.decl_seq = DeclSeq()
        self.decl_seq.parse()

        if (Tokenizer.get_token() == TOKEN_MAP["begin"]):
            Tokenizer.skip_token()
        else:
            print(f"Missing \"begin\" keyword in program statement")
            return

        from .stmt_seq import StmtSeq
        self.stmt_seq = StmtSeq()
        self.stmt_seq.parse()

        if (Tokenizer.get_token() == TOKEN_MAP["end"]):
            Tokenizer.skip_token()
        else:
            print(f"Missing \"end\" keyword in program statement")

    def print(self):
        print("printing")
        return self

    def execute(self):
        print("executing")
        return self
