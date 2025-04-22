class EventValidationError(Exception):
    def __init__(self, errors):
        self.errors = errors
        super().__init__("Event validation failed:\n" + "\n".join(errors))
