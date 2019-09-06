from tkinter import *
from functions import *

window = Tk()
 
window.title("Agenda")
 
window.geometry('470x550')
 
lblN = Label(window, text="Nome")
 
lblN.place(x = 1, y = 15)

lblA = Label(window, text="Idade")
 
lblA.place(x = 1, y = 40)

lblC = Label(window, text="Cidade")

lblC.place(x = 1, y = 70)
 
EntradaN = Entry(window,width=10)
 
EntradaN.place(x = 50, y = 15)

EntradaA = Entry(window,width=10)
 
EntradaA.place(x = 50, y = 40)

EntradaC = Entry(window,width=10)

EntradaC.place(x = 50, y = 70)   

def clickedN():
     Contato.delete('1.0', END)
     Contato.config(state="normal")
     Nome = EntradaN.get()
     
     i = 0
     while(i <= 50):
         
         if person[i] == Nome:
            
            Contato.insert(INSERT, "--------------------")
            Contato.insert(INSERT, "\n ")
            Contato.insert(INSERT, "Nome: ")
            Contato.insert(INSERT, person[i])
            Contato.insert(INSERT, "\n ")

            Contato.insert(INSERT, "CPF: ")
            Contato.insert(INSERT, cpf[i])
            Contato.insert(INSERT, "\n ")

            Contato.insert(INSERT, "idade: ")
            Contato.insert(INSERT, age[i])
            Contato.insert(INSERT, "\n ") 

            Contato.insert(INSERT, "Cidade: ")
            Contato.insert(INSERT, city[i])
            Contato.insert(INSERT, "\n ") 

            Contato.insert(INSERT, "Numero Telefone: ")
            Contato.insert(INSERT, tel1[i])
            Contato.insert(INSERT, "-")
            Contato.insert(INSERT, tel2[i])
            Contato.insert(INSERT, "\n ") 

            Contato.insert(INSERT, "Nascimento: ")
            Contato.insert(INSERT, day[i])
            Contato.insert(INSERT, "/")
            Contato.insert(INSERT, month[i])
            Contato.insert(INSERT, "/")
            Contato.insert(INSERT, year[i])
            Contato.insert(INSERT, "\n")
         i += 1                   

    #Contato.insert(INSERT, )

def clickedA():

     Contato.delete('1.0', END)

     Contato.config(state="normal")

     AgeB = int(EntradaA.get())
     
     j = 0
     while(j <= 50):
         
         if age[j] == AgeB:
            Contato.insert(INSERT, "--------------------")
            Contato.insert(INSERT, "\n ")
            Contato.insert(INSERT, "Nome: ")
            Contato.insert(INSERT, person[j])
            Contato.insert(INSERT, "\n ")

            Contato.insert(INSERT, "CPF: ")
            Contato.insert(INSERT, cpf[j])
            Contato.insert(INSERT, "\n ")

            Contato.insert(INSERT, "idade: ")
            Contato.insert(INSERT, age[j])
            Contato.insert(INSERT, "\n ") 

            Contato.insert(INSERT, "Cidade: ")
            Contato.insert(INSERT, city[j])
            Contato.insert(INSERT, "\n ") 

            Contato.insert(INSERT, "Numero Telefone: ")
            Contato.insert(INSERT, tel1[j])
            Contato.insert(INSERT, "-")
            Contato.insert(INSERT, tel2[j])
            Contato.insert(INSERT, "\n ") 

            Contato.insert(INSERT, "Nascimento: ")
            Contato.insert(INSERT, day[j])
            Contato.insert(INSERT, "/")
            Contato.insert(INSERT, month[j])
            Contato.insert(INSERT, "/")
            Contato.insert(INSERT, year[j])
            Contato.insert(INSERT, "\n")
         j += 1

def clickedC():

     Contato.delete('1.0', END)

     Contato.config(state="normal")

     Cidade = EntradaC.get()
     
     j = 0
     while(j <= 50):
         
         if Cidade == city[j]:
            Contato.insert(INSERT, "--------------------")
            Contato.insert(INSERT, "\n ")
            Contato.insert(INSERT, "Nome: ")
            Contato.insert(INSERT, person[j])
            Contato.insert(INSERT, "\n ")

            Contato.insert(INSERT, "CPF: ")
            Contato.insert(INSERT, cpf[j])
            Contato.insert(INSERT, "\n ")

            Contato.insert(INSERT, "idade: ")
            Contato.insert(INSERT, age[j])
            Contato.insert(INSERT, "\n ") 

            Contato.insert(INSERT, "Cidade: ")
            Contato.insert(INSERT, city[j])
            Contato.insert(INSERT, "\n ") 

            Contato.insert(INSERT, "Numero Telefone: ")
            Contato.insert(INSERT, tel1[j])
            Contato.insert(INSERT, "-")
            Contato.insert(INSERT, tel2[j])
            Contato.insert(INSERT, "\n ") 

            Contato.insert(INSERT, "Nascimento: ")
            Contato.insert(INSERT, day[j])
            Contato.insert(INSERT, "/")
            Contato.insert(INSERT, month[j])
            Contato.insert(INSERT, "/")
            Contato.insert(INSERT, year[j])
            Contato.insert(INSERT, "\n")
         j += 1        

def clickedG():

    Contato.delete('1.0', END)

    Contato.config(state="normal")

     
    j = 0
    while(j <= 50):

        Contato.insert(INSERT, "--------------------") 
        Contato.insert(INSERT, "\n ")      
        Contato.insert(INSERT, "Nome: ")
        Contato.insert(INSERT, person[j])
        Contato.insert(INSERT, "\n ")

        Contato.insert(INSERT, "CPF: ")
        Contato.insert(INSERT, cpf[j])
        Contato.insert(INSERT, "\n ")

        Contato.insert(INSERT, "idade: ")
        Contato.insert(INSERT, age[j])
        Contato.insert(INSERT, "\n ") 

        Contato.insert(INSERT, "Cidade: ")
        Contato.insert(INSERT, city[j])
        Contato.insert(INSERT, "\n ") 

        Contato.insert(INSERT, "Numero Telefone: ")
        Contato.insert(INSERT, tel1[j])
        Contato.insert(INSERT, "-")
        Contato.insert(INSERT, tel2[j])
        Contato.insert(INSERT, "\n ") 

        Contato.insert(INSERT, "Nascimento: ")
        Contato.insert(INSERT, day[j])
        Contato.insert(INSERT, "/")
        Contato.insert(INSERT, month[j])
        Contato.insert(INSERT, "/")
        Contato.insert(INSERT, year[j])
        Contato.insert(INSERT, "\n")
        j += 1
 
btnNome = Button(window, text="Buscar", command=clickedN)

btnAge = Button(window, text="Buscar", command=clickedA)

btnGeral = Button(window, text="Listar Todos Contatos", command=clickedG)

btnCity = Button(window, text="Buscar", command=clickedC)

btnAge.place(x = 140, y = 40)
 
btnNome.place(x = 140, y = 10)

btnGeral.place(x = 26, y = 430)

btnCity.place(x = 140, y = 70)

Contato = Text(window, width = 30, height = 30)

Contato.place(x = 220, y = 0)

Contato.config(state="disabled")
 
window.mainloop()