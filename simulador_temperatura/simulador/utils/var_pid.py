import os
import time
from rich.live import Live
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
import config.Variables_Pid.pid_config as var

console = Console()

def construir_panel_pid(ancho):
    width = min(ancho - 10, 80)

    texto = Text()
    texto.append(" CONFIGURACIÓN DEL CONTROLADOR PID\n\n", style="bold cyan")
    texto.append("Kp : Constante proporcional\n", style="bold")
    texto.append("Ki : Constante integral\n", style="bold")
    texto.append("Kd : Constante derivativa\n\n", style="bold")
    texto.append("[bold red]↩ Presione ENTER para ingresar valores...[/bold red]")

    return Panel(
        Align.left(texto),
        title="[bold cyan] CONFIGURAR PID [/bold cyan]",
        border_style="bright_blue",
        padding=(1, 2),
        width=width
    )

def pedir_valores_pid():
    os.system("cls" if os.name == "nt" else "clear")
    ancho_anterior = console.size.width

    #  Mostrar panel redimensionable
    try:
        with Live(construir_panel_pid(ancho_anterior), screen=True, refresh_per_second=4) as live:
            while True:
                ancho_actual = console.size.width
                if ancho_actual != ancho_anterior:
                    live.update(construir_panel_pid(ancho_actual))
                    ancho_anterior = ancho_actual

                if console.input("\n[bold yellow]↩ Presione ENTER para continuar...[/bold yellow]") == "":
                    break
                time.sleep(0.02)

    except KeyboardInterrupt:
        console.clear()
        console.print("[bold red] Panel cancelado por el usuario.[/bold red]")
        return

    os.system("cls" if os.name == "nt" else "clear")

    #  Captura de entradas con validación
    try:
        var.KP = float(Prompt.ask("[bold yellow]Ingrese el valor de Kp[/bold yellow]"))
        var.KI = float(Prompt.ask("[bold yellow]Ingrese el valor de Ki[/bold yellow]"))
        var.KD = float(Prompt.ask("[bold yellow]Ingrese el valor de Kd[/bold yellow]"))

        console.print("\n[bold green] PID actualizado correctamente:[/bold green]")
        console.print(f"[cyan]  Kp = {var.KP}[/cyan]")
        console.print(f"[cyan]  Ki = {var.KI}[/cyan]")
        console.print(f"[cyan]  Kd = {var.KD}[/cyan]")

    except ValueError:
        console.print("\n[bold red] Error: solo se permiten números reales.[/bold red]")

    except KeyboardInterrupt:
        console.clear()
        console.print("[bold red] Entrada cancelada por el usuario.[/bold red]")
