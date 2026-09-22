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

# Dividindo a Janela em duas partes: tela e corpo

tela = Frame(janela, width=235, height=50, bg=cor1)
tela.grid(row=0, column=0)

corpo = Frame(janela, width=235, height=260, bg=cor5)
corpo.grid(row=1, column=0)

# Criando os botões da calculadora

b_1 = Button(corpo, text="C", width=11, height=2, bg=cor2, fg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_1.place(x=-1, y=0)
b_2 = Button(corpo, text="/", width=5, height=2, bg=cor2, fg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=119, y=0)
b_3 = Button(corpo, text="*", width=5, height=2, bg=cor2, fg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=179, y=0)
b_4 = Button(corpo, text="7", width=5, height=2, bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_4.place(x=-1, y=52)
b_5 = Button(corpo, text="8", width=5, height=2, bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(corpo, text="9", width=5, height=2, bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x=119, y=52)
b_7 = Button(corpo, text="-", width=5, height=2, bg=cor2, fg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_7.place(x=179, y=52)
b_8 = Button(corpo, text="4", width=5, height=2, bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x=-1, y=104)
b_9 = Button(corpo, text="5", width=5, height=2, bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(corpo, text="6", width=5, height=2, bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_10.place(x=119, y=104)
b_11 = Button(corpo, text="+", width=5, height=2, bg=cor2, fg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_11.place(x=179, y=104)
b_12 = Button(corpo, text="1", width=5, height=2, bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_12.place(x=-1, y=156)
b_13 = Button(corpo, text="2", width=5, height=2, bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(corpo, text="3", width=5, height=2, bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_14.place(x=119, y=156)
b_15 = Button(corpo, text="=", width=5, height=5, bg=cor4, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_15.place(x=179, y=156)
b_16 = Button(corpo, text="0", width=11, height=2, bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_16.place(x=-1, y=208)
b_17 = Button(corpo, text=",", width=5, height=2, bg=cor3, fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_17.place(x=119, y=208)

janela.mainloop()