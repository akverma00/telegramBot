# telegramBot/Validater.py

class Validator:

    @staticmethod
    def isMessageValidated(message: str, blacklist: list[str], whitelist: list[str]):
        if blacklist is not None and Validator.blacklistMessages(message, blacklist) == True:
            return False
        if whitelist is not None and  Validator.whitelistMessages(message, whitelist) ==  True:
            return True
        return True

    @staticmethod
    def blacklistMessages(message: str, blacklist: list[str]):
        for word in blacklist:
            if word in message:
                return True
        return False

    @staticmethod
    def whitelistMessages(message: str, whitelist: list[str]):
        for word in whitelist:
            if word in message:
                return True
        return False