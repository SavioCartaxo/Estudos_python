import pandas as pd

vendas_df = pd.read_excel('Vendas.xlsx')

print(vendas_df.loc[1])