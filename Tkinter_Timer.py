from tkinter import Tk, Label, Button, Frame

proceso = 0
flag_1 = False


def iniciar(h=00, m=00, s=00):
    global proceso
    global flag_1

    # Verificamos si los segundos y los minutos son mayores a 60
    # Verificamos si las horas son mayores a 24
    if s >= 60: #60
        s = 00
        m = m + 1
        if m >= 60:
            m = 00
            h = h + 1
            if h >= 24:
                h = 00

    # etiqueta que muestra el cronometro en pantalla
    if flag_1 == False:

        if m < 27: #27
            time["bg"] = "green"
            estatus['text'] = "OK"
            estatus['bg'] = "green"

        if m >= 27 and m < 54:
            time["bg"] = "yellow"
            estatus['text'] = "OK"
            estatus['bg'] = "yellow"

        if m >= 54:
            time["bg"] = "red"
            estatus['text'] = "NOK"
            estatus['bg'] = "red"
            flag_1 = True

    else:
        time["bg"] = "red"
        estatus['text'] = "NOK"
        estatus['bg'] = "red"

    time['text'] = str(h) + ":" + str(m) + ":" + str(s)

    # iniciamos la cuenta progresiva de los segundos
    proceso = time.after(1000, iniciar, (h), (m), (s + 1))


def parar():
    global proceso
    time.after_cancel(proceso)


root = Tk()
root.title('Cronometro')
root.geometry("300x250+1000+100")

time = Label(root, fg='black', width=20, font=("Arial", "80"))
time.pack()

estatus = Label(root, fg='black', width=20, font=("Arial", "80"))
estatus.pack()

# si queremos que se autoejecuta al iniciar el programa hay que desomentar
# esta linea y comentar los botones
iniciar()

# Generamos un frame para poner los botones de iniciar y parar
frame = Frame(root)
#btnIniciar = Button(frame, fg='blue', text='Iniciar', command=iniciar)
#btnIniciar.grid(row=1, column=1)
#btnParar = Button(frame, fg='blue', text='Parar', command=parar)
#btnParar.grid(row=1, column=2)
frame.pack()

if __name__ == "__main__":
    root.mainloop()


