# Raised when model output doesn't adhere to the specified format for changes
class ModelError(Exception):
    def __init__(self, message: str, already_added_to_changelist: bool):
        super().__init__(message)
        self.already_added_to_changelist = already_added_to_changelist


# Used to indicate an issue with Dotcoder's code
class DotcoderError(Exception):
    pass


# Used to indicate an issue with the user's usage of Dotcoder
class UserError(Exception):
    pass
