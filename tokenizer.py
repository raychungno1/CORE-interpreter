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
                if not(self.__tokenize_line(line)):
                    return

        self.token_ids.append(Tokenizer.token_map["EOF"])

        # Index for traversal
        self.index = 0

    def getToken(self):
        if self.index < len(self.token_ids):
            return self.token_ids[self.index]
        return None

    def skipToken(self):
        if self.index <= len(self.token_ids):
            self.index += 1

    def __tokenize_line(self, line):
        index = 0
        whitespace_error = False
        whitespace_present = False
        last_token_symbol = False

        while index < len(line):

            if token := Tokenizer.__tokenize_whitespace(line, index):
                whitespace_present = True
                index += len(token)
                continue

            if token := Tokenizer.__tokenize_symbol(line, index):
                self.token_ids.append(Tokenizer.token_map[token])
                last_token_symbol = True

            else:
                if token := Tokenizer.__tokenize_word(line, index):
                    self.token_ids.append(Tokenizer.token_map[token])

                elif token := Tokenizer.__tokenize_identifier(line, index):
                    self.token_ids.append(Tokenizer.token_map["id"])

                elif token := Tokenizer.__tokenize_int(line, index):
                    self.token_ids.append(Tokenizer.token_map["integer"])

                whitespace_error = self.tokens and not(
                    last_token_symbol or whitespace_present)
                last_token_symbol = False

            whitespace_present = False

            if len(token) == 0:
                print("invalid token")
                return False

            if whitespace_error:
                print("whitespace error: ", line)
                return False

            self.tokens.append(token)
            index += len(token)

        return True

    def __tokenize_int(line, start_index):
        end_index = start_index

        while (end_index < len(line) and line[end_index].isdigit()):
            end_index += 1

        return line[start_index: end_index]

    def __tokenize_whitespace(line, start_index):
        end_index = start_index

        while (end_index < len(line) and line[end_index] in Tokenizer.whitespace):
            end_index += 1

        return line[start_index: end_index]

    def __tokenize_identifier(line, start_index):
        end_index = start_index

        while (end_index < len(line) and
               (line[end_index].isdigit() or line[end_index].isupper())):
            end_index += 1

        return line[start_index: end_index]

    def __tokenize_word(line, start_index):
        for word in Tokenizer.words:
            if line.find(word, start_index) == start_index:
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
