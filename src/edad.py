from datetime import date

MENSAJE_FECHA_FUTURA = "La fecha de nacimiento no puede ser posterior a la fecha actual"

def _validar_fechas(fecha_nacimiento: date, fecha_actual: date) -> None:
    if fecha_nacimiento > fecha_actual:
        raise ValueError(MENSAJE_FECHA_FUTURA)

def _ya_cumplio_anios(fecha_nacimiento: date, fecha_actual: date) -> bool:
    return (fecha_actual.month, fecha_actual.day) >= (fecha_nacimiento.month, fecha_nacimiento.day)

def calcular_edad(fecha_nacimiento: date, fecha_actual: date) -> int:
    _validar_fechas(fecha_nacimiento, fecha_actual)
    diferencia_anios = fecha_actual.year - fecha_nacimiento.year
    ajuste = 0 if _ya_cumplio_anios(fecha_nacimiento, fecha_actual) else 1
    return diferencia_anios - ajuste