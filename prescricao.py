#minha_prescricao=['Acido Acetilsalicilico', 'Alcool', 'Insulinas']  #listas
#minha_prescricao.append('Anticoagulantes Orais')

#Acido_Acetilsalicilico = {'Alcool': 'potencialmente grave'}    #dicionario
#experimentando gavetasprint(Acido_Acetilsalicilico['alcool'])

#Acido_Acetilsalicilico ['Alcool'] = 'muito grave'
# serviu para ver a alteração de grave para muito grave print(Acido_Acetilsalicilico['alcool'])

#for Acido_Acetilsalicilico in minha_prescricao:
 #   print(Acido_Acetilsalicilico)                #serve para atribuir uma variável a uma lista

#for indice, medicamento in enumerate (minha_prescricao, start=1):
 #   print(indice, medicamento) #serve para enumerar a lista
 
#avisos= {'Alcool' : 'Risco de hemorragia se misturado com insulina'}
#def verificar_receita(lista_meds):
       
#    for indice, med in enumerate (minha_prescricao, start=1):
 #       print(f"{indice}.{med}")

#Se o medicamento "med" estiver no dicionário de avisos
  #      if med in avisos:
            #print(f"\t ATENÇÃO :{avisos[med]}")



#1 A base de Dados
avisos = {'Alcool': 'Pode causar hemorragia se misturado com insulina'}

#2 Definir função
def analisar_paciente(lista_meds):
        print('\n--- A analisar prescrição ---')
        for indice, meds in enumerate (lista_meds, start=1):
            print(f'{indice}.{meds}')
            if meds in avisos:
                print(f'\t ATENÇÃO: {avisos[meds]}')


#3 Os dados
minha_prescricao = ['Acido Acetilsalicilico', 'Anticoagulantes Orais', 'Alcool', 'Insulina']

#4 Analisar o paciente

analisar_paciente(minha_prescricao)