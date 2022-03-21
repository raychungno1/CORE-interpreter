from tokenizer import TOKEN_MAP, Tokenizer


class Prog:
    def __init__(self):
        self.decl_seq = None
        self.stmt_seq = None

    def parse(self):
        Tokenizer.check_and_skip_token("program", "Program")

        from .decl_seq import DeclSeq
        self.decl_seq = DeclSeq()
        self.decl_seq.parse()

        Tokenizer.check_and_skip_token("begin", "Program")

        from .stmt_seq import StmtSeq
        self.stmt_seq = StmtSeq()
        self.stmt_seq.parse()

        Tokenizer.check_and_skip_token("end", "Program")

        return self

    def print(self, depth = 0, tab = "\t"):
        print(depth * tab + "program")
        self.decl_seq.print(depth+1, tab)
        print(depth * tab + "begin")
        self.stmt_seq.print(depth+1, tab)
        print(depth * tab + "end")

        return self

    def execute(self):
        print("executing")
        return self
