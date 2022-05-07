import matplotlib.pyplot as plt
import pandas as pd

def grafico(dataset, tipo_grafico, titulografico, nombregrafico):
  fig, ax = plt.subplots()
 
  dataset.plot(kind=tipo_grafico, ax = ax, color = "red")
  ax.set_title(str(titulografico), loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:orange'})
  ax.set_ylabel('')
 
  plt.show()

  plt.savefig('{}.png'.format(nombregrafico), bbox_inches='tight')

def dispersión(df, columna, nombregrafico):
    
    data=df[columna].groupby(pd.cut(df[columna], range(100,240,10))).count()
    fig, ax = plt.subplots()
    lista = []
    for i in range(100,230,10):
        lista.append(i)
    plt.scatter(lista,data)
    plt.title('Diagrama de dispersión:', color= 'orange')         
    plt.show()
    fig.savefig('{}.png'.format(nombregrafico))