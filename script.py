

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

import sys

PYTHON_VERSION = sys.version_info.major

if PYTHON_VERSION < 3:
    try:
        import tkinter as tk
    except ImportError:
        raise ImportError("Se requiere el modulo Tkinter")
else:
    try:
        import tkinter as tk
    except ImportError:
        raise ImportError("Se requiere el modulo tkinter")
    

def verificar(dato):
    if dato == "":
        dato = "error"
    return dato

def convertir(valor):
    if valor.isdecimal():
        valor = int(valor)
        if valor < 1 or valor > 10:
            valor = "error"
    else:
        valor = "error"
    return valor

def ver():
    mensaje = "Lista de alumnos:\n"
    for nombre in alumnos:
        cursos = alumnos[nombre]
        mensaje += nombre + " - " + str(cursos) + " cursos\n"
    text_label.delete('1.0', tk.END)  # Borrar el contenido anterior
    text_label.insert(tk.END, mensaje)  # Insertar el nuevo mensaje

def agregar():
    nombre_alumno = caja_nombre.get()
    nombre_alumno = verificar(nombre_alumno)
    cursos = cursos_combobox.get()  # Obtener el valor seleccionado del Combobox
    cursos = convertir(cursos)
    
    # Verificar si el nombre de alumno ya está en la lista
    if nombre_alumno in alumnos:
        mensaje = "El alumno ya está en la lista."
    elif nombre_alumno == "error":
        mensaje = "Error. Nombre vacío."
    elif cursos == "error":
        mensaje = "Error. Debes seleccionar un número de cursos entre 1 y 10."
    else:
        alumnos[nombre_alumno] = cursos
        mensaje = "Has ingresado un alumno correctamente."
        # Actualizar los valores del Combobox
        alumnos_combobox['values'] = list(alumnos.keys())  # Actualizar con las claves de alumnos
        cursos_combobox.set("")
        caja_nombre.delete(0, 'end')
    
    text_label.delete('1.0', tk.END)  # Borrar el contenido anterior
    text_label.insert(tk.END, mensaje)  # Insertar el nuevo mensaje
    ventana.after(2000, lambda: clear_message())

def ver_alumno():
    nombre = alumnos_combobox.get()  # Obtener el nombre seleccionado en el Combobox
    if nombre in alumnos:
        mensaje = nombre + " tiene " + str(alumnos[nombre]) + " cursos."
    else:
        mensaje = "Ese alumno no tiene cursos."
    alumnos_combobox.set("")
    text_label.delete('1.0', tk.END)  # Borrar el contenido anterior
    text_label.insert(tk.END, mensaje)  # Insertar el nuevo mensaje
    ventana.after(3000, lambda: clear_message())

def clear_message():
    # Limpia el mensaje en text_label
    text_label.delete('1.0', tk.END)

def eliminar_alumno():
    nombre = alumnos_combobox.get()  # Obtener el nombre seleccionado en el Combobox
    if nombre in alumnos:
        del alumnos[nombre]  # Eliminar al alumno del diccionario
        mensaje = "El alumno ha sido eliminado."
        # Actualizar los valores del Combobox
        alumnos_combobox['values'] = list(alumnos.keys())
        alumnos_combobox.set("")
    else:
        mensaje = "Ningun alumno seleccionado."
    
    text_label.delete('1.0', tk.END)  # Borrar el contenido anterior
    text_label.insert(tk.END, mensaje)
    ventana.after(2000, lambda: clear_message())

# Función para cambiar el color de fondo cuando el cursor entra en el botón
def on_button_enter(event):
    event.widget.config(bg='gray12')

# Función para restaurar el color de fondo cuando el cursor sale del botón
def on_button_leave(event):
    event.widget.config(bg='gray15')

alumnos = {}

ventana = tk.Tk()
ventana.config(width=340, height=470)
ventana.title("Proyecto Alumnos")
ventana.configure(background="gray20")


combostyle = ttk.Style() #Estilo para el combobox

combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'fieldbackground': 'gray17',
                                       'background': 'gray17',
                                       }}}
                         )
combostyle.theme_use('combostyle') 


etiqueta_titulo = tk.Label(
                text="Ingresar alumno:",
                background="gray20",
                foreground="gray66"
                )
etiqueta_titulo.place(x=25, y=20)

etiqueta_nombre = tk.Label(
                text="Nombre alumno:",
                background="gray20",
                foreground="gray66"
                )
etiqueta_nombre.place(x=25, y=60)

caja_nombre = tk.Entry(
                background="gray17",
                foreground="gray66"
                )
caja_nombre.place(x=150, y=60, width=165, height=20)

etiqueta_cursos = tk.Label(
                text="Cursos:",
                background="gray20",
                foreground="gray66"
                )
etiqueta_cursos.place(x=25, y=100)

# Cambiar caja_cursos a un Combobox para seleccionar números del 1 al 10
cursos_combobox = ttk.Combobox(
                    values=[str(i) for i in range(1, 11)],
                    state="readonly",
                    style="Custom.TCombobox"
                    )
cursos_combobox.place(x=150, y=100, width=50, height=20)

boton_agregar = tk.Button(
                text="Agregar a la lista",
                command=agregar,
                background="gray15",
                activebackground="gray12",
                relief="flat",
                foreground="gray55"
                )
boton_agregar.bind("<Enter>", on_button_enter)
boton_agregar.bind("<Leave>", on_button_leave)
boton_agregar.place(x=25, y=140)

etiqueta_nombre = tk.Label(
                text="Seleccionar alumno:",
                background="gray20",
                foreground="gray66",
                )
etiqueta_nombre.place(x=25, y=200)

boton_cursos = tk.Button(
                text="Ver cantidad de cursos",
                command=ver_alumno,
                background="gray15",
                activebackground="gray12",
                relief="flat",
                foreground="gray55"
                )
boton_cursos.bind("<Enter>", on_button_enter)
boton_cursos.bind("<Leave>", on_button_leave)
boton_cursos.place(x=25, y=260)

boton_eliminar = tk.Button(
                text="Eliminar alumno", 
                command=eliminar_alumno,                
                background="gray15",
                activebackground="gray12",
                relief="flat",
                foreground="gray55"
                )
boton_eliminar.bind("<Enter>", on_button_enter)
boton_eliminar.bind("<Leave>", on_button_leave)
boton_eliminar.place(x=160, y=260)

alumnos_combobox = ttk.Combobox(
                   values=list(alumnos.keys()),
                   state="readonly"
                   )
alumnos_combobox.place(x=25, y=230, width=150, height=20)


boton_lista = tk.Button(
                text="Ver toda la lista de alumnos",
                command=ver,                
                background="gray15",
                activebackground="gray12",
                relief="flat",
                foreground="gray55"
                )
boton_lista.bind("<Enter>", on_button_enter)
boton_lista.bind("<Leave>", on_button_leave)
boton_lista.place(x=20, y=330)

# Configurar text_label como un widget scrolledtext con fondo blanco y límite de 3 líneas
text_label = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, height=5, width=35,foreground="gray66")
text_label.place(x=20, y=370)
text_label.configure(bg="gray17")


ventana.mainloop()



#PROYECTO ALUMNOS
#estoy muy orgullosa de
# que hayas podido hacer
# esto, <3

