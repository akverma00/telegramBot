# telegramBot/Validater.py

class Validator:

    @staticmethod
    def isMessageValidated(message, blacklist, whitelist):
        if Validator.blacklistMessagesCheck(message, blacklist) and Validator.whitelistMessagesCheck(message, whitelist):
            return True
        return False

    @staticmethod
    def blacklistMessagesCheck(message, blacklist):
        for word in blacklist:
            if word in message:
                return False
        return True

    @staticmethod
    def whitelistMessagesCheck(message, whitelist):
        for word in whitelist:
            if word in message:
                return True
        return False