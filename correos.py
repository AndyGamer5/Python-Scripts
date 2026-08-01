import tkinter as tk
from tkinter import filedialog, messagebox

from sympy import python
import yagmail
import time

# Variable global para guardar PDF
archivo_pdf = ""

# ------------------------------
# Seleccionar PDF
# ------------------------------
def seleccionar_pdf():
    global archivo_pdf

    archivo_pdf = filedialog.askopenfilename(
        title="Seleccionar PDF",
        filetypes=[("PDF files", "*.pdf")]
    )

    if archivo_pdf:
        label_pdf.config(text=f"PDF seleccionado:\n{archivo_pdf}")

# ------------------------------
# Enviar correos
# ------------------------------
def enviar_correos():

    correo = entry_correo.get()
    password = entry_password.get()
    asunto = entry_asunto.get()

    mensaje = texto_mensaje.get("1.0", tk.END)

    correos = texto_correos.get("1.0", tk.END)
    lista_correos = correos.strip().split("\n")

    # Validaciones
    if not correo or not password:
        messagebox.showerror("Error", "Debes ingresar tu correo y contraseña")
        return

    if not asunto:
        messagebox.showerror("Error", "Debes ingresar un asunto")
        return

    if not archivo_pdf:
        messagebox.showerror("Error", "Debes seleccionar un PDF")
        return

    try:

        yag = yagmail.SMTP(correo, password)

        enviados = 0

        for destino in lista_correos:

            destino = destino.strip()

            if destino:

                yag.send(
                    to=destino,
                    subject=asunto,
                    contents=mensaje,
                    attachments=archivo_pdf
                )

                enviados += 1

                estado_label.config(
                    text=f"Enviado a: {destino}"
                )

                ventana.update()

                # Pausa anti-spam
                time.sleep(2)

        messagebox.showinfo(
            "Éxito",
            f"Correos enviados correctamente: {enviados}"
        )

        estado_label.config(text="Proceso terminado")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ------------------------------
# Ventana principal
# ------------------------------
ventana = tk.Tk()
ventana.title("Sistema de Envío de Correos")
ventana.geometry("700x700")
ventana.config(bg="#f4f4f4")

# ------------------------------
# Título
# ------------------------------
label_titulo = tk.Label(
    ventana,
    text="Envío Automático de Correos",
    font=("Arial", 18, "bold"),
    bg="#f4f4f4"
)
label_titulo.pack(pady=10)

# ------------------------------
# Correo
# ------------------------------
frame_correo = tk.Frame(ventana, bg="#f4f4f4")
frame_correo.pack(fill="x", padx=20, pady=5)

label_correo = tk.Label(
    frame_correo,
    text="Correo Gmail:",
    bg="#f4f4f4"
)
label_correo.pack(anchor="w")

entry_correo = tk.Entry(frame_correo, width=60)
entry_correo.pack(fill="x")

# ------------------------------
# Password
# ------------------------------
frame_password = tk.Frame(ventana, bg="#f4f4f4")
frame_password.pack(fill="x", padx=20, pady=5)

label_password = tk.Label(
    frame_password,
    text="Contraseña de aplicación:",
    bg="#f4f4f4"
)
label_password.pack(anchor="w")

entry_password = tk.Entry(frame_password, width=60, show="*")
entry_password.pack(fill="x")

# ------------------------------
# Asunto
# ------------------------------
frame_asunto = tk.Frame(ventana, bg="#f4f4f4")
frame_asunto.pack(fill="x", padx=20, pady=5)

label_asunto = tk.Label(
    frame_asunto,
    text="Asunto:",
    bg="#f4f4f4"
)
label_asunto.pack(anchor="w")

entry_asunto = tk.Entry(frame_asunto, width=60)
entry_asunto.pack(fill="x")

# ------------------------------
# Mensaje
# ------------------------------
frame_mensaje = tk.Frame(ventana, bg="#f4f4f4")
frame_mensaje.pack(fill="both", padx=20, pady=5)

label_mensaje = tk.Label(
    frame_mensaje,
    text="Mensaje:",
    bg="#f4f4f4"
)
label_mensaje.pack(anchor="w")

texto_mensaje = tk.Text(frame_mensaje, height=8)
texto_mensaje.pack(fill="both")

# ------------------------------
# Correos destinatarios
# ------------------------------
frame_correos = tk.Frame(ventana, bg="#f4f4f4")
frame_correos.pack(fill="both", padx=20, pady=5)

label_correos = tk.Label(
    frame_correos,
    text="Correos destinatarios (uno por línea):",
    bg="#f4f4f4"
)
label_correos.pack(anchor="w")

texto_correos = tk.Text(frame_correos, height=10)
texto_correos.pack(fill="both")

# ------------------------------
# Botón PDF
# ------------------------------
btn_pdf = tk.Button(
    ventana,
    text="Seleccionar PDF",
    command=seleccionar_pdf,
    bg="#3498db",
    fg="white",
    font=("Arial", 11, "bold")
)
btn_pdf.pack(pady=10)

label_pdf = tk.Label(
    ventana,
    text="Ningún PDF seleccionado",
    bg="#f4f4f4"
)
label_pdf.pack()

# ------------------------------
# Botón enviar
# ------------------------------
btn_enviar = tk.Button(
    ventana,
    text="Enviar Correos",
    command=enviar_correos,
    bg="#27ae60",
    fg="white",
    font=("Arial", 14, "bold"),
    width=20,
    height=2
)
btn_enviar.pack(pady=20)

# ------------------------------
# Estado
# ------------------------------
estado_label = tk.Label(
    ventana,
    text="Esperando acción...",
    bg="#f4f4f4",
    fg="#555"
)
estado_label.pack(pady=10)

# ------------------------------
# Ejecutar ventana
# ------------------------------
ventana.mainloop()
