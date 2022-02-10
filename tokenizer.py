class Tokenizer:
    def __init__(self, file_name):
        with open(file_name) as input_file:
            for line in input_file:
                print(line, end="")