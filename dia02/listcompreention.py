#%%
marcas = ["Ferrari" , "Nissan",  "Ford" , "GM"]
carros = ["488", "350Z", "Territorry", "Onix"]


mercadorias = list(zip(marcas,carros))
mercadorias
# %%
tupla_iteravel = [('19888713', 'João'), ('17899746', 'Maria'),
                  ('59444468', 'José'), ('13877746', 'Claúdia'),
                  ('25774698', 'Ana')]
zip_code , nomes = zip(*tupla_iteravel)
zip_code=list(zip_code)
nomes = list(nomes)
print(zip_code)
print(nomes)
# %%
pilotos = [('Verstappen', 'RedBull'), ('Russel', 'Mercedes'),
         ('Hamilton', 'Ferrari'), ('Piastri', 'Mclaren')]

tempos = [ [ 1.25], [1.27], [1.26] , [1.24]] 

#%%

colocacao = [x for x in [pilotos,tempos]] 
colocacao
# %%
desempenho_escolar = {'Patrick': [10,9,9.5], 'Luana': [9.1,9.7,10], 'Ana': 
                    [4.5,7.4,9.2]}

try:
    consulta = input("Digite o aluno que queira saber a nota: ")
    resutado = desempenho_escolar[consulta]
except KeyError:
    print("Estudante não encontrado na nossa base de dados")
else:
    print(resutado)  
finally:
    ("Consulta encerrada")
# %%
preco_produtos = [12000,7700,3697,230000]
produtos = ["Iphone 16", "S25", "Geladeira Samsung" ,"Song plus"]

#%%
def calcular_imposto(preco, imposto):
    return preco * imposto

impostos = [calcular_imposto(preco,0.4) for preco in preco_produtos] 
print(impostos)
    
# %%
lista_int = list(zip(preco_produtos, produtos))

lista_int.sort(reverse=True)
lista_int

# %%


meta_vendas = 17000
vendas_valores = [12000,2146,26900,90000]

vendedores = [ "Flávio", "Lucas", "Maurício", "Pool"]


vendedores_check_meta = []

vendedores_check_meta= [vendedor for i , vendedor in enumerate(vendedores) if vendas_valores[i]> meta_vendas]
print(vendedores_check_meta)
# %%

meta_insignias = 18 
valores_insignias = [12,9,4,7,21]

treinadores = ["Ash", "Brock", "Mistty", "oliver", "Celebi"] 
hall_fama_treinadores = []

hall_fama_treinadores = [treinador for i , treinador in enumerate(treinadores) if valores_insignias[i]>meta_insignias]
print(hall_fama_treinadores)



# %%

hall_superior = []

for i, treinador in enumerate(treinadores):
    if valores_insignias[i] > meta_insignias:
        hall_superior.append(treinador)        
print(hall_superior)        

# %%


ball_oro = [ ('Messi','Barcelona',8 ), ('Cristiano', 'Real Madrid', 5)]

maior_ganhador= []

for name,time,premio in ball_oro:
    if premio > 7:
        maior_ganhador.append(name)
# %%
maior_ganhador
# %%
