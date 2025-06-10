#%%
import pandas as pd
# %%
df = pd.read_csv("../data/transacoes.csv")
df
# %%


filtro = (df["qtdePontos"] >=50) & (df["qtdePontos"] <=100)
filtro
 
# %%
df[filtro]
# %%
