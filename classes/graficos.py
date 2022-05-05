import matplotlib.pyplot as plt

class Grafico_barras:
  def __init__(self, csv, columna):
        self.csv = csv
        self.columna = columna
  
  def crear_grafico(self):
    fig, ax = plt.subplots()
    self.csv[self.columna].plot(kind="hist", ax=ax)
    ax.set_title("histograma", loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    ax.set_ylabel('')
    plt.savefig('img/histograma-' + '-'.join(self.columna) + '.png', bbox_inches='tight')
    return

class Grafico_sectores:
  def __init__(self, csv, columna):
        self.csv = csv
        self.columna = columna
  
  def crear_grafico(self):
    fig, ax = plt.subplots()
    self.csv[self.columna].plot(kind="hist", ax=ax)
    ax.set_title("histograma", loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    ax.set_ylabel('')
    plt.savefig('img/histograma-' + '-'.join(self.columna) + '.png', bbox_inches='tight')
    return

class Grafico_histograma:
  def __init__(self, csv, columna):
        self.csv = csv
        self.columna = columna
  
  def crear_grafico(self):
    fig, ax = plt.subplots()
    self.csv[self.columna].plot(kind="hist", ax=ax)
    ax.set_title("histograma", loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    ax.set_ylabel('')
    plt.savefig('img/histograma-', bbox_inches='tight')
    return