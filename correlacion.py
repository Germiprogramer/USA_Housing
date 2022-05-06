from classes.estadisticos import *
from classes.graficos import *
import matplotlib.pyplot as plt

casas = pd.read_csv("USA_Housing.csv")
casas.rename(columns = {'Avg. Area Income': 'Ingresos', 'Avg. Area House Age': 'Edad', 'Avg. Area Number of Rooms': 'Salas', 'Avg. Area Number of Bedrooms': 'Dormitorios', 'Area Population': 'Area', 'Price': 'Precio', 'Address': 'Direccion'}, inplace = True)

#Eliminamos los valores del dataset que no nos interesan para realizar la correlación
casas_filtrado=casas.drop(["Ingresos", "Edad", "Area", 'Direccion'],axis=1)

print("Seguidamente, se procederá a analizar la relación del número de habitaciones, dormitorios y el precio de la casa.")
print(casas_filtrado,"\n")

#Realizamos la correlación

print("La gráfica de la correlación entre las distintas columnas es la siguiente: ")
df_corr = casas_filtrado.corr()
print(df_corr, "\n")
