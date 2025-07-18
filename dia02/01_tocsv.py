#%%
import pandas as pd

df = pd.read_csv("../data/clientes.csv")

df
# %%
df.to_parquet("clientes.parquet")
# %%
df_2 = pd.read_parquet("clientes.parquet")
df_2
# %%
df.to_excel("clientes.xlsx", index=False)
# %%
df_3 = pd.read_excel("clientes.xlsx")
df_3
# %%
