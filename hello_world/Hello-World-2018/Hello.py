

#AUTHOR: Ariel Roque
#LANGUAGE: Python
#GITHUB: https://github.com/arielroque

from tkinter import*

gui = Tk()

gui.geometry("320x420")

texto = Label(gui,text="Olá meu nome é Ariel!")

texto.place(x=90,y=100)

texto1 = Label(gui,text="I love Python!")

texto1.place(x=120,y=120)

gui.mainloop()
