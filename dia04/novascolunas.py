#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%
df = pd.read_csv("../data/clientes.csv")
df.head()
# %%
df['qtdePontos_100'] = df['qtdePontos'] + 100
df
# %%

df.describe()
# %%
df['qtdePontos'] = np.log(df ['qtdePontos']+1)
df['qtdePontos'].describe()
# %%
plt.hist(df['qtdePontos'])
plt.grid(True)
plt.show()
# %%
times = pd.DataFrame({
    "nome": ["Real Madrid", "Milan" , "Bayern de Munique", "Ajax"],
    "titulos_champions" : [15,7,6,4],
    "Ano_Criacao" : [1912,1905,1898,1936]
})

times
# %%
times.sort_values(by="Ano_Criacao",ascending=False)
# %%

dft = pd.read_csv("../data/clientes.csv")
dft
# %%
dft["qtdePontos"].astype(float)
# %%

replace = {
        "0000-00-00 00:00:00.000" : "2024-12-06 09:00:00.000" ,  
    }
dft["dtCriacao"]= pd.to_datetime(dft["dtCriacao"].replace(replace))
# %%
# %%

dft["dtCriacao"].dt.month

# %%
# df.dropna(how="all or any", subset = ["coluna"]
# )
dft["dtCriacao"] = df["dtCriacao"].fillna(0)
dft
# %%
