

class Login:

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def getUsername(self):
        return self.username


    def getPassword(self):
        return self.password
    

    def __str__(self) -> str:
        return f'{self.username}, {self.password}'
    

    

