import csv


class Tokenizer:

    whitespace = "\t\r \n"
    words = ["program", "begin", "end", "int", "if",
             "then", "else", "while", "loop", "read", "write"]

    with open('token-map.csv', mode='r') as infile:
        reader = csv.reader(infile)
        token_map = dict((rows[0], rows[1]) for rows in reader)

    def __init__(self, file_name):

        # Load token mapping

        self.tokens = []
        self.token_ids = []
        with open(file_name) as input_file:
            for line in input_file:
                print(line, end="")
                if not(self.__tokenize_line(line)):
                    return

        print(self.tokens)
        print(self.token_ids)

    def __tokenize_line(self, line):
        index = 0

        while index < len(line):
            char = line[index]

            token = " "
            if char.isdigit():
                token = Tokenizer.__tokenize_int(line, index)
                self.token_ids.append(Tokenizer.token_map["integer"])

            elif char in Tokenizer.whitespace:
                token = Tokenizer.__tokenize_whitespace(line, index)
                self.token_ids.append(0)

            elif char.isupper():
                token = Tokenizer.__tokenize_identifier(line, index)
                self.token_ids.append(Tokenizer.token_map["id"])

            elif char.islower():
                token = Tokenizer.__tokenize_word(line, index)
                if len(token) > 0:
                    self.token_ids.append(Tokenizer.token_map[token])

            else:
                token = Tokenizer.__tokenize_symbol(line, index)
                if len(token) > 0:
                    self.token_ids.append(Tokenizer.token_map[token])

            if len(token) == 0:
                print("invalid token")
                return False

            self.tokens.append(token)
            index += len(token)

        self.token_ids.append(Tokenizer.token_map["EOF"])
        return True

    def __tokenize_int(line, start_index):
        end_index = start_index + 1

        while (end_index < len(line) and line[end_index].isdigit()):
            end_index += 1

        return line[start_index: end_index]

    def __tokenize_whitespace(line, start_index):
        end_index = start_index + 1

        while (end_index < len(line) and line[end_index] in Tokenizer.whitespace):
            end_index += 1

        return line[start_index: end_index]

    def __tokenize_identifier(line, start_index):
        end_index = start_index + 1

        while (end_index < len(line) and
               (line[end_index].isdigit() or line[end_index].isupper())):
            end_index += 1

        return line[start_index: end_index]

    def __tokenize_word(line, start_index):
        print(line[start_index:])
        for word in Tokenizer.words:
            if line.find(word, start_index) == start_index:
                print(word)
                return word
        return ""

    def __tokenize_symbol(line, start_index):
        end_index = start_index

        if end_index >= len(line):
            return ""

        if line[end_index] in ";,[]()+-*":
            end_index += 1

        elif line[end_index] in "=!<>":
            if line[end_index + 1] in "=":
                end_index += 2
            else:
                end_index += 1

        elif line.find("||", start_index) != -1 or line.find("&&", start_index) != -1:
            end_index += 2

        return line[start_index: end_index]
