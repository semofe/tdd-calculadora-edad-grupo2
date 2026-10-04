def calcular_edad(fecha_nacimiento, fecha_actual):
    aun_no_cumple = (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day)
    return (fecha_actual.year - fecha_nacimiento.year) - int(aun_no_cumple)