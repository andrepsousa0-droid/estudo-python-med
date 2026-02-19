minha_prescricao=['Acido Acetilsalicilico', 'Alcool', 'Insulinas']  #listas
minha_prescricao.append('Anticoagulantes Orais')

Acido_Acetilsalicilico = {'Alcool': 'potencialmente grave'}    #dicionario
#experimentando gavetasprint(Acido_Acetilsalicilico['alcool'])

Acido_Acetilsalicilico ['Alcool'] = 'muito grave'
# serviu para ver a alteração de grave para muito grave print(Acido_Acetilsalicilico['alcool'])

#for Acido_Acetilsalicilico in minha_prescricao:
 #   print(Acido_Acetilsalicilico)                #serve para atribuir uma variável a uma lista

#for indice, medicamento in enumerate (minha_prescricao, start=1):
 #   print(indice, medicamento) #serve para enumerar a lista
 
avisos= {'Alcool' : 'Risco de hemorragia se misturado com insulina'}

for indice, med in enumerate (minha_prescricao, start=1):
    print(f"{indice}.{med}")

#Se o medicamento "med" estiver no dicionário de avisos
    if med in avisos:
        print(f"\t ATENÇÃO :{avisos[med]}")