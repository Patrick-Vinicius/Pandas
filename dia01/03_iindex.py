#%%
import pandas as pd
#%%


idades = [
    32 , 42 , 38 , 41 , 20,
    19 , 52 , 18 , 11 , 22,
    17, 25 , 26 , 27 , 29
]

indexs = [
    "Oliver" , "Luana", "Ahmed", "Layla", "Patrick",
    "Bruna" ,  "Albert" , "Miguel" , "Cleyton", "Puta Cana",
    "Adriano" , "Raniere", "Liliane" , "Thierry" , "Bruno"
]
series_idades = pd.Series(idades, index=indexs)


# %%
series_idades["Bruna"]
# %%
series_idades.iloc[-1]
# %%
series_idades.iloc[::-1]
# %%
df = pd.DataFrame()
df["idades"] = series_idades
df['nomes'] = indexs
df
# %%

series_idades = series_idades.sort_values()
series_idades

# %%
series_idades.loc["Adriano"]
# %%
