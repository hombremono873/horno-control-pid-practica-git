
import random

def suavizar_u(u_real: float, intensidad: float = 0.1) -> float:
   
    u_real = max(0.0, min(1.0, u_real))  # asegurar límite
    delta = intensidad * u_real
    u_modulado = random.uniform(u_real - delta, u_real + delta)
    return max(0.0, min(1.0, u_modulado))

def u_a_angulo_conduccion(u: float, theta_min: float = 10.0, theta_max: float = 170.0, intensidad: float = 0.1) -> float:
    u_suavizado = suavizar_u(u, intensidad)
    return theta_max - u_suavizado * (theta_max - theta_min)
    