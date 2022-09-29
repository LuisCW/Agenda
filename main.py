import datetime
from tkinter import  messagebox
from tkinter import ttk
from tkinter import *
from tkcalendar import Calendar, DateEntry
import tkinter as tk
import time
from datetime import date


lista=[]

class index:

    def __init__(self, window):
        self.wind = window
        self.wind.geometry("300x550")

        self.wind.title('Agenda')
        self.contenido()
        self.reloj()
        self.fecha()

    def reloj(self):
        self.current_time_label = tk.Label(text="", font=('Tahoma', 44), fg='#ffffff', bg='#72a922', pady=10, padx=10)
        self.current_time_label.pack(pady=10)
        self.update_clock()

    def fecha(self):
        self.week_day_label =tk.Label(text="", font=('Tahoma', 12), fg='#ffffff', bg='#FF0000', pady=10, padx=10)
        self.week_day_label.pack(pady=5)
        self.get_date()

    def update_clock(self):
        hora = time.strftime("%H:%M:%S")
        self.current_time_label.configure(text=hora)
        self.wind.after(1000, self.update_clock)

    def get_date(self):
        datetime_object = datetime.datetime.now()
        week_day = datetime_object.strftime("%A")
        today = date.today()
        d = today.strftime("%d / %m / %y ")
        self.week_day_label.configure(text=d + '|' + week_day)

    def contenido(self):
        img = PhotoImage(file="fondo.png")
        label = Label(
            self.wind,
            image=img
        )
        label.place(x=0, y=0)
        Label(self.wind, text="Agenda", font=("Helvetica", 28), foreground=("green")).pack(pady=40)

        def calendar():
            self.wind.destroy()
            obj = calendario(Tk())
            obj.windCalendar.mainloop()
        self.Boton1 = Button(self.wind, text="Calendario", command=calendar, width=20, height=1, font=('Helvetica', 16), bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
        self.Boton1.pack(pady=10)

        def remember():
            self.wind.destroy()
            obj = recordatorio(Tk())
            obj.windRemember.mainloop()
        self.Boton2 = Button(self.wind, text="Recordatorio", command=remember, width=20, height=1, font=('Helvetica', 16), bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
        self.Boton2.pack(pady=10)



class calendario:
    def __init__(self, windowCalendar):
        fechaSeleccionada = StringVar()
        tipoEvento = StringVar()
        nombre = StringVar()
        hora = StringVar()
        minutos = StringVar()
        cumpleaños = StringVar()
        self.windCalendar = windowCalendar
        self.windCalendar.geometry("350x900")
        self.windCalendar.title('Agenda')
        img = PhotoImage(file="fondo.png")
        label = Label(
            self.windCalendar,
            image=img
        )
        label.place(x=0, y=0)
        self.reloj1()
        self.fecha1()

        cal = Calendar(windowCalendar, selectmode='day')
        date = cal.datetime.today() + cal.timedelta(days=2)
        cal.calevent_create(date, 'Hello World', 'message')
        cal.calevent_create(date, 'Reminder 2', 'reminder')
        cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
        cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')

        cal.tag_config('reminder', background='red', foreground='yellow')

        cal.pack(fill="both", expand=True)

        Label(self.windCalendar, text="Fecha Seleccionada", font=("Helvetica", 16), foreground=("red")).pack(pady=5)
        cal = DateEntry(windowCalendar, textvariable=fechaSeleccionada, width=12, background='darkblue',
                        foreground='white', borderwidth=2, selectmode='day')
        cal.pack(padx=10, pady=10)
        Label(self.windCalendar, text="Tipo de Evento", font=("Helvetica", 16), foreground=("red")).pack(pady=5)
        self.tipoEvento = ttk.Combobox(windowCalendar,textvariable=tipoEvento, values=["Recordatorio", "Cumpleaños", "Evento"]).pack(pady=5)
        Label(self.windCalendar, text="Nombre", font=("Helvetica", 16), foreground=("red")).pack(pady=5)
        self.nombreEvento = ttk.Entry(windowCalendar, textvariable=nombre).pack(pady=5)
        Label(self.windCalendar, text="Hora", font=("Helvetica", 16), foreground=("red")).pack(pady=5)
        self.hora = ttk.Combobox(windowCalendar,textvariable=hora, values=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23",]).pack(pady=5)
        self.minutos = ttk.Combobox(windowCalendar,textvariable=minutos, values=["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12",
                                         "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",  "24",  "25",  "26",  "27",  "28",  "29",  "30",  "31",  "32",  "33",  "34",
                                         "35",  "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49",  "50",  "51",  "52",  "53",  "54",  "55",  "56",  "57",  "58",  "59",]).pack(
            pady=5)
        Label(self.windCalendar, text="Cumpleaños de:", font=("Helvetica", 16), foreground=("red")).pack(pady=5)
        self.Cumpleaños = ttk.Entry(windowCalendar, textvariable=cumpleaños).pack(pady=5)
        def agregar():
            fs = fechaSeleccionada.get().strip()
            tp = tipoEvento.get().strip()
            nom = nombre.get().strip()
            h = hora.get().strip()
            m = minutos.get().strip()
            cum = cumpleaños.get().strip()
            lista.append(fs + "$" + tp + "$" + nom + "$" + h + "$" + m + "$" + cum + "$")

            def escribirEvento():
                archivo = open("recordatorio.txt", "w")
                lista.sort()
                for elemento in lista:
                    archivo.write(elemento+ "\n")
                archivo.close()
            if len(fs)&len(tp)&len(nom)&len(h)&len(m):
                messagebox.showwarning('Mensaje', 'Evento guardado correctamente')
                escribirEvento()
            else:
                messagebox.showwarning('¡Alerta!', 'Debe llenar todos los campos')

        Button(self.windCalendar, text="Agregar Recordatorio", command=agregar, width=20, height=1, font=('Helvetica', 16), bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa').pack(pady=5)
        def index0():
            self.windCalendar.destroy()
            obj = index(Tk())
            obj.wind.mainloop()
        Button(self.windCalendar, text="Atrás", command=index0, width=20, height=1, font=('Helvetica', 16), bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa').pack(pady=5)
        date = Label(self.windCalendar, text="")
        date.pack(pady=20)


    def reloj1(self):
        self.current_time_label = tk.Label(text="", font=('Tahoma', 44), fg='#ffffff', bg='#72a922', pady=10, padx=10)
        self.current_time_label.pack(pady=5)
        self.update_clock()

    def update_clock(self):
        hora = time.strftime("%H:%M:%S")
        self.current_time_label.configure(text=hora)
        self.windCalendar.after(1000, self.update_clock)

    def fecha1(self):
        self.week_day_label =tk.Label(text="", font=('Tahoma', 12), fg='#ffffff', bg='#FF0000', pady=10, padx=10)
        self.week_day_label.pack(pady=5)
        self.get_date()

    def get_date(self):
        datetime_object = datetime.datetime.now()
        week_day = datetime_object.strftime("%A")
        today = date.today()
        d = today.strftime("%d / %m / %y ")
        self.week_day_label.configure(text=d + '|' + week_day)

class recordatorio:
    def __init__(self, windowRemember):
        self.windRemember = windowRemember
        self.windRemember.geometry("900x600")
        self.windRemember.title('Agenda')
        self.iniciarArchivo()
        self.cargar()
        self.content()

    def iniciarArchivo(self):
        archivo = open("recordatorio.txt", "a")
        archivo.close()

    def cargar(self):
        archivo = open("recordatorio.txt", "r")
        linea = archivo.readline()
        if linea:
            while linea:
                if linea[-1] == "\n":
                    linea = linea[:-1]
                lista.append(linea)
                linea = archivo.readline()
        archivo.close()

    
    def content(self):
        img = PhotoImage(file="fondo.png")
        label = Label(
            self.windRemember,
            image=img
        )
        label.place(x=0, y=0)
        Label(self.windRemember, text="Lista de Eventos", font=("Helvetica", 16), foreground=("red")).pack(pady=20)
        def consultar():
            r = Text(self.windRemember, width=100, height=18)
            lista.sort()
            valores = []
            r.insert(INSERT, "Fecha\t\tEvento\t\tNombre\t\tHora\t\tMinutos\t\tCumpleaños de:\n")
            for elemento in lista:
                arreglo = elemento.split("$")
                valores.append(arreglo[5])
                r.insert(INSERT, arreglo[0]+"\t\t"+arreglo[1]+"\t\t"+arreglo[2]+"\t\t"+arreglo[3]+"\t\t"+arreglo[4]+"\t\t"
                     +arreglo[5]+"\t\n")
                r.place(x=50, y=80)
                delete = Spinbox(self.windRemember, value=(valores), textvariable=conteliminar)
                delete.place(x=380, y=450)
            if lista == []:
                delete = Spinbox(self.windRemember, value=(valores))
                delete.place(x=380, y=450)
            r.config(state=DISABLED)

        conteliminar = StringVar()
        def escribirEvento():
            archivo = open("recordatorio.txt", "w")
            lista.sort()
            for elemento in lista:
                archivo.write(elemento + "\n")
            archivo.close()
        def eliminar():
            conteliminar.get()
            removido = False
            for elemento in lista:
                arreglo = elemento.split("$")
                if conteliminar.get() == arreglo[2]:
                    lista.remove(elemento)
                    removido = True
            escribirEvento()
            consultar()
            if removido:
                messagebox.showinfo("Eliminar", "Elemento eliminado" + " " + conteliminar.get())

        Label(self.windRemember, text="Escribe el nombre del evento para eliminar", font=("Helvetica", 16), foreground=("red")).place(x=250, y=400)
        delete = Entry(self.windRemember, textvariable=conteliminar)
        delete.place(x=380, y=450)

        btnEliminar = Button(self.windRemember, text="Eliminar", command=eliminar, width=20, height=1, font=('Helvetica', 16), bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
        btnEliminar.place(x=330, y=480)

        def index1():
            self.windRemember.destroy()
            obj = index(Tk())
            obj.wind.mainloop()
        btnAtrás =Button(self.windRemember, text="Atrás", command=index1, width=20, height=1, font=('Helvetica', 16), bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
        btnAtrás.place(x=330, y=530)

        consultar()

obj = index(Tk())
obj.wind.mainloop()
