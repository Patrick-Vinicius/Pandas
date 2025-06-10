#%%
import pandas as pd
# %%
df = pd.read_csv("../data/transacao_produto.csv")
df
# %%

filtro_produtos = (df["idProduto"] == 5) | (df["idProduto"] == 11)
filtro_produtos

#%%
df[filtro_produtos]
# %%

df["idProduto"].isin([5,11])
# %%


clientes = pd.read_csv("../data/clientes.csv")
clientes
# %%
clientes["dtCriacao"].notna()
# %%
~clientes["dtCriacao"].isna()
# %%


filtro = clientes["qtdePontos"] == 0
clientes_0 = clientes[filtro].copy()

clientes_0["flag_1"] = 1
clientes_0
# %%
