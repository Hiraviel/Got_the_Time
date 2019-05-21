import datetime
import re
from tkinter import Tk, Label, Button, Frame

stage1 = 0
proceso = 0
flag_1 = False


def cronometro():

    global proceso

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

            if m < 5:  # 27
                time["bg"] = "green"
                estatus['text'] = "OK"
                estatus['bg'] = "green"

            elif m >= 5 and m < 10 :
                time["bg"] = "yellow"
                estatus['text'] = "OK"
                estatus['bg'] = "yellow"

            elif m>=10 and h >= 0:
                flag_1 = True

        if flag_1 == True:
            time["bg"] = "red"
            estatus['text'] = "NOK"
            estatus['bg'] = "red"
            flag_1 = True

        time['text'] = str(h) + ":" + str(m) + ":" + str(s)

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
    iniciar()
    frame = Frame(root)
    frame.pack()
    root.mainloop()


def captura():

    global stage1
    global flag_1

    flag_1 = False

    while stage1 <= 0:

        #print(stage1)
        #print(flag_1)

        VIN = input("Put VIN: ")
        pkykVIN = bool(re.match("^[A-Z0-9]*$", VIN)) #OK
        #print(pkykVIN)

        if len(VIN) != 4: # CAMBIAR A 17
            print("Error with the lenght ({}) of the VIN.".format(len(VIN)))

        else:

            if pkykVIN != False:
                #print(stage1)   #OK
                print("\n")

                MODEL = input("Put MODEL: ")
                    
                if len(MODEL) != 6:
                    print(len(MODEL))
                    #print(stage1)
                    print("\n")
                    print("Error with the lenght ({}) of the MODEL.".format(len(MODEL)))

                else:
                    stage1 = 1
                    #break

    #print(stage1)

    if stage1 == 1:

        fecha = datetime.datetime.today().strftime("%Y-%d-%m")

        start = datetime.datetime.now()
        inicio = str(start)

        #Cronometro aquí
        cronometro()
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


    datos = (str(fecha),str(VIN), str(MODEL), str(inicio[11:19]), str(fin[11:19]), str(tt[0:7]), str(estatus))
    print("Creating file..."+"\n")
    file = open(VIN + "_" + fecha + ".txt", "w+")

    for i in range(len(datos)):
        file.write(datos[i]+", ")
    file.close()

    print("Done..."+"\n")

    rfile = open(VIN + "_" + fecha + ".txt", "r")
    if rfile.mode == "r":
        contents = rfile.read()
        print(contents)


    #print(stage1)
    #print(flag_1)


if __name__ == "__main__":
    while True:
        captura()
    

