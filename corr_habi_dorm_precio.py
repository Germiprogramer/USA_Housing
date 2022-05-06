from classes.estadisticos import *
from classes.graficos import *
import matplotlib.pyplot as plt
import seaborn as sns

casas = pd.read_csv("USA_Housing.csv")
casas.rename(columns = {'Avg. Area Income': 'Ingresos', 'Avg. Area House Age': 'Edad', 'Avg. Area Number of Rooms': 'Salas', 'Avg. Area Number of Bedrooms': 'Dormitorios', 'Area Population': 'Area', 'Price': 'Precio', 'Address': 'Direccion'}, inplace = True)

corr_habi_dorm_precio = Correlacion(casas, ["Ingresos", "Edad", "Area", 'Direccion'], "corr_habi_dorm_precio")
corr_habi_dorm_precio.calculo()