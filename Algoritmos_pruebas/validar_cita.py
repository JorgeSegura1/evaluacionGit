def validar_cita(nombre_paciente, fecha, estado):
    if not nombre_paciente or not fecha:
        return "Datos incompletos"

    if estado.lower() == "confirmada":
        return f"Cita confirmada para {nombre_paciente} el {fecha}"

    return "La cita no está confirmada"


print(validar_cita("Jorge Segura", "2026-09-25", "confirmada"))