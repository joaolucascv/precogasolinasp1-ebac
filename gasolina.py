import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv('gasolina.csv', sep=',')

with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=gasolina_df, x="dia", y="venda", palette="pastel")
  grafico.set(title='Preço médio de venda da gasolina por dia', xlabel='Dia (Julho de 2021)', ylabel='Preço (R$)');
  plt.savefig('gasolina.png')
