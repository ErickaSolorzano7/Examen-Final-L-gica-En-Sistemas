from tkinter import ttk
from tkinter import *

# ("I Logica en Sistemas")
# ("II Primer Semestre")
# ("III Ericka Eunice Solorzano Retana")
# ("IV 09-07-19-14628")
class Desk:
    def __init__(self, window):
        
        anchura = 800   
        altura = 500
          
        self.wind = window

        #le asignamos el ancho y el alto a la ventana 
        self.wind.geometry(str(anchura)+'x'+str(altura))

        #centramos el contenido 
        self.wind.columnconfigure(0, weight=1)
        
        #le damos un titulo a la ventana DEL PROGRAMA
        self.wind.title('Examen Final Logica En Sistemas')
        
        frame = LabelFrame(self.wind, text = 'Variables')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        
        Label(frame, text = 'Primer Numero: ').grid(row = 1, column = 0)
        
        #creamos un input donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 1)
        
        # igual que arriba una etiqueta y un campo input para ingresar valores
        Label(frame, text = 'Segundo Numero: ').grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, column = 1)
        

        Label(frame, text = 'Tercer Numero: ').grid(row = 3, column = 0)
        self.var3 = Entry(frame)
        self.var3.grid(row = 3, column = 1)
        

        #Creamos un boton para ejecutar las operaciones       
        Button (frame, text = 'Ejecutar', command = self.bottonA).grid(row = 6, columnspan = 5, sticky = W + E)
        Button (frame, text = 'Imprimir', command = self.bottonB).grid(row = 7, columnspan = 5, sticky = W + E)
     
        #designamos un área para mensajes
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

    
    def bottonA(self):
        a=float(self.var1.get())
        b=float(self.var2.get())
        c=float(self.var3.get())
        if (a<c):
            self.message['text'] = 'La Operacion Es y A es Menor : {}'.format(a*b*c)
        elif(a==c):
            self.message['text'] = 'A y C son Iguales LA SUMA ES : {}'.format(a+b+c)
        elif(b==0):
            self.message['text'] = 'B es 0, la resta es : {}'.format(a-c)
        else:
            self.message['text'] = 'Ingrese Valores : {}'.format(0)

    def bottonB(self):
        a = ""
        b = ""
        c = ""
        if():
          self.message[a] 
        elif():
          self.message['text'] = 'Repeticion de numero  : {}'.format(a*b+c)
        else:
           print ("Ingrese Un  Numero")
  
   
   

if __name__ == '__main__':
    window = Tk()
    
    app = Desk(window)

    window.mainloop()