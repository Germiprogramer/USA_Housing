# USA_Housing

La primera parte del trabajo es realizar un análisis del dataset dado. Se ha elegido analizar el parámetro "precio", debido a que es el que tiene un mayor interés de cara a aquellos que estén interesados en las casas del archivo.

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


# 5 - (Opcional) Aplique algún tipo de clustering o reducción de dimensionalidad e intente encontrar relaciones entre los datos.
