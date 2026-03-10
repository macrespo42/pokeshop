class ApplicationException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class InvalidRarityError(ApplicationException):
    def __init__(self, message: str = "Invalid Rarity"):
        super().__init__(message)


class InvalidPhysicalStateError(ApplicationException):
    def __init__(self, message: str = "Invalid Physical State"):
        super().__init__(message)


class InvalidEditionError(ApplicationException):
    def __init__(self, message: str = "Invalid Edition"):
        super().__init__(message)


class InvalidNameError(ApplicationException):
    def __init__(self, message: str = "Invalid Name"):
        super().__init__(message)


class InvalidStatusError(ApplicationException):
    def __init__(self, message: str = "Invalid Status"):
        super().__init__(message)


class InvalidPokemonTypeError(ApplicationException):
    def __init__(self, message: str = "Invalid Pokemon Type"):
        super().__init__(message)


class CardAlreadySoldError(ApplicationException):
    def __init__(self, message: str = "Card already sold"):
        super().__init__(message)


class CreateUnavailableCardError(ApplicationException):
    def __init__(
        self, message: str = "Card must be available when added to the catalog"
    ):
        super().__init__(message)


class SellAlreadySoledCardError(ApplicationException):
    def __init__(self, message: str = "Can't sell a retired card"):
        super().__init__(message)
