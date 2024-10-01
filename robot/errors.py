
# *******************ERRORS*******************

class PortError(Exception):
    def __init__(self, message: str, errorCode: str):
        super().__init__(message)
        self.errorCode = errorCode

    def __str__(self):
        return f"{self.message} (Error Code): {self.errorCode}"

class LackOfInput(Exception):
    def __init__(self, message: str, errorCode: str):
        super().__init__(message)
        self.errorCode = errorCode

    def __str__(self):
        return f"{self.message} (Error Code): {self.errorCode}"