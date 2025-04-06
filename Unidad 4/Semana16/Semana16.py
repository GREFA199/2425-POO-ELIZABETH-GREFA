import tkinter as tk
from tkinter import font

# Inicializar ventana
ventana = tk.Tk()
ventana.title("Organizador de Tareas")
ventana.geometry("500x480")
ventana.configure(bg="#f0f0f0")

# Lista para llevar control del estado de cada tarea (False: pendiente, True: completada)
estados = []

# Fuente tachada
fuente_tachada = font.Font(overstrike=1)
fuente_normal = font.Font(overstrike=0)

# Campo de entrada
entrada = tk.Entry(ventana, width=35, font=("Arial", 12))
entrada.place(x=20, y=20)

# Listbox para mostrar tareas
lista = tk.Listbox(ventana, width=50, height=15, font=("Arial", 12))
lista.place(x=20, y=60)

# Funciones
def agregar(event=None):
    texto = entrada.get().strip()
    if texto:
        lista.insert(tk.END, texto)
        estados.append(False)
        entrada.delete(0, tk.END)

def completar(event=None):
    seleccion = lista.curselection()
    if seleccion:
        i = seleccion[0]
        texto = lista.get(i)
        lista.delete(i)
        estados[i] = not estados[i]
        nuevo_texto = texto
        lista.insert(i, nuevo_texto)

        # Aplicar estilo tachado o normal
        if estados[i]:
            lista.itemconfig(i, {'fg': 'green', 'font': fuente_tachada})
        else:
            lista.itemconfig(i, {'fg': 'black', 'font': fuente_normal})

def eliminar(event=None):
    seleccion = lista.curselection()
    if seleccion:
        i = seleccion[0]
        lista.delete(i)
        del estados[i]

def cerrar(event=None):
    ventana.destroy()

# Botones
btn_agregar = tk.Button(ventana, text="Agregar", width=15, command=agregar, bg="#90ee90")
btn_agregar.place(x=370, y=17)

btn_completar = tk.Button(ventana, text="Completar", width=20, command=completar)
btn_completar.place(x=80, y=380)

btn_eliminar = tk.Button(ventana, text="Eliminar", width=20, command=eliminar)
btn_eliminar.place(x=260, y=380)

# Atajos de teclado
ventana.bind("<Return>", agregar)
ventana.bind("<c>", completar)
ventana.bind("<C>", completar)
ventana.bind("<d>", eliminar)
ventana.bind("<D>", eliminar)
ventana.bind("<Escape>", cerrar)

# Iniciar la app
ventana.mainloop()

