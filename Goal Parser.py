class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('(al)','al').replace('()','o')

# the second way to accomplish the task
class Solution:
    def interpret(self, command: str) -> str:
        x = ''
        for i in range(len(command)):
            if command[i] == 'G':
                a = 'G'
                x += a
            elif command[i] == '(' and command[i+1] == ')':
                a = 'o'
                x += a
            elif command[i] == '(' and command[i+1] == 'a' and command[i+2] == 'l' and command[i+3] == ')':
                a = 'al'
                x += a
        return x