from rich.console import Console
import config.Variables_Horno.horno_config as vhorno
from utils.perturbador import perturbacion_total, get_ruido, set_error
import utils.funciones_auxiliares.alarma as func
from config.Variables_Horno.horno_config import error_oscilante

console = Console()
def adicionar_error():
    console.print("[cyan]Digite 1 para agregar inpulso de error (0 para quitar error)[/cyan]")
    if console.input("\n[bold red] Presione ENTER para salvar...[/bold red]") == "1":
        vhorno.flag_error = True
    else:
        vhorno.flag_error = False 
        
def adicionar_error_oscilante():
    console.print("[cyan]Digite 1 para agregar oscilante (0 para quitar error)[/cyan]")
    if console.input("\n[bold red] Presione ENTER para salvar...[/bold red]") == "1":
        vhorno.error_oscilante = True
    else:
        vhorno.error_oscilante = False 
def set_error(t):
    vhorno.delta_T, hay_impulso = perturbacion_total(t, probabilidad=0.02, duracion=3, magnitud=80)
    func.alarma_impulso(hay_impulso)
    
def construir_error(t, T):
    # Error base = diferencia entre referencia y temperatura real
    error = vhorno.T_SET - T
    if vhorno.error_oscilante:
        error += get_ruido(t)

    # Opción 4: impulso probabilístico (sólo si está activado en el menú)
    if vhorno.flag_error:
        vhorno.delta_T, hay_impulso = perturbacion_total(
            t, probabilidad=0.02, duracion=3, magnitud=80
        )
        func.alarma_impulso(hay_impulso)  
        error += vhorno.delta_T

    return error
