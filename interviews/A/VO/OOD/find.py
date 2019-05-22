class Command:

    def __init__(self, cmd):

        self.cmd = cmd 
        
        self.tokens = cmd.split()

class FindCommand(Command):

    def __init__(self, cmd):

        Command.__init__(self, cmd)

        self.cmdName = "find"
        self.directory = None 
        self.expression = None 
        self.name = None 

        for i in range(len(self.tokens)):

            if i == 0:
                continue 

            elif i == 1:
                self.directory = self.parseDirectory(self.tokens[1])

            elif i == 2:
                self.expression = self.tokens[2]

            else:
                self.name = self.tokens[3]

    def parseDirectory(self, directory):

        if directory == ".":
            return "/usr/xuqitao/git" 

        elif directory == "~":
            return "/usr/xuqitao" 

        else:
            return directory 






