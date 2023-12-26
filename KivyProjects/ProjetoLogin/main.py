import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import datetime

kivy.require('1.0.9')

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}
        for line in self.file:
            email, password, name, created = line.strip().split(";")
            self.users[email] = (password, name, created)
        self.file.close()

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Email já existe.")
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]

class MyApp(App):
    def build(self):
        self.db = DataBase("users.txt")
        self.username_input = TextInput(hint_text="Nome de usuário")
        self.email_input = TextInput(hint_text="Email")
        self.password_input = TextInput(hint_text="Senha", password=True)
        self.login_button = Button(text="Login", on_press=self.login)
        self.create_button = Button(text="Criar Conta", on_press=self.create_account)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Bem-vindo ao Meu App"))
        layout.add_widget(self.username_input)
        layout.add_widget(self.email_input)
        layout.add_widget(self.password_input)
        layout.add_widget(self.login_button)
        layout.add_widget(self.create_button)
        return layout

    def login(self, instance):
        email = self.email_input.text
        password = self.password_input.text
        if self.db.validate(email, password):
            popup = Popup(title='Login Bem-sucedido',
                          content=Label(text='Login bem-sucedido!'),
                          size_hint=(None, None), size=(400, 200))
            popup.open()
        else:
            popup = Popup(title='Login Falhou',
                          content=Label(text='Login falhou. Verifique suas credenciais.'),
                          size_hint=(None, None), size=(400, 200))
            popup.open()

    def create_account(self, instance):
        username = self.username_input.text
        email = self.email_input.text
        password = self.password_input.text
        result = self.db.add_user(email, password, username)
        if result == 1:
            popup = Popup(title='Conta Criada',
                          content=Label(text='Sua conta foi criada com sucesso!'),
                          size_hint=(None, None), size=(400, 200))
            popup.open()
        else:
            popup = Popup(title='Erro ao Criar Conta',
                          content=Label(text='Não foi possível criar a conta. O email já existe.'),
                          size_hint=(None, None), size=(400, 200))
            popup.open()

if __name__ == '__main__':
    MyApp().run()
