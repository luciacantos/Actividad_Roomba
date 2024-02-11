import tkinter as tk
import matplotlib.pyplot as plt

# cogemos que un robot aspirador moderno tiene una velocidad media de 20 cm/s (0.2 m/s)
velocidad_media = 0.2

def calcular_area_disponible():
    try:

        largo_habitacion = float("".get())
        ancho_habitacion = float("".get())


        largo_area_no_utilizable = float("".get())
        ancho_area_no_utilizable = float("".get())

        area_habitacion = largo_habitacion * ancho_habitacion
        area_no_utilizable = largo_area_no_utilizable * ancho_area_no_utilizable
        area_disponible = area_habitacion - area_no_utilizable

        area_disponible = area_disponible / 10000 # m^2
        area_no_utilizable = area_no_utilizable / 10000 # m^2

        tiempo = area_disponible / velocidad_media
        tiempo_minutos = tiempo / 60


        dibujar_areas(largo_habitacion, ancho_habitacion, largo_area_no_utilizable, ancho_area_no_utilizable)

    except ValueError as e:
        resultado_area_disponible.config(text=f"Error: {e}")



