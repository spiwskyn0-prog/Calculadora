from tkinter import *

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
janela.resizable(False, False)

# Dividindo a Janela em duas partes: tela e corpo

tela = Frame(janela, width=235, height=50, bg=cor5)
tela.grid(row=0, column=0)
tela.grid_propagate(False)

corpo = Frame(janela, width=235, height=260, bg=cor5)
corpo.grid(row=1, column=0)
corpo.grid_propagate(False)

# Configurando o grid do corpo: 4 colunas, 5 linhas, todas expansíveis igualmente

for c in range(4):
    corpo.grid_columnconfigure(c, weight=1, uniform="col")
for r in range(5):
    corpo.grid_rowconfigure(r, weight=1, uniform="row")

# Criando a tela da calculadora

tela_display = Label(tela, text="123456789", padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 18"), bg=cor1, fg=cor5)
tela_display.place(x=0, y=0, width=235, height=50)

# Criando os botões da calculadora

b_1 = Button(corpo, text="C", bg=cor2, fg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_1.grid(row=0, column=0, columnspan=2, sticky="nsew")

b_2 = Button(corpo, text="/", bg=cor2, fg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_2.grid(row=0, column=2, sticky="nsew")

b_3 = Button(corpo, text="*", bg=cor2, fg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_3.grid(row=0, column=3, sticky="nsew")

b_4 = Button(corpo, text="7", bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_4.grid(row=1, column=0, sticky="nsew")

b_5 = Button(corpo, text="8", bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_5.grid(row=1, column=1, sticky="nsew")

b_6 = Button(corpo, text="9", bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_6.grid(row=1, column=2, sticky="nsew")

b_7 = Button(corpo, text="-", bg=cor2, fg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_7.grid(row=1, column=3, sticky="nsew")

b_8 = Button(corpo, text="4", bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_8.grid(row=2, column=0, sticky="nsew")

b_9 = Button(corpo, text="5", bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_9.grid(row=2, column=1, sticky="nsew")

b_10 = Button(corpo, text="6", bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_10.grid(row=2, column=2, sticky="nsew")

b_11 = Button(corpo, text="+", bg=cor2, fg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_11.grid(row=2, column=3, sticky="nsew")

b_12 = Button(corpo, text="1", bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_12.grid(row=3, column=0, sticky="nsew")

b_13 = Button(corpo, text="2", bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_13.grid(row=3, column=1, sticky="nsew")

b_14 = Button(corpo, text="3", bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_14.grid(row=3, column=2, sticky="nsew")

b_15 = Button(corpo, text="=", bg=cor4, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_15.grid(row=3, column=3, rowspan=2, sticky="nsew")

b_16 = Button(corpo, text="%", bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_16.grid(row=4, column=0, sticky="nsew")

b_17 = Button(corpo, text="0", bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_17.grid(row=4, column=1, sticky="nsew")

b_18 = Button(corpo, text=".", bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_18.grid(row=4, column=2, sticky="nsew")

janela.mainloop()