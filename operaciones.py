import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
import os

class GeneradorRecibosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Recibos de Agua")
        self.root.geometry("600x700")
        self.root.configure(padx=20, pady=20)

        # Variables de datos
        self.df = pd.read_csv("operaguas.csv", encoding='latin1')
        self.datos_exportar = [] # Lista para guardar los cálculos y exportarlos a Canva

        # --- SECCIÓN 1: Carga de Datos ---
        marco_carga = ttk.LabelFrame(self.root, text="1. Base de Datos (Excel/CSV)", padding=10)
        marco_carga.pack(fill="x", pady=(0, 15))

        self.btn_cargar = ttk.Button(marco_carga, text="Cargar Archivo", command=self.cargar_archivo)
        self.btn_cargar.pack(side="left", padx=5)

        self.lbl_archivo = ttk.Label(marco_carga, text="Ningún archivo cargado")
        self.lbl_archivo.pack(side="left", padx=10)

        # --- SECCIÓN 2: Selección de Titular ---
        marco_seleccion = ttk.LabelFrame(self.root, text="2. Búsqueda de Titular/Contrato", padding=10)
        marco_seleccion.pack(fill="x", pady=(0, 15))

        self.combo_titulares = ttk.Combobox(marco_seleccion, state="readonly", width=50)
        self.combo_titulares.pack(side="left", padx=5)
        self.combo_titulares.bind("<<ComboboxSelected>>", self.autocompletar_datos)

        # --- SECCIÓN 3: Formulario y Lecturas ---
        marco_formulario = ttk.LabelFrame(self.root, text="3. Datos y Lecturas del Mes", padding=10)
        marco_formulario.pack(fill="x", pady=(0, 15))

        # Crear campos de entrada
        self.entradas = {}
        campos = [
            ("No. de Contrato:", "contrato"),
            ("Correo Electrónico:", "correo"),
            ("Lectura Inicial (m3):", "lectura_inicial"),
            ("Lectura Final (m3):", "lectura_final"),
            ("Deuda Anterior ($):", "deuda"),
            ("Tarifa por m3 ($):", "tarifa")
        ]

        for i, (label_text, key) in enumerate(campos):
            ttk.Label(marco_formulario, text=label_text).grid(row=i, column=0, sticky="w", pady=5)
            ent = ttk.Entry(marco_formulario, width=30)
            ent.grid(row=i, column=1, pady=5, padx=10)
            self.entradas[key] = ent
        
        # Valor por defecto para tarifa
        self.entradas["tarifa"].insert(0, "15.50")

        # --- SECCIÓN 4: Cálculos y Resultados ---
        marco_calculo = ttk.Frame(self.root)
        marco_calculo.pack(fill="x", pady=10)

        self.btn_calcular = ttk.Button(marco_calculo, text="Calcular Operaciones", command=self.calcular_totales)
        self.btn_calcular.pack(pady=10)

        marco_resultados = ttk.LabelFrame(self.root, text="4. Resumen a Pagar", padding=10)
        marco_resultados.pack(fill="x", pady=(0, 15))

        self.lbl_consumo = ttk.Label(marco_resultados, text="Consumo del Mes: 0.00 m3", font=("Arial", 11, "bold"))
        self.lbl_consumo.pack(anchor="w", pady=2)
        
        self.lbl_subtotal = ttk.Label(marco_resultados, text="Subtotal por Consumo: $0.00", font=("Arial", 11, "bold"))
        self.lbl_subtotal.pack(anchor="w", pady=2)
        
        self.lbl_total = ttk.Label(marco_resultados, text="GRAN TOTAL A PAGAR: $0.00", font=("Arial", 14, "bold"), foreground="red")
        self.lbl_total.pack(anchor="w", pady=10)

        # --- SECCIÓN 5: Exportar a Canva ---
        marco_exportar = ttk.Frame(self.root)
        marco_exportar.pack(fill="x", pady=10)

        self.btn_guardar = ttk.Button(marco_exportar, text="Guardar Registro Actual", command=self.guardar_registro)
        self.btn_guardar.pack(side="left", padx=5)

        self.btn_exportar = ttk.Button(marco_exportar, text="Exportar CSV para Canva", command=self.exportar_csv_canva)
        self.btn_exportar.pack(side="right", padx=5)

    def cargar_archivo(self):
        ruta = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv"), ("Archivos Excel", "*.xlsx")])
        if ruta:
            try:
                if ruta.endswith('.csv'):
                    self.df = pd.read_csv(ruta)
                else:
                    self.df = pd.read_excel(ruta)
                
                self.lbl_archivo.config(text=os.path.basename(ruta))
                
                # Asumiendo que existe una columna llamada 'Titular'
                # Si tu columna se llama diferente, cambia 'Titular' por el nombre exacto
                if 'Titular' in self.df.columns:
                    titulares = self.df['Titular'].dropna().astype(str).tolist()
                    self.combo_titulares['values'] = titulares
                    messagebox.showinfo("Éxito", "Base de datos cargada correctamente.")
                else:
                    messagebox.showwarning("Advertencia", "No se encontró la columna 'Titular' en el archivo.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo leer el archivo: {e}")

    def autocompletar_datos(self, event):
        seleccion = self.combo_titulares.get()
        if self.df is not None:
            # Filtrar la fila del titular seleccionado
            fila = self.df[self.df['Titular'].astype(str) == seleccion].iloc[0]
            
            # Limpiar entradas
            for ent in self.entradas.values():
                ent.delete(0, tk.END)
            
            # Autocompletar (Ajusta los nombres de las columnas según tu Excel)
            # Usaremos get() con un valor por defecto '' para evitar errores si la columna no existe
            self.entradas["contrato"].insert(0, str(fila.get('No. De contrato', '')))
            self.entradas["correo"].insert(0, str(fila.get('Correo', '')))
            
            # Ajusta estos nombres exactos de columnas ("lectura octubre inicial", etc.)
            self.entradas["lectura_inicial"].insert(0, str(fila.get('lectura octubre inicial', '0')))
            self.entradas["lectura_final"].insert(0, str(fila.get('lectura octubre final', '0')))
            self.entradas["deuda"].insert(0, str(fila.get('DEUDA ACUMULADA DEL MES ANTERIOR SEP', '0')))
            self.entradas["tarifa"].insert(0, "15.50") # Volver a poner la tarifa por defecto

    def calcular_totales(self):
        try:
            lec_ini = float(self.entradas["lectura_inicial"].get())
            lec_fin = float(self.entradas["lectura_final"].get())
            deuda = float(self.entradas["deuda"].get())
            tarifa = float(self.entradas["tarifa"].get())

            consumo = lec_fin - lec_ini

            if consumo < 0:
                messagebox.showwarning("Error de Lectura", "La lectura final es menor a la inicial. Revisa los datos.")
                return False

            subtotal = consumo * tarifa
            total = subtotal + deuda

            # Actualizar Etiquetas
            self.lbl_consumo.config(text=f"Consumo del Mes: {consumo:.2f} m3")
            self.lbl_subtotal.config(text=f"Subtotal por Consumo: ${subtotal:.2f}")
            self.lbl_total.config(text=f"GRAN TOTAL A PAGAR: ${total:.2f}")
            
            return {"consumo": consumo, "subtotal": subtotal, "total": total}

        except ValueError:
            messagebox.showerror("Error de Datos", "Por favor, asegúrate de que las lecturas, tarifa y deuda sean números válidos.")
            return False

    def guardar_registro(self):
        calculos = self.calcular_totales()
        if calculos:
            registro = {
                "Titular": self.combo_titulares.get(),
                "Contrato": self.entradas["contrato"].get(),
                "Correo": self.entradas["correo"].get(),
                "Lectura Inicial": self.entradas["lectura_inicial"].get(),
                "Lectura Final": self.entradas["lectura_final"].get(),
                "Consumo": f"{calculos['consumo']:.2f}",
                "Deuda Anterior": f"{float(self.entradas['deuda'].get()):.2f}",
                "Total Pagar": f"{calculos['total']:.2f}"
            }
            self.datos_exportar.append(registro)
            messagebox.showinfo("Guardado", f"Registro de {registro['Titular']} guardado en memoria. Llevas {len(self.datos_exportar)} registros listos para Canva.")

    def exportar_csv_canva(self):
        if not self.datos_exportar:
            messagebox.showwarning("Sin datos", "No hay registros guardados para exportar.")
            return
        
        ruta_guardado = filedialog.asksaveasfilename(
            defaultextension=".csv", 
            filetypes=[("Archivo CSV", "*.csv")],
            initialfile="Datos_Para_Canva.csv"
        )
        
        if ruta_guardado:
            df_exportar = pd.DataFrame(self.datos_exportar)
            # Exportar sin índice para que Canva lo lea perfecto
            df_exportar.to_csv(ruta_guardado, index=False, encoding='utf-8-sig')
            messagebox.showinfo("Éxito", f"Archivo listo para Canva guardado en:\n{ruta_guardado}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GeneradorRecibosApp(root)
    root.mainloop()