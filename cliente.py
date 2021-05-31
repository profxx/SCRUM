from modulos import *
from valida import Validadores
from reports import Relatorios 
from funcionalidades import Funcs

root = tix.Tk()

class App(Funcs, Relatorios, Validadores):
  def__init__(self):
    self.root=root 
    self.images_base64()
    self.validaEntradas ()
    self.tela ()
    self.frames_da_tela()
    self.widgets_frame1() 
    self.lista_frame2()
    self.monta_tabelas()
    self.select_lista() 
    self.Menus ()
    root.mainloop()
  def tela(self):
    self.root.title("Cadastro de Clientes")
    self.root.configure (background = "#1C1C1C")
    self.root.geometry("700x500")
    self.root.state("zoomed") 
    self.root.resizable(True, True)
    self.root.minsize (width = 700, height = 500) 
    self.root.iconbitmap("icocli.ico")
  def frames_da_tela(self):
    self.frame_1 = Frame(
      self.root,
      bd = 4, # Borda
      bg = "#363636", # Cor de fundo (background color) highlightbackground "#836FFF",
      highlightbackground = "#836FFF",
      highlightthickness = 1)
    self.frame_1.place(
      relx = 0.01,
      rely = 0.02,
      relwidth = 0.98,
      relheight = 0.46)
    self.frame_2 Frame(
      self.root,
      bd = 4,
      bg = "#363636",
      highlightbackground = "#836FFF",
      highlightthickness = 1)
    self.frame_2.place(
      relx=0.01,
      rely=0.5,
      relwidth=0.98,
      relheight=0.46)
  def widgets_framel(self):
    # Abas
    self.abas = ttk.Notebook(self.frame_1)
    self.abal = Frame(self.abas)
    self.aba2 = Frame(self.abas)

            bg = "#808080"
            fg = "#363636"
            activebackground = '#A9A9A9',
            activeforeground = '#363636',
            font = ("verdana", "10")
            command = self.insere_cliente
        )
        self.bt_novo.place(relx=0.6, rely = 0.1, relwidth=0.1, relheight=0.1)

        # Botão Alterar 
        self.bt_alterar = Button(self.aba1, text="Alterar", bd = 2, bg = "#808080", fg = "#363636", activebackground = '#A9A9A9', activeforeground = '#363636', font=("verdana", "10"), command = self.altera_cliente)
        self.bt_alterar.place(relx=0.8, rely=0.1, relwidth = 0.1, relheigth=0.1)

        # Botão Apagar
        self.bt_apagar = Button(self.aba1, text="Apagar", bd = 2, bg = "#808080", fg = "#363636", activebackground = '#A9A9A9', activeforeground = '#363636', font=("verdana", "10"), command = self.deleta_cliente)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth = 0.1, relheigth=0.1)

        # Criação da Label e Entrada do código
        self.lb_codigo = Label(self.aba1, text = "Código", bg = "#363636", fg = "#808080", font = ("trebouchet", "10"))
        self.lb_codigo.place(relx = 0.008, rely = 0.02)

        self.codigo_entry = Entry(self.aba1, validate = "Key", validatecommand=self.vcmd2)
        self.codigo_entry.place(relx = 0.008, rely = 0.11, relwidth = 0.07, relheight = 0.08)

        # Criação da Label e Entrada do Nome
        self.lb_nome = Label(self.aba1, text = "Nome", bg = "#363636", fg = "#363636", font = ("trebouchet", "10"))
