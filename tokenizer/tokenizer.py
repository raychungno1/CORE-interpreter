from tokenize import Token
from tokenizer import TOKEN_MAP


class Tokenizer:
    instance = None

    @staticmethod
    def get_token():
        return Tokenizer.instance.getToken()

    @staticmethod
    def skip_token():
        return Tokenizer.instance.skipToken()

    @staticmethod
    def int_val():
        return Tokenizer.instance.intVal()

    @staticmethod
    def id_name():
        return Tokenizer.instance.idName()

    def __init__(self, code_file, input_file):
        """Initializes a new Tokenizer with input file \"file_name\"."""
        if (Tokenizer.instance is not None):
            return

        self.tokens = []
        self.token_ids = []
        self.isEOF = False
        self.code_file = open(code_file, "r")
        self.input_file = open(input_file, "r")

        line = self.code_file.readline()
        if (line):
            self.__tokenize_line(line)
        else:
            self.isEOF = True
            self.token_ids.append(TOKEN_MAP["EOF"])

        Tokenizer.instance = self

    def getToken(self):
        """Return the id of the current token,
        or None if the end of file has been reached.
        """
        if (self.isEOF):
            return None
        elif self.token_ids:
            return self.token_ids[0]
        else:
            self.isEOF = True
            return TOKEN_MAP["EOF"]

    def skipToken(self):
        """Consumes the current token and moves the the next one if it exists."""
        if self.isEOF:
            return

        if self.token_ids:
            token = self.token_ids.pop(0)
            if (TOKEN_MAP[token] == "integer" or TOKEN_MAP[token] == "id"):
                self.tokens.pop(0)

        while not(self.token_ids) and (line := self.code_file.readline()):
            self.__tokenize_line(line)

    def intVal(self):
        """Return the int value of the current integer token."""
        return self.tokens[0]

    def idName(self):
        """Return the value of the current identifier token."""
        return self.tokens[0]

    def __tokenize_line(self, line):
        """Converts a string into valid CORE tokens
        while enforcing whitespace requirement.
        """
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
                self.token_ids.append(TOKEN_MAP[token])
                last_token_symbol = True

            else:
                if token := Tokenizer.__tokenize_word(line, index):
                    self.token_ids.append(TOKEN_MAP[token])

                elif token := Tokenizer.__tokenize_int(line, index):
                    self.token_ids.append(TOKEN_MAP["integer"])
                    self.tokens.append(token)

                elif token := Tokenizer.__tokenize_identifier(line, index):
                    self.token_ids.append(TOKEN_MAP["id"])
                    self.tokens.append(token)

                whitespace_error = self.tokens and not(
                    last_token_symbol or whitespace_present)
                last_token_symbol = False

            whitespace_present = False
            index += len(token)

            if len(token) == 0:
                print("invalid token")
                self.isEOF = True

            if whitespace_error:
                print("whitespace error: ", line.strip())
                self.isEOF = True

    def __tokenize_int(line, start_index):
        """Returns an integer token beginning at line[start_index], if exists."""
        end_index = start_index

        while (end_index < len(line) and line[end_index].isdigit()):
            end_index += 1

        return line[start_index: end_index]

    def __tokenize_whitespace(line, start_index):
        """Returns a whitespace token beginning at line[start_index], if exists."""
        end_index = start_index

        while (end_index < len(line) and line[end_index] in "\t\r \n"):
            end_index += 1

        return line[start_index: end_index]

    def __tokenize_identifier(line, start_index):
        """Returns an identifier token beginning at line[start_index], if exists."""
        end_index = start_index

        while (end_index < len(line) and
               (line[end_index].isdigit() or line[end_index].isupper())):
            end_index += 1

        return line[start_index: end_index]

    def __tokenize_word(line, start_index):
        """Returns a reserved word token beginning at line[start_index], if exists."""
        for word in ["program", "begin", "end", "int", "if",
                     "then", "else", "while", "loop", "read", "write"]:
            if line.find(word, start_index) == start_index:
                return word

    def __tokenize_symbol(line, start_index):
        """Returns an sumbol token beginning at line[start_index], if exists."""
        end_index = start_index

        if line[end_index] in "=!<>":
            end_index += 1
            if line[end_index] == "=":
                end_index += 1

        elif line[end_index] in ";,[]()+-*":
            end_index += 1

        elif line.find("||", start_index) != -1 or line.find("&&", start_index) != -1:
            end_index += 2

        return line[start_index: end_index]
