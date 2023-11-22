from tkinter import *



janela = Tk()

janela.geometry('500x500')

janela.config(bg='#add8e6')

boas_vindas = Label(text='Arquivo para calcular a nota da faculdade: ' , font='Montserrat' , bg='#add8e6')
boas_vindas.pack()

txt_nota1 = Label(text='Nota da AV1: ' , font='Montserrat' , bg='#add8e6')
txt_nota1.place(x=0 , y=50)

nota1 = Entry(janela , width=30)
nota1.place(x=110 , y=51)

txt_nota2 = Label(text='Nota da AV2: ' , font='Montserrat' , bg='#add8e6')
txt_nota2.place(x=0 , y=105)

nota2 = Entry(janela , width=30)
nota2.place(x=110 , y=106)


txt_nota3 = Label(text='Nota da AV3: ' , font='Montserrat' , bg='#add8e6')
txt_nota3.place(x=0 , y=156)

nota3 = Entry(janela , width=30)
nota3.place(x=110 , y=157)


txt_nota4 = Label(text='Nota do EDAG: ' , font='Montserrat' , bg='#add8e6')
txt_nota4.place(x=0 , y=206)

nota4 = Entry(janela , width=30)
nota4.place(x=125 , y=207)

resultado_txt = Label(text='Nota: ',  font='Montserrat' , bg='#add8e6')
resultado_txt.place(x=0 , y=250)
resultado = Entry(janela , width=30)
resultado.place(x=50 , y=251)


def calcula_nota_final():
    
    resultado.delete(0 , 'end')

    n1 = float(nota1.get().replace(',' , '.'))

    n2 = float(nota2.get().replace(',' , '.'))

    n3 = float(nota3.get().replace(',' , '.'))

    n4 = float(nota4.get().replace(',' , '.'))

    nf = (n1 * 0.25) + (n2 * 0.25) + (n3 * 0.3) + (n4 * 0.2)
    nf = f'{nf:,.1f}'


    resultado.insert(0 , nf)


    
    


def calcula_nota_av3():

    resultado.delete(0 , 'end')
    
    n1 = float(nota1.get().replace(',' , '.'))
    
    n2 = float(nota2.get().replace(',' , '.'))

    n4 = float(nota4.get().replace(',' , '.'))

    n_av3 = (((n1 * 0.25) + (n2 * 0.25) + (n4 * 0.2)) - 7) / 0.3
    n_av3 = -1 * n_av3
    n_av3 = f'{n_av3:,.1f}'
    resultado.insert(0 , n_av3)
    

    


botao_nota_final = Button(janela , text='Calcular nota Final' , bd=5 , command=calcula_nota_final)

botao_nota_final.place(x=85 , y=300)

botao_nota_AV3 = Button(janela , text='Calcular nota da AV3' , bd=5 , command=calcula_nota_av3)
botao_nota_AV3.place(x=220 , y=300)

janela.mainloop()
