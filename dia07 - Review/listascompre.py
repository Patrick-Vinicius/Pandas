#%%

sopa_letras = "que que tem na sopa do neném?"

list_sopa = []

for z in sopa_letras:
    list_sopa.append(z)
print(list_sopa)    
# %%


sopa_selecoes = "Germany, France , Greece"

lista_de_Teams = []

for y in sopa_selecoes:
    lista_de_Teams.append(y)
print(lista_de_Teams)
# %%
#utilizando list compreention


sopa_letras = "que que tem na sopa do neném?"

list_sopa = []

list_sopa = [w for w in sopa_letras]
list_sopa
# %%
sopa_selecoes = "Germany, France , Greece"

lista_de_Teams = []

lista_de_Teams = [f for f in sopa_selecoes]
lista_de_Teams
# %%
