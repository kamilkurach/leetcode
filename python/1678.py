# 1678. Goal Parser Interpretation
class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("()", "o").replace("(al)", "al")
        return command
