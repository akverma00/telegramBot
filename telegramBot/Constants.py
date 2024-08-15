
class Constants:
    def __init__(self):
    # Dictionary mapping source chat IDs to lists of target chat IDs.
    # Each key in the dictionary is a source chat ID, and 
    # the corresponding value is a list of target chat IDs to which messages from the source chat should be forwarded.
        self.SOURCE_TO_TARGET_MAP = {
            -1002008905623: [
                -1001833328420,
                -1002133513866,
                -1002056442424
            ],
            -1001809265514: [
                -1001945508703,
                -1001833328420,
                -1001905014374,
                -1002121131434,
                -1002133513866,
                -1002056442424
            ],
            -1001985321961: [
                -1001945508703,
                -1002056442424
            ]
        }

        self.WHITELIST_MESSAGES_MAP = {
            -1002008905623: [
                "abcdef"
            ],
            -1001809265514: [
                "abcdef"
            ]
        }

        self.BLACKLIST_MESSAGES_MAP = {
        -1002008905623: [
            "http",
            "@"
        ],
        -1001809265514: [
            "http",
            "@"
        ],
        -1001985321961: [
            "http",
            "@"
        ]
    }
