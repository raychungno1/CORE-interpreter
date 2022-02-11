import csv

from sqlalchemy import null


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
        last_token_symbol = False
        whitespace_present = False

        while index < len(line):
            char = line[index]

            token = ""
            if char.isdigit():
                token = Tokenizer.__tokenize_int(line, index)
                whitespace_error = len(self.tokens) > 0 and not(last_token_symbol) and not(whitespace_present)
                self.token_ids.append(Tokenizer.token_map["integer"])
                last_token_symbol = False
                whitespace_present = False

            elif char in Tokenizer.whitespace:
                token = Tokenizer.__tokenize_whitespace(line, index)
                whitespace_present = True
                index += len(token)
                continue

            elif char.isupper():
                token = Tokenizer.__tokenize_identifier(line, index)
                whitespace_error = len(self.tokens) > 0 and not(last_token_symbol) and not(whitespace_present)
                self.token_ids.append(Tokenizer.token_map["id"])
                last_token_symbol = False
                whitespace_present = False

            elif char.islower():
                token = Tokenizer.__tokenize_word(line, index)
                if len(token) > 0:
                    whitespace_error = len(self.tokens) > 0 and not(last_token_symbol) and not(whitespace_present)
                    self.token_ids.append(Tokenizer.token_map[token])
                    last_token_symbol = False
                    whitespace_present = False

            else:
                token = Tokenizer.__tokenize_symbol(line, index)
                if len(token) > 0:
                    self.token_ids.append(Tokenizer.token_map[token])
                    last_token_symbol = True
                    whitespace_present = False

            if len(token) == 0:
                print("invalid token")
                return False

            if whitespace_error:
                print("whitespace error: ", token)
                return False

            self.tokens.append(token)
            index += len(token)

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
