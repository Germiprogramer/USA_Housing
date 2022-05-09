from classes.estadisticos import *
from classes.graficos import *
import matplotlib.pyplot as plt

casas = pd.read_csv("USA_Housing.csv")

# ANALISIS DEL DATASET
print("ANÁLISIS DEL DATASET")

# Sustituimos el nombre de los valores a español
casas.rename(columns = {'Avg. Area Income': 'Ingresos', 'Avg. Area House Age': 'Edad', 'Avg. Area Number of Rooms': 'Salas', 'Avg. Area Number of Bedrooms': 'Dormitorios', 'Area Population': 'Area', 'Price': 'Precio', 'Address': 'Direccion'}, inplace = True)

# LIMPIEZA DEL DATASET. Eliminamos las filas que no tengan valor
def nec_limp(dataset, columna):
    lista = list(dataset[columna])
    for i in range(len(lista)):
        if lista[i] == "":
            print("se necesita una limpieza de datos")
            break
        else:
            pass

nec_limp(casas, "Precio")



casas = casas.dropna(subset=["Precio"])


print("El dataset es el siguiente: ")
print(casas)

#Numero de filas
filas = Filas(casas)
filas.calculo()

#Numero de columnas
columnas = Columnas(casas)
columnas.calculo()

#Valores maximos
max = Maximos(casas, "Precio")
max.calculo()
#Valores minimos
min = Minimos(casas, "Precio")
min.calculo()

#Media
media_HP = Media(casas, "Precio")
media_HP.calculo()

#Mediana
mediana_HP = Mediana(casas, "Precio")
mediana_HP.calculo()

#Moda
moda_HP = Moda(casas, "Precio")
moda_HP.calculo()

#Desviación típica
desv_HP = Desviacion_tipica(casas, "Precio")
desv_HP.calculo()

#q1
q1 = Q1(casas, "Precio")
q1.calculo()


#q3
q3 = Q3(casas, "Precio")
q3.calculo()

#rango intercuartilico
a = casas["Precio"].quantile(0.25)
b = casas["Precio"].quantile(0.75)
rango_int = b - a
print("El rango intercuartilico es {}".format(rango_int))

#grafico
grafico(casas["Precio"], "hist", "Precio de las casas", "histogramaprecio")


