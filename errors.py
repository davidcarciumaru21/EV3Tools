class PortError(Exception):
    def __init__(self, message: str, errorCode: str):
        self.message = message
        self.errorCode = errorCode
        super().__init__(message)

    def __str__(self):
        return f"{self.message} (Error Code: {self.errorCode})"

class LackOfInput(Exception):
    def __init__(self, message: str, errorCode: str):
        self.message = message
        self.errorCode = errorCode
        super().__init__(message)

    def __str__(self):
        return f"{self.message} (Error Code: {self.errorCode})"
        
class UnknownOrientation(Exception):
    def __init__(self, message: str, errorCode: str):
        self.message = message
        self.errorCode = errorCode
        super().__init__(message)

    def __str__(self):
        return f"{self.message} (Error Code: {self.errorCode})"
        
class UnknownSpeed(Exception):
    def __init__(self, message: str, errorCode: str):
        self.message = message
        self.errorCode = errorCode
        super().__init__(message)

    def __str__(self):
        return f"{self.message} (Error Code: {self.errorCode})"

class UnknownStopMethod(Exception):
    def __init__(self, message: str, errorCode: str):
        self.message = message
        self.errorCode = errorCode
        super().__init__(message)

    def __str__(self):
        return f"{self.message} (Error Code: {self.errorCode})"

class UnknownFace(Exception):
    def __init__(self, message: str, errorCode: str):
        self.message = message
        self.errorCode = errorCode
        super().__init__(message)

    def __str__(self):
        return f"{self.message} (Error Code: {self.errorCode})"
        
class UnknownTimeArgument(Exception):
    def __init__(self, message: str, errorCode: str):
        self.message = message
        self.errorCode = errorCode
        super().__init__(message)

    def __str__(self):
        return f"{self.message} (Error Code: {self.errorCode})"
        
class UnableToWriteText(Exception):
    def __init__(self, message: str, errorCode: str):
        self.message = message
        self.errorCode = errorCode
        super().__init__(message)

    def __str__(self):
        return f"{self.message} (Error Code: {self.errorCode})"