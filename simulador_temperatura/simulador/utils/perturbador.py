# perturbador.py
import math
import random
from random import uniform
from random import random
from math import sin
import config.Variables_Horno.horno_config as vhorno
import utils.funciones_auxiliares.alarma as func

def impulso_probabilistico(t, probabilidad, duracion, magnitud):
    if not hasattr(impulso_probabilistico, "activo"):
        impulso_probabilistico.activo = False
        impulso_probabilistico.t_inicio = 0
        impulso_probabilistico.signo = 1  # nuevo atributo para alternar signo

    if impulso_probabilistico.activo:
        if t < impulso_probabilistico.t_inicio + duracion:
            # Alternar el signo en cada ciclo
            impulso_probabilistico.signo *= -1
            return impulso_probabilistico.signo * abs(magnitud), True
        else:
            impulso_probabilistico.activo = False
            return 0, False

    if random() < probabilidad:
        impulso_probabilistico.activo = True
        impulso_probabilistico.t_inicio = t
        impulso_probabilistico.signo = -1  # empieza en negativo al activarse
        return impulso_probabilistico.signo * abs(magnitud), True

    return 0, False

# Esta función devuelve la perturbación total del sistema en un instante t.
# Incluye:
# - ruido aleatorio
# - perturbación senoidal suave
# - impulso térmico probabilístico

def perturbacion_total(t, probabilidad=0.05, duracion=3, magnitud=-40):
    ruido = uniform(-0.5, 1.5)
    senoide = 20 * sin(0.05 * t)
    impulso, activo = impulso_probabilistico(t, probabilidad, duracion, magnitud)
    total = ruido + senoide + impulso
    return total, activo

# ================================
# FUNCIÓN DE RUIDO leve
# ================================

def get_ruido(t):
    #ruido = random.uniform(-0.5, 1.5)
    ruido = uniform(-0.5, 1.5)
    perturbacion = 20 * math.sin(0.05 * t)
    return perturbacion + ruido
def set_error(t):
    vhorno.delta_T, hay_impulso = perturbacion_total(t, probabilidad=0.02, duracion=3, magnitud=80)
    func.alarma_impulso(hay_impulso)    

