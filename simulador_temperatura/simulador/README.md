# Simulador de Horno Eléctrico con Control PID

**Universidad de Antioquia – Facultad de Ingeniería**  
**Autor:** Omar Alberto Torres  
**Docente:** Yony Ceballos  
**Fecha:** 2025  

---

## 📘 Contexto del Proyecto

Este trabajo corresponde a la implementación de un **simulador computacional de un horno eléctrico con regulación PID**. El objetivo es integrar conceptos de **transferencia de calor, modelado matemático y control de procesos**, aplicando **métodos numéricos** como la integración de Euler.  

El proyecto permite analizar de forma numérica y visual el comportamiento dinámico del sistema, además de explorar la robustez del controlador PID frente a perturbaciones externas.  

---

## 📂 Estructura del Proyecto

El proyecto está compuesto por:

- **Código fuente en Python** (desarrollado en *Visual Studio Code*).  
- **Archivo `requirements.txt`**: contiene todas las librerías necesarias para crear un entorno virtual y ejecutar el simulador.  
- **Ejecutable `main.exe`**: compilación del proyecto que permite al docente ejecutar la aplicación directamente, sin necesidad de instalar dependencias.  

---

## ⚙️ Dependencias del Proyecto

El entorno de ejecución requiere las siguientes librerías principales (incluidas en `requirements.txt`):  

- `numpy`  
- `matplotlib`  
- `rich`  
- `pillow`  
- `python-dateutil`  

Para instalar las dependencias en un entorno virtual:

```bash
pip install -r requirements.txt

## 🚀 Ejecución del Proyecto

### Opción 1: Ejecutar desde código fuente

1. Crear un entorno virtual en Python:  
   ```bash
   python -m venv venv
## 🔑 Activar el entorno virtual

En **Windows**:  
```bash
venv\Scripts\activate

## ⚙️ Explicación compacta del código

- **Modelo térmico**  
  El horno se representa como un **sistema de primer orden**, aplicando la **Ley de Fourier** (conducción) y la **Ley de Enfriamiento de Newton** (pérdidas al ambiente).  
  La temperatura se actualiza en cada paso de tiempo mediante el **método de Euler**, lo que permite aproximar la evolución dinámica del sistema.

- **Algoritmo PID**  
  El controlador PID ajusta la energía suministrada al horno según:  
  - **Proporcional (Kp):** responde al error instantáneo.  
  - **Integral (Ki):** corrige el error acumulado en el tiempo.  
  - **Derivativa (Kd):** anticipa cambios bruscos y estabiliza la respuesta.  

  La combinación de estas tres acciones permite que la temperatura alcance el setpoint con **mínimo error en estado estacionario**, controlando el **sobreimpulso** y la **estabilidad** incluso bajo perturbaciones externas.

SIMULADOR
├── build/
├── config/
├── dist/
├── modelo/
├── utils/
├── visualizacion/
├── main.py
├── main.spec
├── README.md
└── requirements.txt



