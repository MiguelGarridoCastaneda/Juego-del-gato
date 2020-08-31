import tkinter as tk
from tkinter import ttk

partida = {'jX':[], 'jO':[], 'registro':[], 'turno':1, 'ganador':""}

botones = []
       


root = tk.Tk()
root.geometry("500x600+300+100")
root.title("Juego del gato")
label = tk.Label(root, text="Turno de jugador X", font=('Helvetica', 24, 'bold'))
label.place(height=50, width=400, x=50, y=500)

def tablero():

    boton1 = tk.Button(root, command=lambda: marcar(1), font=('Helvetica', 50, 'bold'))
    boton1.place(width=150, height=150, x=25, y=25)
    botones.append(boton1)

    boton2 = tk.Button(root, command=lambda: marcar(2), font=('Helvetica', 50, 'bold'))
    boton2.place( width=150, height=150, x=175, y=25)
    botones.append(boton2)

    boton3 = tk.Button(root, command=lambda: marcar(3), font=('Helvetica', 50, 'bold'))
    boton3.place( width=150, height=150, x=325, y=25)
    botones.append(boton3)

    boton4 = tk.Button(root, command=lambda: marcar(4), font=('Helvetica', 50, 'bold'))
    boton4.place(width=150, height=150, x=25, y=175)
    botones.append(boton4)

    boton5 = tk.Button(root, command=lambda: marcar(5), font=('Helvetica', 50, 'bold'))
    boton5.place( width=150, height=150, x=175, y=175)
    botones.append(boton5)

    boton6 = tk.Button(root, command=lambda: marcar(6), font=('Helvetica', 50, 'bold'))
    boton6.place( width=150, height=150, x=325, y=175)
    botones.append(boton6)

    boton7 = tk.Button(root, command=lambda: marcar(7), font=('Helvetica', 50, 'bold'))
    boton7.place(width=150, height=150, x=25, y=325)
    botones.append(boton7)

    boton8 = tk.Button(root, command=lambda: marcar(8), font=('Helvetica', 50, 'bold'))
    boton8.place( width=150, height=150, x=175, y=325)
    botones.append(boton8)

    boton9 = tk.Button(root, command=lambda: marcar(9), font=('Helvetica', 50, 'bold'))
    boton9.place( width=150, height=150, x=325, y=325)
    botones.append(boton9)
    
def marcar(numero):
    global partida
    if (partida['turno'] % 2 !=0):
        botones[numero - 1].config(text='X')
        label.config(text='Turno de jugador O')
        botones[numero - 1].config(state='disable')
        partida['jX'].append(numero)
    else:
        botones[numero - 1].config(text='O')
        label.config(text='Turno de jugador X')
        botones[numero - 1].config(state='disable')
        partida['jO'].append(numero)
    victoria()
    partida['turno'] +=1
    
def victoria():
    global partida
    print(partida['turno'])
    if(partida['turno']>=4 and partida['turno']<=8):
        if (partida['turno'] % 2 != 0):
            if((1 in partida['jX'] and 2 in partida['jX'] and 3 in partida['jX']) or (4 in partida['jX'] and 5 in partida['jX'] and 6 in partida['jX'])
                or (7 in partida['jX'] and 8 in partida['jX'] and 9 in partida['jX']) or (1 in partida['jX'] and 4 in partida['jX'] and 7 in partida['jX'])
                or (2 in partida['jX'] and 5 in partida['jX'] and 8 in partida['jX']) or (3 in partida['jX'] and 6 in partida['jX'] and 9 in partida['jX'])
                or (1 in partida['jX'] and 5 in partida['jX'] and 9 in partida['jX']) or (3 in partida['jX'] and 5 in partida['jX'] and 7 in partida['jX'])):
                label.config(text="El ganador es el jugador X")
                for boton in botones:
                    boton.config(state='disable')          
        else:
            if((1 in partida['jO'] and 2 in partida['jO'] and 3 in partida['jO']) or (4 in partida['jO'] and 5 in partida['jO'] and 6 in partida['jO'])
                or (7 in partida['jO'] and 8 in partida['jO'] and 9 in partida['jO']) or (1 in partida['jO'] and 4 in partida['jO'] and 7 in partida['jO'])
                or (2 in partida['jO'] and 5 in partida['jO'] and 8 in partida['jO']) or (3 in partida['jO'] and 6 in partida['jO'] and 9 in partida['jO'])
                or (1 in partida['jO'] and 5 in partida['jO'] and 9 in partida['jO']) or (3 in partida['jO'] and 5 in partida['jO'] and 7 in partida['jO'])):
                label.config(text="El ganador es el jugador O")
                for boton in botones:
                    boton.config(state='disable')
    elif(partida['turno'] == 9): 
        label.config(text="Empate")
        for boton in botones:
            boton.config(state='disable')
        
        
tablero()
root.mainloop()

