import matplotlib.pyplot as plt

def grafico(dataset, tipo_grafico, nombregrafico):
  fig, ax = plt.subplots()
 
  dataset.plot(kind=tipo_grafico, ax = ax, color = "red")
  ax.set_title(str(nombregrafico), loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:orange'})
  ax.set_ylabel('')
 
  plt.show()

  plt.savefig('grafico.png', bbox_inches='tight')