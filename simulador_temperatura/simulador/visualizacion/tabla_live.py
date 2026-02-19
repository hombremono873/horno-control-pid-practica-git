from rich.console import Console, Group
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
import config.Variables_Pid.pid_config as vpid
console = Console()

"""
    Genera un panel Rich con:
    - Tabla de valores dinámicos en tiempo real
    - Tabla de configuración actual de PID y horno
    - Tabla de acciones individuales PID (P, I, D)
    - Mensaje de advertencia
    """
def generar_tabla(t, T, T_set, u, error, pid, horno, acciones):
    def construir_tabla_estado():
        tabla = Table(expand=True)
        tabla.add_column("Tiempo (s)", justify="right")
        tabla.add_column("Temperatura (°C)", justify="right")
        tabla.add_column("Setpoint (°C)", justify="right")
        tabla.add_column("u(t)", justify="right")
        tabla.add_column("Error", justify="right")
        tabla.add_row(
             str(t),
             f"{T:.2f}",
             f"{T_set:.2f}",
             f"{u:.3f}",
             f"{error:.2f}",
        )
        return tabla

    def construir_tabla_config():
        tabla = Table(title="Configuración PID y Horno", expand=True)
        tabla.add_column("Parámetro", style="bold cyan")
        tabla.add_column("Valor", justify="right")

        tabla.add_row("Kp", f"{pid.get('kp', 0.0):.2f}")
        tabla.add_row("Ki", f"{pid.get('ki', 0.0):.2f}")
        tabla.add_row("Kd", f"{pid.get('kd', 0.0):.2f}")
        tabla.add_row("B (Ganancia térmica)", f"{horno.get('B', 0.0):.2f}")
        tabla.add_row("Tau (Constante tiempo)", f"{horno.get('tau', 0.0):.2f}")
        tabla.add_row("Restricción Integral", f"{vpid.restringir_integral:.2f}")
        tabla.add_row("T_amb (°C)", f"{horno.get('T_amb', 0.0):.1f}")
        tabla.add_row("dt (s)", f"{horno.get('dt', 0.1):.2f}")
       
        return tabla

    def construir_tabla_acciones():
        tabla = Table(title="Acciones individuales del PID", expand=True)
        tabla.add_column("Acción", style="bold green")
        tabla.add_column("Valor", justify="right")
        tabla.add_row("Proporcional (P)", f"{acciones.get('P', 0.0):.3f}")
        tabla.add_row("Integral (I)", f"{acciones.get('I', 0.0):.3f}")
        tabla.add_row("Derivativa (D)", f"{acciones.get('D', 0.0):.3f}")
        return tabla

    mensaje = Text(
        "Para parar, cierra la ventana de la gráfica antes de presionar Ctrl+C",
        style="bold red"
    )

    grupo = Group(
        Align.center(construir_tabla_estado()),
        Align.center(construir_tabla_acciones()),
        Align.center(construir_tabla_config()),
        Align.center(mensaje)
    )

    ancho_terminal = console.size.width
    ancho_deseado = max(40, int(ancho_terminal * 0.9))

    return Panel(
        grupo,
        title="[italic cyan]Simulación Térmica del Horno (Modo Consola)[/italic cyan]",
        width=ancho_deseado,
        padding=(1, 2),
        border_style="bright_blue"
    )
    
    
    


    

