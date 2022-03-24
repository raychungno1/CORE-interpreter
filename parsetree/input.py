from error import ReadFileError
from tokenizer import TOKEN_MAP, Tokenizer


class Input:
    file = None

    @staticmethod
    def set_input_file(file_name):
        Input.file = open(file_name, "r")

    def __init__(self):
        self.id_list = None

    def parse(self):
        Tokenizer.check_and_skip_token("read", "Input")

        from .id_list import IdList
        self.id_list = IdList()
        self.id_list.parse()

        Tokenizer.check_and_skip_token(";", "Input")

    def print(self, depth=0, tab="\t"):
        print(depth * tab + "read ", end="")
        self.id_list.print()
        print(";")

    def execute(self):
        if Input.file == None:
            raise ReadFileError()

        from .id import Id
        self.id_list.execute(lambda id: Id.set_id(
            id, int(Input.file.readline())))
