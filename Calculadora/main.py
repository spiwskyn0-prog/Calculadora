from tkinter import *
from tkinter import ttk

# Definindo quais cores serão usadas

cor1 = "#beef9e"  # Light Green
cor2 = "#a6c36f"  # Muted Olive
cor3 = "#828c51"  # Palm Leaf
cor4 = "#335145"  # Pine Teal
cor5 = "#1e352f"  # Evergreen

# Criando a janela principal

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")

# Dividindo a Janela em duas partes: tela e botões

tela = Frame(janela, width=235, height=50, bg=cor1)
tela.grid(row=0, column=0)

corpo = Frame(janela, width=235, height=260, bg=cor5)
corpo.grid(row=1, column=0)


janela.mainloop()