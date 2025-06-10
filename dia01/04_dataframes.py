
#%%
import pandas as pd

#%%
idades = [
    32 , 42 , 38 , 41 , 20,
    19 , 52 , 18 , 11 , 22,
    17, 25 , 26 , 27 , 29
]

nomes = [
    "Oliver" , "Luana", "Ahmed", "Layla", "Patrick",
    "Bruna" ,  "Albert" , "Miguel" , "Cleyton", "Puta Cana",
    "Adriano" , "Raniere", "Liliane" , "Thierry" , "Bruno"
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

series_idades
# %%

df = pd.DataFrame()
df ["idades"] = series_idades
df ["nomes"]= series_nomes
df
# %%
df.iloc[2]
# %%
