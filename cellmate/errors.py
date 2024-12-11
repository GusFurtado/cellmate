class CellmateException(Exception):
    """
    Custom exception raised for errors encountered while constructing
    or manipulating an Excel table.
    """

    def __init__(self, message="An error occurred while processing the Excel table"):
        super().__init__(message)
