import config.Variables_Horno.horno_config as var_horno
import config.Variables_Pid.pid_config as var
import utils.funciones_auxiliares.calculo_windout as windout
import math

def escalar_u(u, u_max=20000.0):
    if u_max <= 0:
        raise ValueError("u_max debe ser mayor que cero")
    u_escalado = u / u_max
    return max(-1.0, min(1.0, u_escalado))
  
def calcular_pid(error, error_prev, integral):
    DT = var_horno.DT
    if DT == 0:
        DT = 1e-6   # protección mínima
        
    #integral += error * DT    #Metodo de euler o del rectangulo
    integral += 0.5 * (error + error_prev) * DT  #integral del trapecio
    
    derivada = (error - error_prev) / DT
    if integral >2000:
       integral = windout.minimizar_integral(integral)
       
    proporcional = var.KP * error
    u = proporcional + var.KI * integral + var.KD * derivada
    if math.isnan(u) or math.isinf(u):
        u = 0.0
    return escalar_u(u), integral, error, var.KD*derivada, proporcional
