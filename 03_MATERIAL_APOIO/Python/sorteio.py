# %%

import pandas as pd
import random
import numpy as np
import time

dados = {
'id':[1,2,3,4,5]
, 'nome':['Daniel Duarte','Edmagno Gomes dos Santos','Mateus Luís Soncin Gazola','Renato Fidelis Ribeiro', 'Wallace Camargo Pereira da Graça']
, 'email':['danielduarte0496@gmail.com', 'edmagnogomes@gmail.com', 'magazola06@gmail.com','fidelisrenato8@gmail.com','wallacecpdg@gmail.com']
}

df = pd.DataFrame(dados)

print(df)

total = 7453246

while total > 0:

    valor = random.randint(1, 5)

    total -= 1

print('E ai quem vai ganhar...')

time.sleep(30)

print('Sorteio realizado...E o vencedor foi...')

time.sleep(30)

print(df[df['id']==valor]['nome'])

print('Vencedor: ' + str(valor))

# %%
