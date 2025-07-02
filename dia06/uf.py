#%% 
import pandas as pd

#%%

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
    
uf = pd.read_html(url)

ufs = uf[1]
# %%
ufs
# %%


def str_to_float (x:str):
    x= float(x.replace(" ", "")
                .replace(",", ".")
                .replace("\xa0", "")
             )
    return x

ufs["Área (km²)"] = ufs["Área (km²)"].apply(str_to_float)
ufs["População (Censo 2022)"] = ufs["População (Censo 2022)"].apply(str_to_float)
ufs["PIB (2015)"]= ufs["PIB (2015)"].apply(str_to_float)
ufs["PIB per capita (R$) (2015)"] = ufs['PIB per capita (R$) (2015)'].apply(str_to_float)

# %%
ufs
# %%


def uf_regiao(ufs):
    if ufs in ["Acre", "Amapá","Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
        return "Região Norte"
    elif ufs in ["Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]: 
        return "Região Nordeste"
    elif ufs in ["Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Região Sudeste"
    elif ufs in [ "Paraná", "Rio Grande do Sul","Santa Catarina"]:
        return "Região Sul"
    elif ufs in ["Distrito Federal", "Goiás, Mato Grosso", "Mato Grosso do Sul"]:
        return "Região Centro-Oeste"
# %%
ufs["Região"] = ufs["Unidade federativa"].apply(uf_regiao)
ufs["Região"]
# %%
ufs
# %%
