import tkinter as tk
import matplotlib.pyplot as plt

# cogemos que un robot aspirador moderno tiene una velocidad media de 20 cm/s (0.2 m/s)
velocidad_media = 0.2

def calcular_area_disponible():
    try:

        largo_habitacion = float(entry_largo_habitacion.get())
        ancho_habitacion = float(entry_ancho_habitacion.get())


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


def dibujar_areas(largo_habitacion, ancho_habitacion, largo_area_no_utilizable, ancho_area_no_utilizable):

    x_no_utilizable = (ancho_habitacion - ancho_area_no_utilizable) / 2
    y_no_utilizable = (largo_habitacion - largo_area_no_utilizable) / 2

    plt.figure()
    plt.gca().add_patch(plt.Rectangle((0, 0), ancho_habitacion, largo_habitacion, color='blue', alpha=0.5))
    plt.gca().add_patch(plt.Rectangle((x_no_utilizable, y_no_utilizable), ancho_area_no_utilizable, largo_area_no_utilizable, color='red', alpha=0.5))


    plt.xlim(0, ancho_habitacion)
    plt.ylim(0, largo_habitacion)


    plt.grid(True)
    plt.title('Áreas habitación y mueble')

    plt.show()


ventana = tk.Tk()
ventana.title("Calculadora de Área a limpiar")


label_largo_habitacion = tk.Label(ventana, text="Largo de la habitación (cm):")
label_largo_habitacion.grid(row=0, column=0, padx=5, pady=5)
entry_largo_habitacion = tk.Entry(ventana)
entry_largo_habitacion.grid(row=0, column=1, padx=5, pady=5)

label_ancho_habitacion = tk.Label(ventana, text="Ancho de la habitación (cm):")
label_ancho_habitacion.grid(row=1, column=0, padx=5, pady=5)
entry_ancho_habitacion = tk.Entry(ventana)
entry_ancho_habitacion.grid(row=1, column=1, padx=5, pady=5)


