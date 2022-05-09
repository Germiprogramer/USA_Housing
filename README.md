# USA_Housing

El link al repositorio es el siguiente: https://github.com/Germiprogramer/USA_Housing.git

# 0 - Análisis del EDA.

La primera parte del trabajo es realizar un análisis del dataset dado. Se ha elegido analizar el parámetro "precio", debido a que es el que tiene un mayor interés de cara a aquellos que estén interesados en las casas del archivo.

El análisis realizado por el programa es el siguiente:

    El numero de filas es: 5000
    
    El numero de columnas es: 7
    
    El valor máximo es: 2469065.5941747027
    
    El valor mínimo es: 15938.657923287848
    
    La media es: 1232072.654142357
    
    La mediana es: 1232669.3779657914
    
    La moda es:
    0       1.593866e+04
    1       3.114052e+04
    2       8.859177e+04
    3       1.430274e+05
    4       1.515271e+05
                ...
    4995    2.318286e+06
    4996    2.330290e+06
    4997    2.332111e+06
    4998    2.370231e+06
    4999    2.469066e+06
    Length: 5000, dtype: float64
    
    La desviación tipica es: 282275.20709891006
    
    El primer cuartil es: 997577.1350487601
    
    El tercer cuartil es: 1471210.2042115545
    
    El rango intercuartilico es 473633.0691627944   
    
Al no ser la desviación típica muy alta respecto a los valores, podemos considerar que la muestra está relativamente centrada.

# 1 - Grafique las variables implicadas de las maneras que crea oportunas.

Para un mayor entendimiento del dataset, se ha graficado el precio de las casas utilizando un histograma. Se ha decidido usar este tipo de gráfico debido a que se considera que es el más adecuado para mostrar la disponibilidad de las casas respecto a su precio.

Al ver el gráfico, podemos ver que la muestra de datos está bastante centrada, asemejándose a la campana de Gauss.

<img width="461" alt="2022-05-05 (3)" src="https://user-images.githubusercontent.com/91720991/167028240-2bbbbe1f-7671-480d-b649-886076f1b5f9.png">

# 2 - Identifique si es necesaria una limpieza de datos y/o completar valores perdidos.

Para la limpieza de datos, hemos usado la función dropna() de pandas. Al ser un dataset muy extenso, no podemos identificar a primera vista si hay huecos vacíos, por lo que usamos la función dropna() para eliminar aquellas filas que no tengan un valor para el precio. El código utilizado es el siguiente.

    casas = casas.dropna(subset=["Precio"])

# 3 - Obtenga las correlaciones entre variables y analice si se pueden observar algunas relaciones interesantes.

Se ha realizado la correlacción entre el número de salas, dormitorios y el precio de la casa. Esto se ha hecho para intentar demostrar que cuanto más grande sea la casa, mayor será el precio. Sin embargo, tal y como se mestra en el siguiente gráfico, los resultados no han sido los esperados; siendo el coeficiente de variación de Pearson relativamente bajo.

<img width="484" alt="2022-05-06 (2)" src="https://user-images.githubusercontent.com/91720991/167197984-e4512a34-746c-4b1f-8174-79c9c0c6a031.png">

Por otro lado, si comparamos el precio con los ingresos, podemos darnos cuenta de que estos si están relacionados; dado que a mayor riqueza de los habitantes de la zona, más cara suele ser la casa.

<img width="960" alt="2022-05-07" src="https://user-images.githubusercontent.com/91720991/167247787-28bc5c2f-a968-4cdd-9dba-e9dc07a82af1.png">



# 4 - Grafique todo lo que considere oportuno.

Ya se han expuesto los gráficos requeridos.

# 5 - (Opcional) Aplique algún tipo de clustering o reducción de dimensionalidad e intente encontrar relaciones entre los datos.

Se han intentado agrupar los datos para agrupar las casas en función de las más baratas.

        print("Se van a realizar una agrupación de las casas poniendo un precio límite.")

        casas = pd.read_csv("USA_Housing.csv")

        casas.rename(columns = {'Avg. Area Income': 'Ingresos', 'Avg. Area House Age': 'Edad', 'Avg. Area Number of Rooms': 'Salas', 'Avg. Area Number of Bedrooms': 'Dormitorios', 'Area Population': 'Area', 'Price': 'Precio', 'Address': 'Direccion'}, inplace = True)

        filtro = 1232072

        casas_baratas =casas['Precio']<=filtro
        positions = np.flatnonzero(casas_baratas)
        filtered_df = casas_baratas.iloc[positions]

        print(filtered_df)
