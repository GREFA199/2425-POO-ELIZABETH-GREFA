import tkinter as tk
from tkinter import font

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Organizador de Tareas")
        self.root.geometry("500x480")
        self.root.configure(bg="#f0f0f0")

        self.estados = []  # False = pendiente, True = completada

        # Fuentes
        self.fuente_normal = font.Font(family="Arial", size=12)
        self.fuente_tachada = font.Font(family="Arial", size=12, overstrike=1)

        # Widgets
        self.entrada = tk.Entry(root, width=35, font=("Arial", 12))
        self.entrada.place(x=20, y=20)

        self.lista = tk.Listbox(root, width=50, height=15, font=self.fuente_normal)
        self.lista.place(x=20, y=60)

        self.btn_agregar = tk.Button(root, text="Agregar", width=15, command=self.agregar, bg="#90ee90")
        self.btn_agregar.place(x=370, y=17)

        self.btn_completar = tk.Button(root, text="Completar", width=20, command=self.completar)
        self.btn_completar.place(x=80, y=380)

        self.btn_eliminar = tk.Button(root, text="Eliminar", width=20, command=self.eliminar)
        self.btn_eliminar.place(x=260, y=380)

        # Atajos de teclado
        root.bind("<Return>", self.agregar)
        root.bind("<c>", self.completar)
        root.bind("<C>", self.completar)
        root.bind("<d>", self.eliminar)
        root.bind("<D>", self.eliminar)
        root.bind("<Escape>", lambda event: root.destroy())

    def agregar(self, event=None):
        texto = self.entrada.get().strip()
        if texto:
            self.lista.insert(tk.END, texto)
            self.lista.itemconfig(tk.END, {'fg': 'black', 'font': self.fuente_normal})
            self.estados.append(False)
            self.entrada.delete(0, tk.END)

    def completar(self, event=None):
        seleccion = self.lista.curselection()
        if seleccion:
            i = seleccion[0]
            self.estados[i] = not self.estados[i]

            if self.estados[i]:  # Completada
                self.lista.itemconfig(i, {'fg': 'green', 'font': self.fuente_tachada})
            else:  # Pendiente
                self.lista.itemconfig(i, {'fg': 'black', 'font': self.fuente_normal})

    def eliminar(self, event=None):
        seleccion = self.lista.curselection()
        if seleccion:
            i = seleccion[0]
            self.lista.delete(i)
            del self.estados[i]


# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
