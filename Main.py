from kivy.lang import Builder
from kivymd.app import MDApp
from Controllers.LoginController import LoginController

class MyApp(MDApp):
    def build(self):
        return Builder.load_file("Views/Front.kv")

    def on_start(self):
        if self.root:
            print("ScreenManager inicializado com sucesso!")

    def irLoginAluno(self):
        if self.root:
            self.root.current = "LoginAluno"

    def irEscolha(self):
        if self.root:
            self.root.current = "Escolha"

    def irLoginProfissional(self):
        if self.root:
            self.root.current = "LoginProfissional"

    def irCadastroProfissional1(self):
        if self.root:
            self.root.current = "CadastroProfissional1"

    def LoginProfissionais_Click(self):
        if self.root:
            self.controle = LoginController(self.root)
            if self.controle.Sessao():
                self.root.current = "PerfilProfissional"
        else:
            print("root ainda não existe")

MyApp().run()