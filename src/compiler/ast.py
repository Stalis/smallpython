class Ident:
    def __init__(self, name):
        self.name = name


class UnaryMessage:
    def __init__(self, receiver, message):
        self._receiver = receiver
        self._message = message

    def receiver(self):
        return self._receiver

    def message(self):
        return self._message


class BinaryMessage(UnaryMessage):
    def __init__(self, receiver, message, arg):
        super().__init__(receiver, message)
        self._arg = arg

    def arg(self):
        return self._arg


class KeywordMessage:
    def __init__(self, receiver, args_dict):
        self._receiver = receiver
        self._args_dict = args_dict

    def receiver(self):
        return self._receiver

    def args_dict(self):
        return self._args_dict


class Pragma(KeywordMessage):
    def __init__(self, args_dict):
        super().__init__('Pragma', args_dict)


class Expression:
    pass


class Literal(Expression):
    pass


class Symbol(Literal):
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)


class SymbolSelector(Symbol):
    pass


class SymbolId(Symbol):
    pass


class Context(Expression):
    def __init__(self):
        self.locals = dict()
        self.public = dict()

    def add_local(self, name: Symbol, body: Expression):
        self.locals[name] = body

    def add_public(self, name: Symbol, body: Expression):
        self.public[name] = body


class Integer:
    def __init__(self, value):
        self._value = value

    def eval(self):
        return int(self._value)


class Float:
    def __init__(self, value):
        self._value = value

    def eval(self):
        return float(self._value)


class String:
    def __init__(self, value):
        self._value = value

    def eval(self):
        self._value = str(self._value)
