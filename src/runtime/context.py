class Context:
    def __init__(self):
        self.vars = list()
        self.methods = list()
        self.classes = list()

    def add_var(self, var_name):
        self.vars.count(var_name)
