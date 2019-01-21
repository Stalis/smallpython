from rply import LexerGenerator

from .tokens import tokens, ignore_regex


class Lexer:
    def __init__(self):
        self.lexer = LexerGenerator()

    def add_tokens(self):
        self.lexer.ignore(ignore_regex)
        for tok in tokens:
            self.lexer.add(tok.name, tok.regex)

    def get_lexer(self):
        self.add_tokens()
        return self.lexer.build()

    def get_tokens(self):
        return [rule.name for rule in self.lexer.rules]
