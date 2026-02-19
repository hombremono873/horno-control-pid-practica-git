from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align
from rich.live import Live 
import time
console = Console()
from datetime import date
def pantalla_bienvenida():
    console.clear()
    hoy = date.today().strftime("%d/%m/%Y")

    texto = (
        "[bold white]UNIVERSIDAD DE ANTIOQUIA[/bold white]\n\n"
        "[bold cyan]SIMULADOR VIRTUAL DE HORNO CON CONTROL PID[/bold cyan]\n\n"
        f"Fecha: [white]{hoy}[/white]\n"
        "Asignatura: [white]Métodos Numéricos[/white]\n"
        "Autor: [white]Omar Alberto Torres[/white]\n"
        "Profesor: [white]Yony Ceballos[/white]\n"
        "Modo: [white]Consola[/white]"
    )

    def construir_layout_bienvenida() -> Layout:
        layout = Layout(name="root")
        panel = Panel(
            texto,
            title="[bold cyan]Bienvenido[/bold cyan]",
            subtitle="[bold cyan]Presione ENTER para continuar[/bold cyan]",
            border_style="bright_blue",
            padding=(1, 4),
            width=max(40, int(console.size.width * 0.6))
        )
        layout.update(Align.center(panel, vertical="middle"))
        return layout

    ancho_anterior = console.size.width
    layout = construir_layout_bienvenida()

    with Live(layout, refresh_per_second=4, screen=True) as live:
        while True:
            ancho_actual = console.size.width
            if ancho_actual != ancho_anterior:
                layout = construir_layout_bienvenida()
                live.update(layout)
                ancho_anterior = ancho_actual

            if console.input("") == "":
                break
            time.sleep(0.02)
