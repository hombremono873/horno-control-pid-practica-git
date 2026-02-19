import os
import time
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.live import Live
import config.Variables_Horno.horno_config as var

console = Console()

def construir_panel_horno(ancho):
    width = min(ancho - 10, 80)
    texto = Text()
    texto.append("CONFIGURACIÓN DEL HORNO\n\n", style="bold cyan")
    texto.append("T_AMB : Temperatura ambiente (°C)\n", style="bold")
    texto.append("T_SET : Temperatura objetivo (°C)\n", style="bold")
    texto.append("B     : Ganancia térmica (°C/u control)\n", style="bold")
    texto.append("TAU   : Constante de tiempo (s)\n", style="bold")
    texto.append("DT    : Paso de simulación (s)\n\n", style="bold")
    texto.append("[bold red] Presione ENTER para ingresar valores...[/bold red]")

    return Panel(
        Align.left(texto),
        title="[bold cyan] CONFIGURAR HORNO [/bold cyan]",
        border_style="bright_blue",
        padding=(1, 2),
        width=width
    )

def pedir_valores_horno():
    os.system("cls" if os.name == "nt" else "clear")
    ancho_anterior = console.size.width

    try:
        with Live(construir_panel_horno(ancho_anterior), screen=True, refresh_per_second=4) as live:
            while True:
                ancho_actual = console.size.width
                if ancho_actual != ancho_anterior:
                    live.update(construir_panel_horno(ancho_actual))
                    ancho_anterior = ancho_actual

                if console.input("\n[bold red] Presione ENTER para continuar...[/bold red]") == "":
                    break
                time.sleep(0.02)
    except KeyboardInterrupt:
        console.clear()
        console.print("[bold red] Panel cancelado por el usuario.[/bold red]")
        return

    os.system("cls" if os.name == "nt" else "clear")

    # Captura segura de valores
    try:
        var.T_AMB = float(Prompt.ask("[bold yellow]Temperatura ambiente (T_AMB)[/bold yellow]"))
        var.T_SET = float(Prompt.ask("[bold yellow]Setpoint de temperatura (T_SET)[/bold yellow]"))
        var.B     = float(Prompt.ask("[bold yellow]Ganancia térmica (B)[/bold yellow]"))
        var.TAU   = float(Prompt.ask("[bold yellow]Constante de tiempo (TAU)[/bold yellow]"))
        var.DT    = float(Prompt.ask("[bold yellow]Paso de tiempo (DT)[/bold yellow]"))

        console.print("\n[bold green] Parámetros del horno actualizados:[/bold green]")
        console.print(f"[cyan]  T_AMB = {var.T_AMB} °C[/cyan]")
        console.print(f"[cyan]  T_SET = {var.T_SET} °C[/cyan]")
        console.print(f"[cyan]  B     = {var.B} °C/u[/cyan]")
        console.print(f"[cyan]  TAU   = {var.TAU} s[/cyan]")
        console.print(f"[cyan]  DT    = {var.DT} s[/cyan]")

    except ValueError:
        console.print("\n[bold red] Error: solo se permiten números reales.[/bold red]")
