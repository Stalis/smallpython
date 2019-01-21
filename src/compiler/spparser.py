from sly import Parser
from .splexer import SPLexer

class SPParser(Parser):
    tokens = SPLexer.tokens

