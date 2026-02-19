# ================================
# PARÁMETROS FÍSICOS DEL SISTEMA
# ================================

T_AMB = 30.0           # Temperatura ambiente (°C)
T_SET = 1000.0         # Setpoint de temperatura (°C)  80
B = 100                 # Ganancia térmica (°C por unidad de control) (0.22)
TAU = 3000              # Constante de tiempo del horno (s)  (3600.0)
DT = 0.1               # Paso de simulación (s)
tiempos = []
temperaturas = []
errores = [] 
delta_T =0
flag_error = False
error_oscilante = False
