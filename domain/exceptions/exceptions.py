class DomainException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class InvalidRarityError(DomainException):
    def __init__(self, message: str = "Invalid Rarity"):
        super().__init__(message)


class InvalidPhysicalStateError(DomainException):
    def __init__(self, message: str = "Invalid Physical State"):
        super().__init__(message)


class InvalidEditionError(DomainException):
    def __init__(self, message: str = "Invalid Edition"):
        super().__init__(message)


class InvalidNameError(DomainException):
    def __init__(self, message: str = "Invalid Name"):
        super().__init__(message)


class InvalidStatusError(DomainException):
    def __init__(self, message: str = "Invalid Status"):
        super().__init__(message)


class InvalidPokemonTypeError(DomainException):
    def __init__(self, message: str = "Invalid Pokemon Type"):
        super().__init__(message)


class CardAlreadySoldError(DomainException):
    def __init__(self, message: str = "Card already sold"):
        super().__init__(message)


class CreateUnavailableCardError(DomainException):
    def __init__(
        self, message: str = "Card must be available when added to the catalog"
    ):
        super().__init__(message)


class SellAlreadySoldCardError(DomainException):
    def __init__(self, message: str = "Can't sell a retired card"):
        super().__init__(message)


class RemoveAlreadySoldCardError(DomainException):
    def __init__(self, message: str = "You can't retire a card who is already sold"):
        super().__init__(message)


class RemoveReservedCardError(DomainException):
    def __init__(self, message: str = "You can't remove an reserved card"):
        super().__init__(message)
