# ================================
# PARÁMETROS DEL CONTROLADOR PID
# ================================
fig = None
ax = None
linea = None
flag = True

restringir_integral = 0.85
error_prev = 0.0
integral = 0.0
derivada = 0.0
proporcional = 0.0
KP = 35              # Ganancia proporcional
KI = 10               # Ganancia             (0.3)
KD = 2