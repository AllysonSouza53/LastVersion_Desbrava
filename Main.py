from kivy.lang import Builder
from kivymd.app import MDApp
from Controllers.LoginController import LoginController
from kivymd.uix.menu import MDDropdownMenu
from Banco import Banco

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

    def ListaProfissõesText_Click(self, item, ativa):
        if ativa:
            menu_items = self.AddItens(Banco.consultar('NOME','PROFISSOES','1'))
            MDDropdownMenu(caller=item, items=menu_items).open()
        else:
            print('erro')


    def ListaProfissõesBotao_Click(self, item):
        try:
            menu_items = self.AddItens(Banco.consultar('NOME','PROFISSOES','1'))
            MDDropdownMenu(caller=item, items=menu_items).open()
        except Exception as e:
            print(e)

    def ListaProfissoesItens_Click(self, text_item):
        self.root.get_screen("CadastroProfissional1").ids.List_ProfissoesText.text = text_item

    def AddItens(self, itens):
        menu_items = [
            {
                "text": f"{item[0].translate(str.maketrans("", "", "(),'"))}",
                "on_release": lambda x=f"{item[0].translate(str.maketrans("", "", "(),'"))}": self.ListaProfissoesItens_Click(x),
            } for item in itens
        ]
        return menu_items


MyApp().run()