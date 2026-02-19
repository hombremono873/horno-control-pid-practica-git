
from utils.flujo import simular
from visualizacion.menu import mostrar_menu
from rich.console import Console
from utils.flujo import simular
from utils.var_pid import pedir_valores_pid
from utils.var_horno import pedir_valores_horno
#import config.Variables_Horno.horno_config as vhorno
from utils.funciones_auxiliares.calculo_windout import acotar_integral
import time
#from rich.live import Live 
from visualizacion.pantalla_vienvenida import pantalla
from utils.funciones_error.errores import adicionar_error, adicionar_error_oscilante

# ====================================================================================
#                         EJECUCIÓN DEL PROGRAMA
# =====================================================================================
console = Console()
             
def main():
    pantalla.pantalla_bienvenida()
    console.clear()
    while True:
        console.clear()
        opcion = mostrar_menu()
        
        if opcion == "1":
             console.clear() 
             pedir_valores_pid()
           
        elif opcion == "2":
            console.clear() 
            pedir_valores_horno()
            console.clear() 
        elif opcion == "3":
            console.clear()
            adicionar_error_oscilante()
        elif opcion == "4":
             console.clear()
             adicionar_error()
        elif opcion == "5":
            console.clear() 
            acotar_integral()  
            console.clear() 
        elif opcion == "6":
             simular()
             console.clear()
        elif opcion == "7" :
             console.clear()
             console.print("[bold red] Saliendo del simulador...[/bold red]")
             break
        else:
            console.print("[red] Opción inválida[/red]")
            time.sleep(2)

if __name__ == "__main__":
    main()
