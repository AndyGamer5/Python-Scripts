import json
from datetime import datetime

class CalendarioAgenda:
    def __init__(self):
        self.archivo = "tareas.json"
        self.tareas = self.cargar()

    # ------------------------------
    #  ARCHIVO JSON
    # ------------------------------
    def cargar(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []

    def guardar(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(self.tareas, f, indent=2, ensure_ascii=False)

    # ------------------------------
    #  MOSTRAR TAREAS
    # ------------------------------
    def tareas_pendientes(self):
        print("\n=== TAREAS PENDIENTES ===")
        pendientes = [t for t in self.tareas if not t["completada"]]

        if not pendientes:
            print("No hay tareas pendientes.")
            return pendientes

        for i, t in enumerate(pendientes, 1):
            print(f"{i}. {t['titulo']} [{t['prioridad']}]")
            print(f"   {t['fecha']} {t['hora']}")
        return pendientes

    # ------------------------------
    #  AGREGAR
    # ------------------------------
    def agregar(self):
        print("\n--- AGREGAR TAREA ---")
        tarea = {
            "titulo": input("Título: "),
            "fecha": input("Fecha (YYYY-MM-DD): "),
            "hora": input("Hora (HH:MM): "),
            "prioridad": input("Prioridad (Alta/Media/Baja): ") or "Media",
            "completada": False
        }
        self.tareas.append(tarea)
        self.guardar()
        print("✓ Tarea agregada.")

    # ------------------------------
    #  COMPLETAR
    # ------------------------------
    def completar(self):
        pendientes = self.tareas_pendientes()
        if not pendientes:
            return
        
        try:
            idx = int(input("\nNúmero de tarea a completar: ")) - 1
            pendientes[idx]["completada"] = True
            self.guardar()
            print("✓ Tarea completada.")
        except:
            print("❌ Número inválido.")

    # ------------------------------
    #  ELIMINAR
    # ------------------------------
    def eliminar(self):
        pendientes = self.tareas_pendientes()
        if not pendientes:
            return
        
        try:
            idx = int(input("\nNúmero de tarea a eliminar: ")) - 1
            self.tareas.remove(pendientes[idx])
            self.guardar()
            print("✓ Tarea eliminada.")
        except:
            print("❌ Número inválido.")

    # ------------------------------
    #  ORDENAR
    # ------------------------------
    def ordenar(self):
        prioridades = {"Alta": 1, "Media": 2, "Baja": 3}

        def clave(t):
            try:
                fecha = datetime.strptime(t["fecha"], "%Y-%m-%d")
            except:
                fecha = datetime.max

            prioridad = prioridades.get(t["prioridad"], 2)
            hora = t.get("hora", "23:59")

            return (fecha, prioridad, hora)

        self.tareas.sort(key=clave)
        self.guardar()
        print("\n✓ Tareas ordenadas.")

    # ------------------------------
    #  ALERTAS
    # ------------------------------
    def alertas(self):
        print("\n=== ALERTAS ===")
        hoy = datetime.now().date()
        alertas = []

        for t in self.tareas:
            if t["completada"]:
                continue

            try:
                fecha = datetime.strptime(t["fecha"], "%Y-%m-%d").date()
                dias = (fecha - hoy).days
            except:
                continue

            if dias < 0:
                alertas.append(f"⚠️ VENCIDA: {t['titulo']} ({abs(dias)} días)")
            elif dias == 0:
                alertas.append(f"🔔 HOY: {t['titulo']} - {t['hora']}")
            elif dias == 1:
                alertas.append(f"📅 Mañana: {t['titulo']}")
            elif dias <= 3:
                alertas.append(f"📌 En {dias} días: {t['titulo']}")

        if alertas:
            for a in alertas:
                print(a)
        else:
            print("No hay alertas.")

    # ------------------------------
    #  FESTIVOS
    # ------------------------------
    def festivos(self):
        print("\n=== DÍAS FESTIVOS 2025 ===")
        lista = [
            "01 Ene - Año Nuevo",
            "03 Feb - Constitución",
            "17 Mar - Natalicio de Benito Juárez",
            "01 May - Día del Trabajo",
            "16 Sep - Independencia",
            "17 Nov - Revolución Mexicana",
            "25 Dic - Navidad"
        ]
        for f in lista:
            print("🎉", f)

    # ------------------------------
    #  MENÚ PRINCIPAL
    # ------------------------------
    def menu(self):
        while True:
            print("\n" + "="*45)
            print("📅 AGENDA SIMPLIFICADA")
            print("="*45)
            print("1. Ver tareas pendientes")
            print("2. Agregar tarea")
            print("3. Completar tarea")
            print("4. Eliminar tarea")
            print("5. Ordenar tareas")
            print("6. Ver alertas")
            print("7. Días festivos")
            print("0. Salir")
            print("="*45)

            op = input("\nElige opción: ")

            match op:
                case "1": self.tareas_pendientes()
                case "2": self.agregar()
                case "3": self.completar()
                case "4": self.eliminar()
                case "5": self.ordenar()
                case "6": self.alertas()
                case "7": self.festivos()
                case "0":
                    print("Adiós 👋")
                    break
                case _:
                    print("❌ Opción inválida")

            input("\nPresiona Enter para continuar...")

# Ejecutar
if __name__ == "__main__":
    CalendarioAgenda().menu()
