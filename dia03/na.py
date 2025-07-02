#%%
import pandas as pd
# %%
df = pd.DataFrame(
    {
        "nome": ["Clio", None, None,"Uno"],
        "marca": ["Renault", "Fiat", "Jeep", "Fiat"],
        "ano_producao": [2014,None,2024,2008]
    }
)
# %%
df.dropna(how="all", subset=["nome", "ano_producao"])
# %%

dt = pd.DataFrame(
    {
        "nome" : ["Luna", "David", "Luna", "Oliver","Maria"],
        "sobrenome": ["Silva", "Luna", "Silva","Santana","Santos"],
        "pagamento":[22227,11123,7987,741,7987]
        
    }
)
dt
# %%
dt = dt.sort_values("pagamento", ascending=False)
dt
# %%
dt.drop_duplicates(keep="last", subset=["nome","sobrenome"])
# %%
# ---------------------------------------------------------------
transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.head()
# %%
transacoes = transacoes.sort_values("dtCriacao")


# %%
transacoes["data"] = pd.to_datetime(transacoes['dtCriacao']).dt.date

transacoes.drop_duplicates(keep="first", subset= ["idCliente","data"])
# %%
# transacoes.drop_duplicates(keep="first", subset= ["idCliente","data"])

# transacoes.drop_duplicates(keep="last", subset= ["idCliente","data"])
# %%
