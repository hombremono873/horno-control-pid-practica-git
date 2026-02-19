import config.Variables_Pid.pid_config as vpid
from rich.console import Console
from rich.prompt import Prompt

from rich.console import Console
from rich.prompt import Prompt
import config.Variables_Pid.pid_config as vpid

def acotar_integral():
    console = Console()
    while True:
        try:
            valor = float(Prompt.ask("[bold yellow] Restrinja el efecto de la integral [0 a 1][/bold yellow]"))
            if 0 <= valor <= 1:
                vpid.restringir_integral = valor
                break
            else:
                console.print("[bold red] Error: el valor debe estar entre 0 y 1.[/bold red]")
        except ValueError:
            console.print("[bold red] Error: solo se permiten números reales.[/bold red]")
 
def minimizar_integral(integral):
    return max(min(integral, integral*vpid.restringir_integral), -integral*vpid.restringir_integral)
    
    