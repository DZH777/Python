class User():

    def __init__(self, login, passwd):
        self.login = login
        self.passwd = passwd
        self.privs = ['entrance', 'exit', 'read']

    def get_user_info(self):
        info = str(self.login) + ' ' + str(self.passwd)
        return info

    def get_user_privs(self):
        priv_list = ''
        for priv in self.privs:
            priv_list += priv + ', '
        return priv_list

class Admin(User):

    def __init__(self, login, passwd):
        super().__init__(login, passwd)
        self.privs.append('write')

user1 = User('tesla', '11111')
print(user1.get_user_info())
print(user1.get_user_privs()[:-2])

user2 = Admin('model', '22222')
print(user2.get_user_info())
print(user2.get_user_privs()[:-2])
