class User:
    """一个表示用户的简单类"""
    def __init__(self, first_name, last_name, username, email, location):
        """初始化用户"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0
       
    def describe_user(self):
        """显示用户信息摘要"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f" Username: {self.username}")
        print(f" Email: {self.email}")
        print(f" Location: {self.location}")
    
    def greet_user(self):
        """向用户发出个性化问候"""
        print(f"\nWelcome back, {self.username}!")
    
    def increment_login_attempts(self):
        """将属性 login_attempts 的值加 1"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """将 login_attempts 重置为 0"""
        self.login_attempts = 0

class Privileges:
    """一次模拟管理员的简单尝试"""
    
    def __init__(self,privileges):
        self.privileges = privileges
   
    def show_privileges(self):
        print("\nAdministrator's permissions:")
        for privilege in self.privileges:
            print(privilege)       

class Admin(User):
    """一次模拟管理员的简单尝试"""
    
    def __init__(self,first_name, last_name, username, email, location):
        """初始化属性"""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges([])

eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.privileges.privileges = ["can add post","can ban user","can delete post"]
eric.describe_user()
eric.privileges.show_privileges()