from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align
from rich.live import Live
import time

console = Console()

def construir_layout(opciones: str) -> Layout:
    layout = Layout(name="root")

    panel_menu = Panel(
        opciones,
        title="[bold cyan]Simulador de Temperatura[/bold cyan]",
        subtitle="[bold cyan]Para entrada de datos pulse enter[/bold cyan]",
        border_style="bright_blue",
        padding=(1, 4),
        width=max(40, int(console.size.width * 0.6))
    )

    layout.update(Align.center(panel_menu, vertical="middle"))
    return layout

def mostrar_menu():
    opciones = (
        "[white]"
        "\n[bold white]UNIVERSIDAD DE ANTIOQUIA[/bold white]\n\n"
        "\n1. Configurar PID"
        "\n2. Configurar horno"
        "\n3. Adicionar error oscilante"
        "\n4. Adicionar error impulso"
        "\n5. Acotar rango de la integral"
        "\n6. Ejecutar simulación"
        "\n7. Salir"
        "\n"
        "\nPara entrada de datos pulse enter[/white]"
    )

    ancho_anterior = console.size.width
    layout = construir_layout(opciones)

    with Live(layout, refresh_per_second=4, screen=True) as live:
        while True:
            ancho_actual = console.size.width
            if ancho_actual != ancho_anterior:
                layout = construir_layout(opciones)
                live.update(layout)
                ancho_anterior = ancho_actual

            #time.sleep(0.1)
            # Salir del Live al presionar ENTER (como todas tus otras pantallas)
            if console.input("\n[bold yellow] ENTER para seleccionar una opción...[/bold yellow]") == "":
                break
            time.sleep(0.02)

    #console.clear()
    opcion = console.input("[bold cyan]Seleccione una opción ahora:[/bold cyan] ")
    return opcion

