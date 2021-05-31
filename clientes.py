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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        filemenu2.add_command(label="Ficha do Cliente", command=self.geraRelatCliente) 
    def validaEntradas(self): 
        self.vcmd2 = (self.root.register(self.validate_entry2), "%P")

# Programa Principal
App()
