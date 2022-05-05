# USA_Housing

La primera parte del trabajo es realizar un análisis del dataset dado. Se ha elegido analizar el parámetro "precio", debido a que es el que tiene un mayor interés de cara a aquellos que estén interesados en las casas del archivo.

# 1 - Grafique las variables implicadas de las maneras que crea oportunas.

Para un mayor entendimiento del dataset, se ha graficado el precio de las casas utilizando un histograma. Se ha decidido usar este tipo de gráfico debido a que se considera que es el más adecuado para mostrar la disponibilidad de las casas respecto a su precio.

<img width="461" alt="2022-05-05 (3)" src="https://user-images.githubusercontent.com/91720991/167028240-2bbbbe1f-7671-480d-b649-886076f1b5f9.png">

# 2 - Identifique si es necesaria una limpieza de datos y/o completar valores perdidos.

Para la limpieza de datos, hemos usado la función dropna() de pandas. Al ser un dataset muy extenso, no podemos identificar a primera vista, por lo que usamos la función dropna() para eliminar aquellas filas que no tengan un valor para el precio. El código utilizado es el siguiente.

    casas = casas.dropna(subset=["Precio"])

# 3 - Obtenga las correlaciones entre variables y analice si se pueden observar algunas relaciones interesantes.

# 4 - Grafique todo lo que considere oportuno.

# 5 - (Opcional) Aplique algún tipo de clustering o reducción de dimensionalidad e intente encontrar relaciones entre los datos.
