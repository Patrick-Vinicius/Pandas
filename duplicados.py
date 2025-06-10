#%%
import pandas as pd
# %%
df = pd.DataFrame ({
    "nome" :  ["Bruno", "Richard", "Flaco", "Robert", "Estevao", "Abel", "Abel", "Bruno"],
    "estado_natal": ["Rio Grande do Sul","Medellin", "Saladas", "São Paulo" , "São Paulo", "Braga","Braga", "Rio Grande do Sul"],
    "salario": [7000,4500,9075,4690,4500,12000,12000,12000]
        
})

df

#%%
df = (df.sort_values("salario", ascending=False)
      .drop_duplicates(keep="last", subset=["nome" , "salario"]))
df
# %%
