import datetime
import time
# Obtener la hora actual como una tupla (hora, minuto, segundo)
hora_actual = time.localtime().tm_hour
minuto_actual = time.localtime().tm_min
segundo_actual = time.localtime().tm_sec

print(f"Hora actual: {hora_actual:02d}:{minuto_actual:02d}:{segundo_actual:02d}")