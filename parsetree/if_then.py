from tokenizer import TOKEN_MAP, Tokenizer


class IfThen:
    def __init__(self):
        self.alt_no = 1
        self.cond = None
        self.stmt_seq_1 = None
        self.stmt_seq_2 = None

    def parse(self):
        Tokenizer.check_and_skip_token("if", "if-then")

        from .cond import Cond
        self.cond = Cond()
        self.cond.parse()

        Tokenizer.check_and_skip_token("then", "if-then")

        from .stmt import Stmt
        self.stmt_seq_1 = Stmt()
        self.stmt_seq_1.parse()

        if (Tokenizer.get_token() == TOKEN_MAP["else"]):
            self.alt_no = 2
            Tokenizer.skip_token()
            self.stmt_seq_2 = Stmt()
            self.stmt_seq_2.parse()

        Tokenizer.check_and_skip_token("end", "if-then")
        Tokenizer.check_and_skip_token(";", "if-then")

    def print(self, depth = 0, tab = "\t"):
        print(depth * tab + "if", end = "")
        self.cond.print()
        print(depth * tab + "then")
        self.stmt_seq_1.print(depth + 1, tab)

        if self.alt_no == 2:
            print(depth * tab + "else")
            self.stmt_seq_2.print(depth + 1, tab)

        print(depth * tab + "end;")

    def execute(self):
        return self
