import tkinter as tk
ventana = tk.Tk() #ventana 
ventana.geometry("800x600") #dimensiones de la ventana 
ventana.configure(background= "medium sea green") #color de la ventana
titulo = tk.Label (ventana,text = "trabajo de fisica", bg = "pink") #titulo del trabajo  
titulo.pack(fill= tk.X)
columna = tk.Canvas(ventana, width=200, height=600)
columna.place(x=0, y=0)
columna.create_rectangle(0, 0, 200, 800, fill='blue')
ventana.resizable(False,False)
ventana.mainloop()