from classes.estadisticos import *
from classes.graficos import *
import matplotlib.pyplot as plt
import seaborn as sns

casas = pd.read_csv("USA_Housing.csv")
casas.rename(columns = {'Avg. Area Income': 'Ingresos', 'Avg. Area House Age': 'Edad', 'Avg. Area Number of Rooms': 'Salas', 'Avg. Area Number of Bedrooms': 'Dormitorios', 'Area Population': 'Area', 'Price': 'Precio', 'Address': 'Direccion'}, inplace = True)

corr_precio_ingr = Correlacion(casas, ["Edad", "Area", 'Direccion', "Salas", "Dormitorios"])
corr_precio_ingr.calculo()