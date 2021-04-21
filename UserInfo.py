class User:
    def __init__(self, fName, lName, username):
        self.fName = fName
        self.lName = lName
        self.username = username

    def getFullName(self):
        return self.fName + " " + self.lName + "\n"
