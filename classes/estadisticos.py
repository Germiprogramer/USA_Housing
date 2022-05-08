import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Media:
    def __init__(self, csv, columna):
        self.csv = csv
        self.columna = columna

    def calculo(self):
        media = self.csv[self.columna].mean()
        print("La media es:")
        print(media)

class Desviacion_tipica:
    def __init__(self, csv, columna):
        self.csv = csv
        self.columna = columna

    def calculo(self):
        desv = self.csv[self.columna].mad()
        print("La desviación tipica es:")
        print(desv)

class Varianza:
    def __init__(self, csv, columna):
        self.csv = csv
        self.columna = columna

    def calculo(self):
        var = self.csv[self.columna].var()
        print("La varianza es:")
        print(var)

class Filas:
  def __init__(self, csv):
    self.csv = csv

  def calculo(self):
    print('El numero de filas es:',self.csv.shape[0])

class Columnas:
  def __init__(self, csv):
    self.csv = csv

  def calculo(self):
    print('El numero de columnas es:',self.csv.shape[1])

class Maximos:
  def __init__(self, csv, columna):
      self.csv = csv
      self.columna = columna

  def calculo(self):
      max = self.csv[self.columna].max()
      print("El valor máximo es:")
      print(max)

class Minimos:
  def __init__(self, csv, columna):
      self.csv = csv
      self.columna = columna

  def calculo(self):
      min = self.csv[self.columna].min()
      print("El valor mínimo es:")
      print(min)

class Mediana:
  def __init__(self, csv, columna):
      self.csv = csv
      self.columna = columna

  def calculo(self):
      median = self.csv[self.columna].median()
      print("La mediana es:")
      print(median)

class Moda:
  def __init__(self, csv, columna):
      self.csv = csv
      self.columna = columna

  def calculo(self):
      moda = self.csv[self.columna].mode()
      print("La moda es:")
      print(moda)

class Rango:
  def __init__(self, csv, columna):
      self.csv = csv
      self.columna = columna

  def calculo(self):
      rango = self.csv[self.columna].range()
      print("La moda es:")
      print(rango)

class Q1:
  def __init__(self, csv, columna):
      self.csv = csv
      self.columna = columna

  def calculo(self):
      q1 = self.csv[self.columna].quantile(0.25)
      print("El primer cuartil es:")
      print(q1)

class Q3:
  def __init__(self, csv, columna):
      self.csv = csv
      self.columna = columna

  def calculo(self):
      q3 = self.csv[self.columna].quantile(0.75)
      print("El tercer cuartil es:")
      print(q3)

class Correlacion:
    def __init__(self, dataset, lista_columnas_eliminadas, nombregrafico):
        self.dataset = dataset
        self.lista_columnas_eliminadas = lista_columnas_eliminadas
        self.nombregrafico = nombregrafico
    def calculo(self):
        filtrado=self.dataset.drop(self.lista_columnas_eliminadas,axis=1)

        print("Seguidamente, se procederá a analizar la relación de las variables solicitadas.")
        print(filtrado,"\n")

        #Realizamos la correlación

        print("La gráfica de la correlación entre las distintas columnas es la siguiente: ")
        corr_df = filtrado.corr()
        print(corr_df, "\n")

        #plt.matshow(corr_df)
        #plt.show()

        plt.figure(figsize=(8, 6))
        sns.heatmap(corr_df, annot=True)
        
        plt.savefig('{}.png'.format(self.nombregrafico), bbox_inches='tight')
        plt.show()