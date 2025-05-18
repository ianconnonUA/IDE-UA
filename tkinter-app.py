import tkinter as tk
from tkinter import scrolledtext
import subprocess

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def ejecutar_codigo():
    codigo = editor.get("1.0", tk.END)
    resultado.delete("1.0", tk.END)
    try:
        salida = subprocess.run(["python", "-c", codigo], capture_output=True, text=True)
        resultado.insert(tk.END, salida.stdout if salida.stdout else salida.stderr)
    except Exception as e:
        resultado.insert(tk.END, str(e))

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("IDE Python Simple")
ventana.geometry("600x400")

# Editor de código
editor = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=70, height=10)
editor.pack()

# Botón para ejecutar código
btn_ejecutar = tk.Button(ventana, text="Ejecutar", command=ejecutar_codigo)
btn_ejecutar.pack()

# Área de resultados
resultado = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=70, height=10, fg="green")
resultado.pack()

ventana.mainloop()