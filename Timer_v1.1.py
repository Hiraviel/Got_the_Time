import datetime
import re
import threading
from tkinter import Tk, Label, Button, Frame

stage1 = 0
stage2 = 0
proceso = 0
flag_1 = False


def prueba():

    global stage2

    print("Estamos en el Thread " + str(stage2))

    while True:

        valor = input("Valor")

        if valor == "1":
            print("OK")
        else:
            print("Salimos del Thread")
            stage2 = 1
            print(stage2)
            break


def cronometro():
    global proceso
    global stage2

    t1 = threading.Thread(target= prueba)
    t1.start()

    def iniciar(h=00, m=00, s=00):

        global flag_1

        if s >= 60:  # 60
            s = 00
            m = m + 1
            if m >= 60:
                m = 00
                h = h + 1
                if h >= 24:
                    h = 00

        if flag_1 == False:

            if m < 27:  # 27
                time["bg"] = "green"
                estatus['text'] = "OK"
                estatus['bg'] = "green"

            elif m >= 27 and m < 52:
                time["bg"] = "yellow"
                estatus['text'] = "OK"
                estatus['bg'] = "yellow"

            elif m >= 52 and h >= 0:
                flag_1 = True

        if flag_1 == True:
            time["bg"] = "red"
            estatus['text'] = "NOK"
            estatus['bg'] = "red"
            flag_1 = True

        if stage2 == 1:
            close_window()

        time['text'] = str(h) + ":" + str(m) + ":" + str(s)

        proceso = time.after(1000, iniciar, (h), (m), (s + 1))


    def close_window():
        root.destroy()

    root = Tk()
    root.title('Cronometro')
    root.geometry("300x250+1000+100")
    root.protocol("WM_DELETE_WINDOW", close_window)

    time = Label(root, fg='black', width=20, font=("Arial", "80"))
    time.pack()

    estatus = Label(root, fg='black', width=20, font=("Arial", "80"))
    estatus.pack()

    iniciar()

    frame = Frame(root)
    frame.pack()

    root.mainloop()


def captura():
    global stage1
    global stage2
    global flag_1

    flag_1 = False
    stage2 = 0

    while stage1 <= 0:

        VIN = input("Put VIN: ")
        pkykVIN = bool(re.match("^[A-Z0-9]*$", VIN))

        if len(VIN) != 4:  # CAMBIAR A 17
            print("Error with the lenght ({}) of the VIN.".format(len(VIN)))

        else:

            if pkykVIN != False:
                print("\n")

                MODEL = input("Put MODEL: ")

                if len(MODEL) != 6:
                    print(len(MODEL))
                    print("\n")
                    print("Error with the lenght ({}) of the MODEL.".format(len(MODEL)))

                else:
                    stage1 = 1

    if stage1 == 1:

        fecha = datetime.datetime.today().strftime("%Y-%d-%m")

        start = datetime.datetime.now()
        inicio = str(start)

        # Cronometro aquí
        try:
            cronometro()

        except:
            pass

        stage1 = 0

        end = datetime.datetime.now()
        fin = str(end)

        duration = end - start
        tt = str(duration)
        print(duration)

    if tt != "00:54:00":
        estatus = "OK"
        print("OK")
    else:
        estatus = "NOK"
        print("NOK")

    datos = (str(fecha), str(VIN), str(MODEL), str(inicio[11:19]), str(fin[11:19]), str(tt[0:7]), str(estatus))
    print("Creating file..." + "\n")
    file = open(VIN + "_" + fecha + "_" +  str(inicio[11:19].replace(":", "")) + ".txt", "w+") #w+

    for i in range(len(datos)):
        file.write(datos[i] + ", ")
    file.close()

    print("Done..." + "\n")

    rfile = open(VIN + "_" + fecha + "_" + str(inicio[11:19].replace(":", "")) + ".txt", "r")
    if rfile.mode == "r":
        contents = rfile.read()
        print(contents)
    rfile.close()


if __name__ == "__main__":
    while True:
        captura()


