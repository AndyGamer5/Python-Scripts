import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
import os
import webbrowser
import tempfile
import re
from datetime import datetime
from string import Template

# --- PLANTILLA HTML (Tu diseño integrado en Python) ---
PLANTILLA_HTML = Template("""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Recibo ${recibo}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&display=swap');
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{font-family:'IBM Plex Sans',Arial,sans-serif;font-size:12px;color:#1a1a2e;background:#e8edf2}
.page{width:210mm;min-height:297mm;margin:10mm auto;background:#fff;display:flex;flex-direction:column;box-shadow:0 4px 24px rgba(0,0,0,.12)}
.top-bar{display:grid;grid-template-columns:1fr 1fr;background:#fff;border-bottom:3px solid #white}
.top-left{padding:16px 22px;display:flex;align-items:center}
.top-right{background:#1e4080;padding:16px 20px;color:#fff}
.top-right .empresa-nombre{font-size:16px;font-weight:700;color:#fff;margin-bottom:4px}
.top-right p{font-size:11px;color:#b8cfe8;line-height:1.7}
.top-right .horario{margin-top:10px}
.top-right .horario strong{color:#fff;font-size:15px;display:block;margin-bottom:2px}
.recibo-bar{text-align:center;padding:10px 20px;border-bottom:1px solid #e2e8f0;background:#fff;}
.recibo-bar .rb-label{font-size:20px;font-weight:300;color:#1a3a6b}
.recibo-bar .rb-numero{font-size:20px;font-weight:700;color:#dc2626;margin-left:8px;letter-spacing:.5px}
.body-wrap{display:grid;grid-template-columns:1fr 220px;flex:1}
.col-left{padding:14px 20px;border-right:1px solid #dde3ec}
.col-right{padding:14px 16px;background:#f0f4fb}
.info-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px;}
.info-left,.info-right{display:flex;flex-direction:column;gap:8px}
.chip{background:#f0f4fb;border:1px solid #dde6f5;border-radius:6px;padding:9px 12px}
.chip .cl{font-size:10px;font-weight:700;color:#1a3a6b;margin-bottom:3px;text-transform:uppercase;letter-spacing:.4px}
.chip .cv{font-size:12px;color:#374151;font-weight:400;line-height:1.5}
.chip .cv.bold{font-weight:700;color:#1a1a2e}
.section-title{font-size:10px;font-weight:700;color:#1a3a6b;text-transform:uppercase;letter-spacing:.8px;margin:12px 0 6px}
.concepto-row{display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #f1f5f9;font-size:12px;color:#374151}
.concepto-row .cc{color:#64748b}
.concepto-row.total{font-weight:700;font-size:14px;color:#1a3a6b;border-bottom:none;padding-top:10px;border-top:2px solid #1a3a6b;margin-top:4px}
table{width:100%;border-collapse:collapse;font-size:11px;margin-bottom:10px}
thead tr{background:#1a3a6b;color:#fff}
thead th{padding:7px 9px;text-align:left;font-size:10px;font-weight:600}
tbody tr:nth-child(even){background:#f5f8fd}
tbody td{padding:7px 9px;border-bottom:1px solid #e2e8f0;color:#374151}
.data-box{background:#fff;border:1px solid #c8d6ec;border-radius:5px;padding:7px 10px;margin-bottom:6px;font-size:11px}
.data-box .db-label{color:#5b7ab5;font-weight:600;font-size:10px;margin-bottom:1px}
.data-box .db-value{color:#1a1a2e;font-weight:600}
.resumen-box{background:#fff;border:1px solid #c8d6ec;border-radius:5px;padding:7px 10px;margin-bottom:6px;display:flex;justify-content:space-between;align-items:center;font-size:11px}
.resumen-box .rb-label{color:#5b7ab5;font-weight:600}
.resumen-box .rb-value{font-weight:700;color:#1a1a2e}
.resumen-box.total-box{background:#1a3a6b;border-color:#1a3a6b}
.resumen-box.total-box .rb-label,.resumen-box.total-box .rb-value{color:#fff;font-size:13px}
.alerta{background:#fff8e1;border-left:3px solid #f59e0b;border-radius:4px;padding:8px 12px;font-size:11px;color:#78350f;margin-bottom:12px}
.corte{border-top:2px dashed #94a3b8;margin:0 20px;display:flex;align-items:center;gap:6px;color:#94a3b8;font-size:11px;padding:7px 0}
.corte::before{content:'✂';font-size:15px}
.comprobante{display:grid;grid-template-columns:1fr 1fr 1fr;border-top:1px solid #dde3ec}
.comp-col{padding:12px 16px;border-right:1px solid #dde3ec}
.comp-col:last-child{border-right:none}
.comp-title{font-size:10px;font-weight:700;color:#1a3a6b;text-transform:uppercase;letter-spacing:.6px;margin-bottom:7px}
.comp-badge{background:#1a3a6b;color:#fff;text-align:center;border-radius:4px;padding:5px 8px;font-size:12px;font-weight:700;margin-bottom:7px}
.comp-line{font-size:11px;color:#374151;margin-bottom:3px;line-height:1.5}
.comp-line strong{color:#1a1a2e}
.comp-link{color:#1a3a6b;font-weight:700;font-size:11px;text-decoration:none}
.comp-field{background:#f0f4fb;border:1px solid #c8d6ec;border-radius:4px;padding:6px 9px;margin-bottom:5px;font-size:11px}
.comp-field .cf-l{color:#5b7ab5;font-size:10px;font-weight:600;margin-bottom:1px}
.comp-field .cf-v{font-weight:700;color:#1a1a2e}
.contact-row{font-size:11px;color:#374151;margin-bottom:3px}
.comp-footer{background:#1a3a6b;color:#b8cfe8;display:grid;grid-template-columns:1fr auto;align-items:center;padding:10px 20px;font-size:10px;gap:12px}
.logo{height:120px;width:auto;display:block}
@media print{body{background:#fff}.page{margin:0;box-shadow:none}}
</style>
</head>
<body>
<div class="page">
  <div class="top-bar">
    <div class="top-left">
      <h1 style="color:#1e4080; font-size:24px;">OPERAGUAS</h1>
    </div>
    <div class="top-right">
      <div class="empresa-nombre">Operaguas de Huimilpan S.A. de C.V.</div>
      <p>RFC: BCI181031743<br>
         Dirección: Los Cues Sin Número, Los Cues, Municipio<br>
         de Huimilpan, Querétaro, C.P. 76970</p>
      <div class="horario">
        <strong>Horario de atención</strong>
        <p>Lunes a viernes de 9:00 a 18:00 hrs.</p>
      </div>
    </div>
  </div>

  <div class="recibo-bar">
    <span class="rb-label">Recibo</span>
    <span class="rb-numero">${recibo}</span>
  </div>

  <div class="body-wrap">
    <div class="col-left">
      ${alertaHtml}
      <div class="info-grid">
        <div class="info-left">
          <div class="chip"><div class="cl">Nombre</div><div class="cv bold">${titular}</div></div>
          <div class="chip"><div class="cl">Domicilio</div><div class="cv">${domicilio}</div></div>
        </div>
        <div class="info-right">
          <div class="chip"><div class="cl">Fecha de emisión</div><div class="cv bold">${emision}</div></div>
          <div class="chip"><div class="cl">Fecha de vencimiento</div><div class="cv bold">${vencimiento}</div></div>
          <div class="chip"><div class="cl">Periodo de consumo</div><div class="cv">${periodo}</div></div>
        </div>
      </div>

      <div class="section-title">Concepto</div>
      <div class="concepto-row"><span class="cc">Servicio integral de agua potable</span><span>${subtotal_fmt}</span></div>
      <div class="concepto-row"><span class="cc">IVA</span><span>${iva_fmt}</span></div>
      <div class="concepto-row"><span class="cc">Adeudo anterior</span><span style="color:${color_adeudo}">${adeudoAnt_fmt}</span></div>
      <div class="concepto-row total"><span>Total a pagar</span><span>${total_fmt}</span></div>

      <div class="section-title" style="margin-top:14px">Datos de Consumo</div>
      <table>
        <thead>
          <tr>
            <th>No. de medidor</th><th>Lec. inicial (m³)</th><th>Lec. final (m³)</th><th>Consumo (m³)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>${medidor}</td><td>${lecIni}</td><td>${lecFin}</td><td>${consumo}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="col-right">
      <div class="section-title">Datos generales de toma y consumo</div>
      <div class="data-box"><div class="db-label">No. de contrato</div><div class="db-value">${contrato}</div></div>
      <div class="data-box"><div class="db-label">Tipo de tarifa</div><div class="db-value">${tarifa}</div></div>
      <div class="data-box"><div class="db-label">Meses con adeudo vencidos</div><div class="db-value">${mesesAdeudo}</div></div>

      <div class="section-title" style="margin-top:12px">Resumen de pago</div>
      <div class="resumen-box"><span class="rb-label">Subtotal</span><span class="rb-value">${subtotal_fmt}</span></div>
      <div class="resumen-box"><span class="rb-label">IVA (16%)</span><span class="rb-value">${iva_fmt}</span></div>
      <div class="resumen-box"><span class="rb-label">Adeudo anterior</span><span class="rb-value" style="color:${color_adeudo}">${adeudoAnt_fmt}</span></div>
      <div class="resumen-box total-box"><span class="rb-label">Total a pagar</span><span class="rb-value">${total_fmt}</span></div>
    </div>
  </div>

  <div class="corte">Línea de corte – Conserve este comprobante</div>

  <div class="comprobante">
    <div class="comp-col">
      <div class="comp-title">Realiza tu Pago</div>
      <div class="comp-badge">Banco: Afirme</div>
      <div class="comp-line"><strong>No. de cuenta:</strong> 011431014590</div>
      <div class="comp-line"><strong>CLABE:</strong> 062680114310145909</div>
      <div class="comp-line"><strong>Referencia:</strong> ${contrato}</div>
    </div>
    <div class="comp-col">
      <div class="comp-title">Atención a clientes</div>
      <div class="contact-row"><strong>(446) 113 9999</strong></div>
      <div class="contact-row"><a class="comp-link" href="mailto:atencion@operaguas.mx">atencion@operaguas.mx</a></div>
    </div>
    <div class="comp-col">
      <div class="comp-title">Comprobante de pago</div>
      <div class="comp-field"><div class="cf-l">No. de contrato</div><div class="cf-v">${contrato}</div></div>
      <div class="comp-field"><div class="cf-l">Total a pagar</div><div class="cf-v">${total_fmt}</div></div>
    </div>
  </div>
</div>
</body>
</html>
""")

class GeneradorRecibosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Recibos Web")
        self.root.geometry("600x700")
        self.root.configure(padx=20, pady=20)

        self.df = None

        # --- SECCIÓN 1: Carga de Datos ---
        marco_carga = ttk.LabelFrame(self.root, text="1. Cargar Base de Datos", padding=10)
        marco_carga.pack(fill="x", pady=(0, 10))

        self.btn_cargar = ttk.Button(marco_carga, text="Cargar Archivo Excel/CSV", command=self.cargar_archivo)
        self.btn_cargar.pack(side="left", padx=5)

        self.lbl_archivo = ttk.Label(marco_carga, text="Ningún archivo cargado")
        self.lbl_archivo.pack(side="left", padx=10)

        # --- SECCIÓN 2: Selección ---
        marco_seleccion = ttk.LabelFrame(self.root, text="2. Seleccionar Titular", padding=10)
        marco_seleccion.pack(fill="x", pady=(0, 10))

        self.combo_titulares = ttk.Combobox(marco_seleccion, state="readonly", width=50)
        self.combo_titulares.pack(side="left", padx=5)
        self.combo_titulares.bind("<<ComboboxSelected>>", self.autocompletar_datos)

        # --- SECCIÓN 3: Formulario ---
        marco_formulario = ttk.LabelFrame(self.root, text="3. Datos para el Recibo", padding=10)
        marco_formulario.pack(fill="x", pady=(0, 10))

        self.entradas = {}
        campos = [
            ("Titular (Nombre):", "Titular"),
            ("No. de Contrato:", "contrato"),
            ("No. de Medidor:", "medidor"),
            ("Lectura Inicial (m3):", "lectura_inicial"),
            ("Lectura Final (m3):", "lectura_final"),
            ("Deuda Anterior ($):", "deuda"),
            ("Tarifa por m3 ($):", "tarifa"),
            ("No. Lote:", "lote"),
            ("Privada:", "privada"),
        ]

        for i, (label_text, key) in enumerate(campos):
            ttk.Label(marco_formulario, text=label_text).grid(row=i, column=0, sticky="w", pady=5)
            ent = ttk.Entry(marco_formulario, width=35)
            ent.grid(row=i, column=1, pady=5, padx=10)
            self.entradas[key] = ent
        
        self.entradas["tarifa"].insert(0, "15.50")

        # --- SECCIÓN 4: Botón de Generar Recibo ---
        marco_accion = ttk.Frame(self.root)
        marco_accion.pack(fill="x", pady=20)

        self.btn_generar = tk.Button(marco_accion, text="🎯 Generar y Ver Recibo", font=("Arial", 14, "bold"), bg="#1e4080", fg="white", command=self.generar_recibo_html)
        self.btn_generar.pack(fill="x", ipady=10)

    def cargar_archivo(self):
        ruta = filedialog.askopenfilename(filetypes=[("Archivos Excel o CSV", "*.xlsx *.xls *.csv")])
        if not ruta:
            return

        try:
            self.df = None
            if ruta.endswith('.csv'):
                codificaciones = ['utf-8', 'latin1', 'utf-8-sig', 'cp1252']
                for cod in codificaciones:
                    try:
                        temp_df = pd.read_csv(ruta, encoding=cod)
                        temp_df.columns = temp_df.columns.astype(str).str.strip() 
                        if 'Titular' in temp_df.columns:
                            self.df = temp_df
                            break
                    except:
                        continue
            else:
                archivo_excel = pd.ExcelFile(ruta)
                for hoja in archivo_excel.sheet_names:
                    temp_df = pd.read_excel(archivo_excel, sheet_name=hoja)
                    temp_df.columns = temp_df.columns.astype(str).str.strip() 
                    if 'Titular' in temp_df.columns:
                        self.df = temp_df
                        break 

            if self.df is not None and 'Titular' in self.df.columns:
                self.lbl_archivo.config(text=os.path.basename(ruta))
                titulares_limpios = self.df['Titular'].dropna().astype(str).tolist()
                titulares_unicos = sorted(list(set(titulares_limpios)))
                self.combo_titulares['values'] = titulares_unicos
                messagebox.showinfo("Éxito", "Base de datos cargada correctamente.")
            else:
                messagebox.showwarning("Advertencia", "No se encontró la columna 'Titular' en el archivo.")

        except Exception as e:
            messagebox.showerror("Error de lectura", f"Hubo un problema:\n{e}")

    def autocompletar_datos(self, event):
        seleccion = self.combo_titulares.get()
        if self.df is not None:
            fila = self.df[self.df['Titular'].astype(str) == seleccion].iloc[0]
            
            for ent in self.entradas.values():
                ent.delete(0, tk.END)
            
            self.entradas["Titular"].insert(0, seleccion)
            self.entradas["contrato"].insert(0, str(fila.get('No. De contrato', 'S/N')))
            self.entradas["medidor"].insert(0, str(fila.get('medidor H', 'S/N')))
            self.entradas["lectura_inicial"].insert(0, str(fila.get('lectura octubre inicial', '0')))
            self.entradas["lectura_final"].insert(0, str(fila.get('lectura octubre final', '0')))
            self.entradas["deuda"].insert(0, str(fila.get('DEUDA ACUMULADA DEL MES ANTERIOR SEP', '0')))
            self.entradas["tarifa"].insert(0, "15.50")
            self.entradas["lote"].insert(0, str(fila.get('No. Lote:', 'S/N')))
            self.entradas["privada"].insert(0, str(fila.get('Privada:', 'S/N')))

    def generar_recibo_html(self):
        try:
            lec_ini = float(self.entradas["lectura_inicial"].get())
            lec_fin = float(self.entradas["lectura_final"].get())
            deuda_ant = float(self.entradas["deuda"].get())
            tarifa = float(self.entradas["tarifa"].get())

            consumo = lec_fin - lec_ini
            if consumo < 0:
                messagebox.showwarning("Aviso", "La lectura final es menor a la inicial.")
                consumo = 0

            subtotal = consumo * tarifa
            iva = subtotal * 0.16
            total = subtotal + iva + deuda_ant
            meses_adeudo = int((deuda_ant / 278.38) + 0.99) if deuda_ant > 0 else 0

            fecha_hoy = datetime.now().strftime("%d/%m/%Y")
            alerta = ''
            if deuda_ant > 0:
                alerta = '''<div class="alerta"><strong>⚠️ Aviso:</strong> Su recibo presenta adeudo vencido. Le invitamos a regularizar su servicio a la brevedad.</div>'''

            datos_plantilla = {
                "recibo": f"F-{self.entradas['contrato'].get()}-{datetime.now().strftime('%m%y')}",
                "titular": self.entradas["Titular"].get(),
                "domicilio": "Boulevard Padre José Guadalupe Velázquez Pedraza, Número Exterior [" + self.entradas["lote"].get() + "], Número Interior [" + self.entradas["lote"].get() + "] Condominio [" + self.entradas["privada"].get() + "], Los Cues, Municipio de Huimilpan, Querétaro, C.P. 76970",
                "emision": fecha_hoy,
                "vencimiento": fecha_hoy,
                "periodo": "01 Mayo 2025 - 31 Mayo 2025",
                "medidor": self.entradas["medidor"].get(),
                "contrato": self.entradas["contrato"].get(),
                "tarifa": "Doméstico Alto",
                "mesesAdeudo": str(meses_adeudo),
                "lecIni": f"{lec_ini:.2f}",
                "lecFin": f"{lec_fin:.2f}",
                "consumo": f"{consumo:.2f}",
                "subtotal_fmt": f"${subtotal:,.2f}",
                "iva_fmt": f"${iva:,.2f}",
                "adeudoAnt_fmt": f"${deuda_ant:,.2f}",
                "total_fmt": f"${total:,.2f}",
                "color_adeudo": "#dc2626" if deuda_ant > 0 else "#374151",
                "alertaHtml": alerta
            }

            html_final = PLANTILLA_HTML.safe_substitute(datos_plantilla)

            # --- SOLUCIÓN DEL ERROR DE RUTA ---
            # Limpiamos el texto del contrato para que no tenga caracteres prohibidos como la '/' de S/N
            contrato_crudo = self.entradas['contrato'].get()
            contrato_limpio = re.sub(r'[\\/*?:"<>|]', '_', contrato_crudo)
            
            ruta_temporal = os.path.join(tempfile.gettempdir(), f"Recibo_{contrato_limpio}.html")
            
            with open(ruta_temporal, "w", encoding="utf-8") as archivo:
                archivo.write(html_final)
            
            webbrowser.open(f"file://{os.path.realpath(ruta_temporal)}")

        except ValueError:
            messagebox.showerror("Error", "Asegúrate de que las lecturas y la deuda sean números correctos.")
        except Exception as e:
            messagebox.showerror("Error de guardado", f"No se pudo crear el recibo:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GeneradorRecibosApp(root)
    root.mainloop()