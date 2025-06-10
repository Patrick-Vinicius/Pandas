#%%
idades = [
    32 , 42 , 38 , 41 , 20,
    19 , 52 , 18 , 11 , 22,
    17, 25 , 26 , 27 , 29
]


media = sum(idades)/len(idades)
media 


#%%
diffs = 0
    
for i in idades:
        diffs += ( i - media)**2
variancia = diffs / (len(idades)-1)

print(variancia)
# %%
import pandas as pd

series_idades = pd.Series(idades)
series_idades 
# %%

#medias = series_idades.mean()
var_idades = series_idades.var()
sumary_idades = series_idades.describe()
sumary_idades
# %%

series_idades = series_idades.sort_values()
series_idades

# %%
series_idades.loc["Adriano"]
series_idades.iloc[-1]