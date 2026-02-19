import matplotlib.pyplot as plt  
import time
from rich.live import Live 
import config.Variables_Horno.horno_config as vhorno

import config.Variables_Pid.pid_config as vpid
from utils.potencia_electrica.angulo_conduccion import  u_a_angulo_conduccion
import visualizacion.imagen_termica as imag_horno
import visualizacion.grafico_pid as imag_pid
from modelo import pid, horno
from visualizacion import grafico_pid
from visualizacion.tabla_live import generar_tabla
from visualizacion import imagen_termica
from utils.funciones_error.errores import construir_error
# =============================================================================#
#                             BUCLE PRINCIPAL                                  #
# =============================================================================#

def calcular_y_actualizar_pid(error):
    u, vpid.integral, vpid.error_prev, vpid.derivada, vpid.proporcional = pid.calcular_pid(
        error, vpid.error_prev, vpid.integral
    )
    return u


def simular_horno(T, u):
    return horno.simular_horno(T, u)


def actualizar_historiales(t, T, error, max_muestras):
    vhorno.tiempos.append(t)
    vhorno.temperaturas.append(T)
    vhorno.errores.append(error)

    exceso = len(vhorno.tiempos) - max_muestras
    if exceso > 0:
        del vhorno.tiempos[:exceso]
        del vhorno.temperaturas[:exceso]
        del vhorno.errores[:exceso]


def preparar_tabla(t, T, u, error):
    acciones = {"P": vpid.proporcional, "I": vpid.integral, "D": vpid.derivada}
    return generar_tabla(
        t, T, vhorno.T_SET, u, error,
        pid={"kp": vpid.KP, "ki": vpid.KI, "kd": vpid.KD},
        horno={"B": vhorno.B, "tau": vhorno.TAU, "T_amb": vhorno.T_AMB, "dt": vhorno.DT},
        acciones=acciones
      )


def pintar(T):
    imag_pid.call_grafica_pid(vhorno.tiempos, vhorno.temperaturas, vhorno.errores)
    imag_horno.call_imagen_termica(T)


def dormir_resto(start_time):
    elapsed = time.monotonic() - start_time
    time.sleep(max(0.0, vhorno.DT - elapsed))


def simular():
    print("Iniciando simulación térmica con PID. Presiona Ctrl+C para detener.\n")
    T = vhorno.T_AMB
    t = 0.0
    MAX_MUESTRAS = 5000

    try:
        with Live(screen=True, refresh_per_second=4) as live:
            while True:
                start_time = time.monotonic()
                error = construir_error(t, T)
                u = calcular_y_actualizar_pid(error)
                T = simular_horno(T, u)
                actualizar_historiales(t, T, error, MAX_MUESTRAS)
                tabla = preparar_tabla(t, T, u, error)
                live.update(tabla)
                pintar(T)
                t += vhorno.DT
                dormir_resto(start_time)

    except KeyboardInterrupt:
        print("\nSimulación detenida por el usuario.")
        plt.close('all')
        grafico_pid.fig = None
        grafico_pid.ax = None
        grafico_pid.linea = None
        grafico_pid.flag = True
        imagen_termica.fig_imagen = None
        imagen_termica.ax_imagen = None
        imagen_termica.flag_imagen = True
        imagen_termica._historial_colores = []

        # limpiar historiales
        vhorno.tiempos.clear()
        vhorno.temperaturas.clear()
        vhorno.errores.clear()
        plt.ioff()
        plt.show()

  
