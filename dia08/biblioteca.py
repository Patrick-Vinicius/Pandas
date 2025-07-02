#%%

import os
# %%

maquinas = [
            ("Retroescavadeira",300),
            ("Helicóptero",7600),
            ("Planeador", 200),
            ("Bi-Trem", 135),
            ("Betoneira", 70),
            ("Caçamba", 98)
          ]

maquinas_alugadas = []
# %%



def listaMaquinas(list_maquinas):
  for i , maqs in enumerate(list_maquinas):
    print(" [{}] {} - R$ {} dia".format(i, maqs[0] , maqs[1]))



while True:
  os.system("clear")
  print("------------------------")
  print("Aluguel de máquinas pesadas")
  print("------------------------")
  print("O que desejas fazer?")
  print("0 - Listar veículos / 1- Alugar uma máquina pesada | 2- Devolver uma máquina pesada")
  
  op = int(input())
 
 

  if op == 0:
    listaMaquinas(maquinas)
  elif op == 1:
    listaMaquinas(maquinas)
    
    print("----------------")
    print("Escolha o código da máquina pesada")
    cod_car = int(input())
    print(" Quantos dias deseja alugar a máquina pesada ?")
    dias = int(input())
    
    
    print("Você escolheu {} por {} dias".format(maquinas[cod_car][0],dias))
    print("o aluguel totalizaria R$ {}, Deseja realmente alugar ?".format(dias*maquinas[cod_car][1]))
     
    print("0 - Sim | 1 - Não ")  
    conf = int(input())
    os.system("clear")
  
    if conf == 0:
      print("Parabéns, você alugou o {} por {} dias.".format(maquinas[cod_car][0],dias))
      maquinas_alugadas.append(maquinas.pop(cod_car))
      
    elif conf ==1:
      print("Encerrando...")
      break
    
    
    elif op == 2:
      print("Máquinas pesadas alugadas")
      
      if len(maquinas_alugadas) == 0:
        print("Não há carros para alugar")
      else:
        print("Lista de carros alugados")
        
        listaMaquinas(maquinas_alugadas)
        print("")
        
        print("Escolha o código da máquina para devolução")
        cod = int(input())
        if conf == 0:
          print("Obrigado por de devolver o {}".format(maquinas_alugadas[0]))
          maquinas.append(maquinas_alugadas.pop(cod))
      
# %%
