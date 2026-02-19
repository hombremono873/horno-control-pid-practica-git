import config.Variables_Horno.horno_config as var
import math

# Modelo térmico de primer orden:
# dT/dt = -(1/TAU)*(T - T_AMB) + (K/TAU)*u
# donde B = K/TAU

def simular_horno(T_actual, u):
    try:
        TAU = var.TAU
        if TAU == 0:
            TAU = 1e-6   # evita división por cero

        dT = (1 / TAU) * (var.T_AMB - T_actual) + var.B * u
        T_nuevo = T_actual + var.DT * dT

        if math.isnan(T_nuevo) or math.isinf(T_nuevo):
            T_nuevo = T_actual

    except Exception:
        T_nuevo = T_actual

    return T_nuevo

# metodo heun
def simular_horno1(T_actual, u):
    try:
        TAU = var.TAU
        if TAU == 0:
            TAU = 1e-6   # evita división por cero
        DT = var.DT
        T_AMB = var.T_AMB
        B = var.B

        # --- Paso 1: pendiente inicial ---
        k1 = (1 / TAU) * (T_AMB - T_actual) + B * u

        # --- Paso 2: valor predicho ---
        T_pred = T_actual + DT * k1

        # --- Paso 3: pendiente final ---
        k2 = (1 / TAU) * (T_AMB - T_pred) + B * u

        # --- Paso 4: corrección (promedio de pendientes) ---
        T_nuevo = T_actual + (DT / 2) * (k1 + k2)

        # --- Validación numérica ---
        if math.isnan(T_nuevo) or math.isinf(T_nuevo):
            T_nuevo = T_actual

    except Exception:
        T_nuevo = T_actual

    return T_nuevo
