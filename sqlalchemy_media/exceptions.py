

class SqlAlchemyMediaException(Exception):
    """
    The base class for all exceptions
    """
    pass


class MaximumLengthIsReachedError(SqlAlchemyMediaException):
    """
    Indicates the maximum allowed file limit is reached.
    """

    def __init__(self, max_length: int):
        super().__init__('Cannot store files smaller than: %d bytes' % max_length )


class MinimumLengthIsNotReachedError(SqlAlchemyMediaException):
    """
    Indicates the minimum allowed length is not \.
    """

    def __init__(self, min_length):
        super().__init__('Cannot store files larger than: %d bytes' % min_length)
