#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Oct 28, 2019 03:17:21 PM EDT  platform: Linux

import sys
import tkMessageBox
import functionAgendar as fcag
import functionComparar as fcco
import functionRenovar as fcre
import time
from datetime import datetime as dt

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import interfaz_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    interfaz_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    interfaz_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("354x389+383+141")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1, 1)
        top.title("Sistema de autenticacion")

        global _images
        _images = (

         tk.PhotoImage("img_close", data='''R0lGODlhDAAMAIQUADIyMjc3Nzk5OT09PT
                 8/P0JCQkVFRU1NTU5OTlFRUVZWVmBgYGF hYWlpaXt7e6CgoLm5ucLCwszMzNbW
                 1v//////////////////////////////////// ///////////yH5BAEKAB8ALA
                 AAAAAMAAwAAAUt4CeOZGmaA5mSyQCIwhCUSwEIxHHW+ fkxBgPiBDwshCWHQfc5
                 KkoNUtRHpYYAADs= '''),

         tk.PhotoImage("img_closeactive", data='''R0lGODlhDAAMAIQcALwuEtIzFL46
                 INY0Fdk2FsQ8IdhAI9pAIttCJNlKLtpLL9pMMMNTP cVTPdpZQOBbQd60rN+1rf
                 Czp+zLxPbMxPLX0vHY0/fY0/rm4vvx8Pvy8fzy8P//////// ///////yH5BAEK
                 AB8ALAAAAAAMAAwAAAVHYLQQZEkukWKuxEgg1EPCcilx24NcHGYWFhx P0zANBE
                 GOhhFYGSocTsax2imDOdNtiez9JszjpEg4EAaA5jlNUEASLFICEgIAOw== '''),

         tk.PhotoImage("img_closepressed", data='''R0lGODlhDAAMAIQeAJ8nD64qELE
                 rELMsEqIyG6cyG7U1HLY2HrY3HrhBKrlCK6pGM7lD LKtHM7pKNL5MNtiViNaon
                 +GqoNSyq9WzrNyyqtuzq+O0que/t+bIwubJw+vJw+vTz+zT z////////yH5BAE
                 KAB8ALAAAAAAMAAwAAAVJIMUMZEkylGKuwzgc0kPCcgl123NcHWYW Fs6Gp2mYB
                 IRgR7MIrAwVDifjWO2WwZzpxkxyfKVCpImMGAeIgQDgVLMHikmCRUpMQgA7 ''')
        )

        self.style.element_create("close", "image", "img_close",
               ("active", "pressed", "!disabled", "img_closepressed"),
               ("active", "alternate", "!disabled",
               "img_closeactive"), border=8, sticky='')

        self.style.layout("ClosetabNotebook", [("ClosetabNotebook.client",
                                     {"sticky": "nswe"})])
        self.style.layout("ClosetabNotebook.Tab", [
            ("ClosetabNotebook.tab",
              { "sticky": "nswe",
                "children": [
                    ("ClosetabNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("ClosetabNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("ClosetabNotebook.label", {"side":
                                      "left", "sticky": ''}),
                                    ("ClosetabNotebook.close", {"side":
                                        "left", "sticky": ''}),]})]})]})])

        PNOTEBOOK = "ClosetabNotebook" 

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.tabs = ttk.Notebook(top)
        self.tabs.place(relx=0.056, rely=0.026, relheight=0.838, relwidth=0.91)
        self.tabs.configure(takefocus="")
        self.tabs.configure(style=PNOTEBOOK)
        self.tabs_t0 = tk.Frame(self.tabs)
        self.tabs.add(self.tabs_t0, padding=3)
        self.tabs.tab(0, text="Agendar",compound="none",underline="-1",)
        self.tabs_t1 = tk.Frame(self.tabs)
        self.tabs.add(self.tabs_t1, padding=3)
        self.tabs.tab(1, text="Renovar",compound="none",underline="-1",)
        self.tabs_t2 = tk.Frame(self.tabs)
        self.tabs.add(self.tabs_t2, padding=3)
        self.tabs.tab(2, text="Consultar datos", compound="none", underline="-1"
                ,)

        self.txnombre = tk.Entry(self.tabs_t0)
        self.txnombre.place(relx=0.375, rely=0.067,height=23, relwidth=0.519)
        self.txnombre.configure(background="white")
        self.txnombre.configure(font="TkFixedFont")

        self.Label1 = tk.Label(self.tabs_t0)
        self.Label1.place(relx=0.031, rely=0.067, height=21, width=56)
        self.Label1.configure(text='''Nombre''')

        self.txapellido = tk.Entry(self.tabs_t0)
        self.txapellido.place(relx=0.375, rely=0.167,height=23, relwidth=0.519)
        self.txapellido.configure(background="white")
        self.txapellido.configure(font="TkFixedFont")

        self.txdoc = tk.Entry(self.tabs_t0)
        self.txdoc.place(relx=0.375, rely=0.267,height=23, relwidth=0.519)
        self.txdoc.configure(background="white")
        self.txdoc.configure(font="TkFixedFont")

        self.txdatosadic = tk.Entry(self.tabs_t0)
        self.txdatosadic.place(relx=0.375, rely=0.567, height=23, relwidth=0.519)

        self.txdatosadic.configure(background="white")
        self.txdatosadic.configure(font="TkFixedFont")

        self.txidsocio = tk.Entry(self.tabs_t0)
        self.txidsocio.place(relx=0.375, rely=0.467,height=23, relwidth=0.519)
        self.txidsocio.configure(background="white")
        self.txidsocio.configure(font="TkFixedFont")

        self.Label2 = tk.Label(self.tabs_t0)
        self.Label2.place(relx=0.031, rely=0.167, height=21, width=57)
        self.Label2.configure(text='''Apellido''')

        self.Label3 = tk.Label(self.tabs_t0)
        self.Label3.place(relx=0.016, rely=0.267, height=21, width=89)
        self.Label3.configure(text='''Documento''')

        self.Label4 = tk.Label(self.tabs_t0)
        self.Label4.place(relx=0.031, rely=0.367, height=21, width=74)
        self.Label4.configure(text='''Fecha nac.''')

        self.Label5 = tk.Label(self.tabs_t0)
        self.Label5.place(relx=0.031, rely=0.467, height=21, width=89)
        self.Label5.configure(text='''Nro. de socio''')

        self.Label6 = tk.Label(self.tabs_t0)
        self.Label6.place(relx=0.031, rely=0.567, height=21, width=77)
        self.Label6.configure(text='''Datos adic.''')

        self.txrenovday = tk.Entry(self.tabs_t0)
        self.txrenovday.place(relx=0.375, rely=0.667,height=23, relwidth=0.113)
        self.txrenovday.configure(background="white")
        self.txrenovday.configure(font="TkFixedFont")

        self.Label7 = tk.Label(self.tabs_t0)
        self.Label7.place(relx=0.031, rely=0.667, height=21, width=88)
        self.Label7.configure(text='''Fecha renov.''')

        self.txrenovmonth = tk.Entry(self.tabs_t0)
        self.txrenovmonth.place(relx=0.563, rely=0.667, height=23
                , relwidth=0.113)
        self.txrenovmonth.configure(background="white")
        self.txrenovmonth.configure(font="TkFixedFont")

        self.txrenovyear = tk.Entry(self.tabs_t0)
        self.txrenovyear.place(relx=0.75, rely=0.667,height=23, relwidth=0.113)
        self.txrenovyear.configure(background="white")
        self.txrenovyear.configure(font="TkFixedFont")

        self.txnacday = tk.Entry(self.tabs_t0)
        self.txnacday.place(relx=0.375, rely=0.367,height=23, relwidth=0.113)
        self.txnacday.configure(background="white")
        self.txnacday.configure(font="TkFixedFont")

        self.txnacmonth = tk.Entry(self.tabs_t0)
        self.txnacmonth.place(relx=0.563, rely=0.367,height=23, relwidth=0.113)
        self.txnacmonth.configure(background="white")
        self.txnacmonth.configure(font="TkFixedFont")

        self.txnacyear = tk.Entry(self.tabs_t0)
        self.txnacyear.place(relx=0.75, rely=0.367,height=23, relwidth=0.113)
        self.txnacyear.configure(background="white")
        self.txnacyear.configure(font="TkFixedFont")

        self.Button1 = tk.Button(self.tabs_t0)
        self.Button1.place(relx=0.594, rely=0.8, height=31, width=1)
        self.Button1.configure(text='''Button''')

#################################################################################
##AGENDADO

	def agendar():
		self.lbagendarstatus.configure(text='''Procesando.''')
		root.update()
		nombre = self.txnombre.get()
		apellido = self.txapellido.get()
		documento = self.txdoc.get()
		fecha_nac = self.txnacday.get() +"/"+ self.txnacmonth.get() +"/"+ self.txnacyear.get()
		nro_socio = self.txidsocio.get()
		datos_adic = self.txdatosadic.get()
		fecha_renov = self.txrenovday.get() +"/"+ self.txrenovmonth.get() +"/"+ self.txrenovyear.get() 
		
		raw_string = nombre +";"+ apellido +";"+ documento +";"+ fecha_nac +";"+ nro_socio +";"+ datos_adic
				

		
		agendado_ok = fcag.agendarUsuario(raw_string, fecha_renov)
		if(agendado_ok == 1 or ";;" in raw_string):
			self.lbagendarstatus.configure(text='''No se pudo agendar.''')
		else:
			self.lbagendarstatus.configure(text='''Agendado.''')

	self.btagendar = tk.Button(self.tabs_t0, command = agendar)
        self.btagendar.place(relx=0.063, rely=0.8, height=21, width=261)
        self.btagendar.configure(text='''Agendar afiliado''')

        self.Label16 = tk.Label(self.tabs_t0)
        self.Label16.place(relx=0.063, rely=0.9, height=21, width=73)
        self.Label16.configure(text='''Resultado:''')
	
        self.lbagendarstatus = tk.Label(self.tabs_t0)
        self.lbagendarstatus.place(relx=0.313, rely=0.9, height=21, width=180)
        self.lbagendarstatus.configure(text='''Preparado.           ''')

	



###################################################################################################
## RENOVACION POR EXTENSION.

	def renovar1():
		self.lba7.configure(text='''Apoye huella y tarjeta.''')
		root.update()
		resultado = fcre.renovar(self.txrenovaciondias.get())
		self.lba7.configure(text='''Procesando.''')
		root.update()
		if (resultado == 0):
			self.lba7.configure(text='''Credencial renovada.''')
		else:
			self.lba7.configure(text='''Hubo un error.''')	






        self.Label12 = tk.Label(self.tabs_t2)
        self.Label12.place(relx=0.063, rely=0.333, height=21, width=52)
        self.Label12.configure(text='''Estado:''')

        self.Label13 = tk.Label(self.tabs_t2)
        self.Label13.place(relx=0.063, rely=0.467, height=21, width=114)
        self.Label13.configure(text='''Datos obtenidos:''')


#########################################################################
## CONSULTAR
	def consultar():
		self.Label15.configure(text='''Apoye tarjeta y huella.''')
		root.update()
		
		self.txdataconseguida.delete('1.0', tk.END) # Borra texto.
		resultado = fcco.autenticar()
		self.Label15.configure(text='''Procesando.''')
		root.update()
		try:
			if("Error:" in resultado):
				self.Label15.configure(text=str(resultado))
			else:
				if (resultado == 1):
					self.Label15.configure(text="Hubo un error.")
				else:
					for i in resultado.split('[')[1].split(']')[0].split(';'):
						self.txdataconseguida.insert(tk.END, i + '\n')
					self.txdataconseguida.insert(tk.END, "FECHA DE RENOVACION: " + resultado.split('[')[2].split(']')[0])
					self.Label15.configure(text='''Listo.''')
		except:
			self.Label15.configure(text="Hubo un error.")
		root.after(5000)
		

#################
        self.btconsultar = tk.Button(self.tabs_t2, command = consultar)
        self.btconsultar.place(relx=0.063, rely=0.2, height=31, width=261)
        self.btconsultar.configure(text='''Consultar datos''')

	self.lbagendarstatus.configure(activebackground="#f9f9f9")
        self.lbagendarstatus.configure(text='''En espera.''')

        self.txrenovaciondias = tk.Entry(self.tabs_t1)
        self.txrenovaciondias.place(relx=0.063, rely=0.667, height=23
                , relwidth=0.3)
        self.txrenovaciondias.configure(background="white")
        self.txrenovaciondias.configure(font="TkFixedFont")
        self.txrenovaciondias.configure(selectbackground="#c4c4c4")

        self.lba3 = tk.Label(self.tabs_t1)
        self.lba3.place(relx=0.063, rely=0.5, height=21, width=278)
        self.lba3.configure(activebackground="#f9f9f9")
        self.lba3.configure(text='''O bien, puede ingresar la cantidad de dias''')

        self.lba5 = tk.Label(self.tabs_t1)
        self.lba5.place(relx=0.375, rely=0.667, height=21, width=35)
        self.lba5.configure(activebackground="#f9f9f9")
        self.lba5.configure(text='''dias.''')

		

        self.txrenovar = tk.Button(self.tabs_t1, command = renovar1)
        self.txrenovar.place(relx=0.063, rely=0.767, height=31, width=261)
        self.txrenovar.configure(activebackground="#f9f9f9")
        self.txrenovar.configure(text='''Extender plazo''')

        self.lba6 = tk.Label(self.tabs_t1)
        self.lba6.place(relx=0.063, rely=0.9, height=21, width=73)
        self.lba6.configure(activebackground="#f9f9f9")
        self.lba6.configure(text='''Resultado:''')

        self.lba7 = tk.Label(self.tabs_t1)
        self.lba7.place(relx=0.344, rely=0.9, height=21, width=175)
        self.lba7.configure(activebackground="#f9f9f9")
        self.lba7.configure(text='''En espera de operaciones.''')

        self.lba4 = tk.Label(self.tabs_t1)
        self.lba4.place(relx=0.063, rely=0.567, height=21, width=177)
        self.lba4.configure(text='''a extender a partir de hoy.''')

        self.tbrendia = tk.Entry(self.tabs_t1)
        self.tbrendia.place(relx=0.438, rely=0.233,height=23, relwidth=0.081)
        self.tbrendia.configure(background="white")
        self.tbrendia.configure(font="TkFixedFont")

        self.tbrenmes = tk.Entry(self.tabs_t1)
        self.tbrenmes.place(relx=0.563, rely=0.233,height=23, relwidth=0.081)
        self.tbrenmes.configure(background="white")
        self.tbrenmes.configure(font="TkFixedFont")

        self.tbrenano = tk.Entry(self.tabs_t1)
        self.tbrenano.place(relx=0.688, rely=0.233,height=23, relwidth=0.113)
        self.tbrenano.configure(background="white")
        self.tbrenano.configure(font="TkFixedFont")

        self.lba0 = tk.Label(self.tabs_t1)
        self.lba0.place(relx=0.063, rely=0.067, height=21, width=262)
        self.lba0.configure(text='''Usted puede ingresar el nuevo plazo de''')

        self.lba1 = tk.Label(self.tabs_t1)
        self.lba1.place(relx=0.063, rely=0.133, height=21, width=79)
        self.lba1.configure(text='''renovado.''')

        self.lba2 = tk.Label(self.tabs_t1)
        self.lba2.place(relx=0.063, rely=0.233, height=21, width=96)
        self.lba2.configure(text='''(dd/mm/aaaa)''')


######################################################################################################
## RENOVAR HASTA FECHA INGRESADA

	def renovar2():
		self.lba7.configure(text='''Procesando.''')
		root.update()
		fecha_cad = dt.strptime(self.tbrendia.get() +"/"+ self.tbrenmes.get() +"/"+ self.tbrenano.get(), "%d/%m/%Y")
		hoy = dt.today()
		diferencia = fecha_cad-hoy
		print("ENTRE " + str(fecha_cad) + " Y HOY " + str(hoy) + " HAY " + str(diferencia.days) + " DIAS")
		resultado = fcre.renovar(diferencia.days)
		if (resultado == 0):
			self.lba7.configure(text='''Credencial renovada.''')
		else:
			self.lba7.configure(text='''Hubo un error.''')
		
		
		


        self.btrenovar2 = tk.Button(self.tabs_t1, command = renovar2)
        self.btrenovar2.place(relx=0.094, rely=0.333, height=31, width=251)
        self.btrenovar2.configure(text='''Extender hasta fecha ingresada''')




        self.Label14 = tk.Label(self.tabs_t2)
        self.Label14.place(relx=0.063, rely=0.067, height=31, width=279)
        self.Label14.configure(text='''Apoye la tarjeta, la huella y continue.''')

        self.Label15 = tk.Label(self.tabs_t2)
        self.Label15.place(relx=0.25, rely=0.333, height=21, width=180)
        self.Label15.configure(text='''Preparado.              ''')

        self.txdataconseguida = tk.Text(self.tabs_t2)
        self.txdataconseguida.place(relx=0.063, rely=0.533, relheight=0.447
                , relwidth=0.894)
        self.txdataconseguida.configure(background="white")
        self.txdataconseguida.configure(font="TkTextFont")
        self.txdataconseguida.configure(selectbackground="#c4c4c4")
        self.txdataconseguida.configure(state='normal')
        self.txdataconseguida.configure(wrap="word")
        self.tabs.bind('<Button-1>',_button_press)
        self.tabs.bind('<ButtonRelease-1>',_button_release)
        self.tabs.bind('<Motion>',_mouse_over)

	def salir():
		exit(1)

        self.btsalir = tk.Button(top, command = salir)
        self.btsalir.place(relx=0.678, rely=0.874, height=31, width=101)
        self.btsalir.configure(text='''Salir''')


#####################################################################################################

# The following code is add to handle mouse events with the close icons
# in PNotebooks widgets.
def _button_press(event):
    widget = event.widget
    element = widget.identify(event.x, event.y)
    if "close" in element:
        index = widget.index("@%d,%d" % (event.x, event.y))
        widget.state(['pressed'])
        widget._active = index

def _button_release(event):
    widget = event.widget
    if not widget.instate(['pressed']):
            return
    element = widget.identify(event.x, event.y)
    try:
        index = widget.index("@%d,%d" % (event.x, event.y))
    except TclError:
        pass
    if "close" in element and widget._active == index:
        widget.forget(index)
        widget.event_generate("<<NotebookTabClosed>>")

    widget.state(['!pressed'])
    widget._active = None

def _mouse_over(event):
    widget = event.widget
    element = widget.identify(event.x, event.y)
    if "close" in element:
        widget.state(['alternate'])
    else:
        widget.state(['!alternate'])

if __name__ == '__main__':
    vp_start_gui()





