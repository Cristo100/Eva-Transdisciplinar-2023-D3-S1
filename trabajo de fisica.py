import tkinter as tk

#----------------------
# Ventana
#-----------------------
# su creacion, dimensiones y color respectivamente.
ventana = tk.Tk()
ventana.geometry("800x600")
ventana.configure(background= "medium sea green")

#-------------------------
# Comienzo del trabajo
#-------------------------
#titulo del trabajo  
titulo = tk.Label (ventana,text = "trabajo de fisica", bg = "pink")
titulo.pack(fill= tk.X)

columna = tk.Canvas(ventana, width=200, height=600)
columna.place(x=0, y=0)
columna.create_rectangle(0, 0, 200, 800, fill='blue')

ventana.resizable(False,False)
ventana.mainloop()
