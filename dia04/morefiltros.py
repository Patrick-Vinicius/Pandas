#%%
import pandas as pd
#%%

treinadores_pokemons = pd.DataFrame ({
    "nome" : ["Brock", None, "Misty", "Ash", None],
    "n_pokemons": [792, 36, None, 1907, None],
    "Km_percorrido" : [3904, 150 , 15000, None, None]
    
})
#%%
treinadores_pokemons.dropna(how="all", subset=["nome"])
# %%
treinadores_pokemons.dropna(how="all", subset=["nome","Km_percorrido"])
# %%

treinadores_pokemons.fillna(0)
# %%
medias = treinadores_pokemons['n_pokemons'].mean()
treinadores_pokemons.fillna(medias)
# %%
