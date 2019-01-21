from .tokens import tokens as token_list

import compiler.ast as ast


class ParserRule:
    def check(self, tokens):
        return False

    def eval(self, tokens):
        return None


class PragmaRule(ParserRule):
    def check(self, tokens):
        ok = True
        ok = ok and (tokens[0].name == 'DELIM_LESS' and tokens[len(tokens) - 1].name == 'DELIM_GREATER')

        kw = False
        for tok in tokens[1:-1]:
            if tok.name == 'IDENT_KEYWORD' and not kw:
                kw = True
            elif tok.name == 'LITERAL_STRING' and kw:
                kw = False
            else:
                return False

        return ok and not kw

    def eval(self, tokens):
        body = dict()

        return ast.Pragma(body)


class Parser:
    def __init__(self):
        self.token_names = [tok.name for tok in token_list]
        self.rules = [PragmaRule()]
        self.result = []

    def parse(self, tokens):
        buffer = []
        for token in tokens:
            buffer.append(token)
            for rule in self.rules:
                if rule.check(buffer):
                    self.result.append(rule.eval(buffer))
                    buffer = []
                    break

        return self.result

