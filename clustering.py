# El clustering consiste en la agrupación de datos. Para aplicarlo a nuestro trabajo, vamos a separar el dataset entre aquellas casas que son baratas y aquellas que son caras. Para ello, usaremos la media como marco de referencia.

from classes.estadisticos import *
from classes.graficos import *
import matplotlib.pyplot as plt
import numpy as np

casas = pd.read_csv("USA_Housing.csv")

casas.rename(columns = {'Avg. Area Income': 'Ingresos', 'Avg. Area House Age': 'Edad', 'Avg. Area Number of Rooms': 'Salas', 'Avg. Area Number of Bedrooms': 'Dormitorios', 'Area Population': 'Area', 'Price': 'Precio', 'Address': 'Direccion'}, inplace = True)

filtro = 1232072

casas_baratas =casas['Precio']<=filtro
positions = np.flatnonzero(casas_baratas)
filtered_df = casas_baratas.iloc[positions]

print(filtered_df)

#De esta forma, nos han quedado únicamente las casas cuyo precio es menos al precio medio.