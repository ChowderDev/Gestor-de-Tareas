import json
import os

TAREAS_FILE = "tareas.json"

# Cargar tareas desde el archivo JSON
def cargar_tareas():
    if not os.path.exists(TAREAS_FILE):
        return []
    with open(TAREAS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

# Guardar tareas en el archivo JSON
def guardar_tareas(tareas):
    with open(TAREAS_FILE, "w", encoding="utf-8") as file:
        json.dump(tareas, file, indent=4)

# Mostrar lista de tareas
def listar_tareas(tareas):
    if not tareas:
        print("📭 No hay tareas pendientes.")
        return
    print("\n📌 Lista de Tareas:")
    for i, tarea in enumerate(tareas):
        estado = "✅" if tarea["completada"] else "❌"
        print(f"{i + 1}. {estado} {tarea['descripcion']}")

# Agregar una nueva tarea
def agregar_tarea(tareas):
    descripcion = input("📝 Ingresa la tarea: ")
    tareas.append({"descripcion": descripcion, "completada": False})
    guardar_tareas(tareas)
    print("✅ Tarea agregada con éxito.")

# Marcar una tarea como completada
def completar_tarea(tareas):
    listar_tareas(tareas)
    try:
        indice = int(input("📍 Ingresa el número de la tarea completada: ")) - 1
        if 0 <= indice < len(tareas):
            tareas[indice]["completada"] = True
            guardar_tareas(tareas)
            print("🎉 Tarea marcada como completada.")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Ingresa un número válido.")

# Eliminar una tarea
def eliminar_tarea(tareas):
    listar_tareas(tareas)
    try:
        indice = int(input("🗑 Ingresa el número de la tarea a eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            tareas.pop(indice)
            guardar_tareas(tareas)
            print("🗑 Tarea eliminada correctamente.")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Ingresa un número válido.")

# Menú principal
def menu():
    tareas = cargar_tareas()
    while True:
        print("\n📌 Gestor de Tareas")
        print("1️⃣ Ver tareas")
        print("2️⃣ Agregar tarea")
        print("3️⃣ Completar tarea")
        print("4️⃣ Eliminar tarea")
        print("5️⃣ Salir")
        
        opcion = input("👉 Selecciona una opción: ")

        if opcion == "1":
            listar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("👋 Saliendo del gestor de tareas.")
            break
        else:
            print("❌ Opción inválida, intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
