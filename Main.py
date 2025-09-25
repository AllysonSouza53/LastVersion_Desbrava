from kivy.lang import Builder
from kivymd.app import MDApp
from Controllers.LoginController import LoginController
from kivymd.uix.menu import MDDropdownMenu
from Banco import Banco

class MyApp(MDApp):
    def build(self):
        return Builder.load_file("Views/Front.kv")
    #quando iniciar
    def on_start(self):
        if self.root:
            print("ScreenManager inicializado com sucesso!")
    #tela escolha
    def irLoginAluno(self):
        if self.root:
            self.root.current = "LoginAluno"

    def irEscolha(self):
        if self.root:
            self.root.current = "Escolha"

    def irLoginProfissional(self):
        if self.root:
            self.root.current = "LoginProfissional"

    #tela LoginProfissional
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

    #tela CadastroProfissional1
    def ListaProfissõesText_Click(self, item, ativa):
        if ativa:
            menu_items = self.AddItensProfissoes(Banco.consultar('NOME','PROFISSOES','1'))
            MDDropdownMenu(caller=item, items=menu_items).open()
        else:
            print('erro')


    def ListaProfissõesBotao_Click(self, item):
        try:
            menu_items = self.AddItensProfissoes(Banco.consultar('NOME','PROFISSOES','1'))
            MDDropdownMenu(caller=item, items=menu_items).open()
        except Exception as e:
            print(e)

    def ListaProfissoesItens_Click(self, text_item):
        self.root.get_screen("CadastroProfissional1").ids.List_ProfissoesText.text = text_item

    def AddItensProfissoes(self, itens):
        menu_items = [
            {
                "text": f"{item[0].translate(str.maketrans("", "", "(),'"))}",
                "on_release": lambda x=f"{item[0].translate(str.maketrans("", "", "(),'"))}": self.ListaProfissoesItens_Click(x),
            } for item in itens
        ]
        return menu_items

    def irCadastroProfissional2(self):
        if self.root:
            self.root.current = "CadastroProfissional2"

    #tela CadastroProfissionais2
    def ListaUFText_Click(self,item, ativa):
        if ativa:
            itens = [
                'Acre',
                'Alagoas',
                'Amapá',
                'Amazonas',
                'Bahia',
                'Ceará',
                'Distrito Federal',
                'Espirito Santo',
                'Goiás',
                'Maranhão',
                'Mato Grosso do Sul',
                'Mato Grosso',
                'Minas Gerais',
                'Pará',
                'Paraíba',
                'Paraná',
                'Pernambuco',
                'Piauí',
                'Rio de Janeiro',
                'Rio Grande do Norte',
                'Rio Grande do Sul',
                'Rondônia',
                'Roraima',
                'Santa Catarina',
                'São Paulo',
                'Sergipe',
                'Tocantins'
            ]
            menu_items = [
                {
                "text":f'{index}',
                "on_release": lambda x=f'{index}': self.ListUFItens_Click(x)
                }for index in itens
            ]

            MDDropdownMenu(caller=item, items=menu_items).open()
        else:
            print('erro')

    def ListaUFBotao_Click(self, item):
        try:
            itens = [
                'Acre',
                'Alagoas',
                'Amapá',
                'Amazonas',
                'Bahia',
                'Ceará',
                'Distrito Federal',
                'Espirito Santo',
                'Goiás',
                'Maranhão',
                'Mato Grosso do Sul',
                'Mato Grosso',
                'Minas Gerais',
                'Pará',
                'Paraíba',
                'Paraná',
                'Pernambuco',
                'Piauí',
                'Rio de Janeiro',
                'Rio Grande do Norte',
                'Rio Grande do Sul',
                'Rondônia',
                'Roraima',
                'Santa Catarina',
                'São Paulo',
                'Sergipe',
                'Tocantins'
            ]
            menu_items = [
                {
                    "text": f'{item[index]}',
                    "on_release": lambda x=f'{item[index]}': self.ListaUFText_Click(x)
                } for index in itens
            ]

            MDDropdownMenu(caller=item, items=menu_items).open()
        except Exception as e:
            print(e)

    def ListUFItens_Click(self, text_item):
        self.root.get_screen("CadastroProfissional2").ids.List_UFText.text = text_item

MyApp().run()