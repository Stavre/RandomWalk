from random_walk import keep_to_field


class Field:
    """class for modelling a field.
    unfinished"""

    def __init__(self, walkers=None, field_length=None, field_height=None, rules=None):
        if rules is None:
            rules = []
        if field_height is None:
            field_height = [1, -1]
        if field_length is None:
            field_length = [1, -1]
        if rules is None:
            rules = []

        self.walkers = walkers
        self.field_length = field_length
        self.field_height = field_height
        self.rules = rules

    def walk(self, steps=1):
        for walker in self.walkers:
            for rule in self.rules:
                rule(self.field_length, self.field_height, walker)
                keep_to_field(self.field_length, self.field_height, walker)
                walker.take_steps(steps)
                rule(self.field_length, self.field_height, walker)

    def positions(self):
        return [x.current_point for x in self.walkers]
