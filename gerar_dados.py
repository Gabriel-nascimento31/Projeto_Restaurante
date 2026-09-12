from lista_encadeada import Lista
from faker import Faker
import pickle

fake = Faker('pt_BR')
numero_dados = 100

dados = Lista()

for c in range(numero_dados):
    cliente = fake.name()

    dados.adicionar(cliente)

print('Dados gerados com sucesso!')



with open("dados_lista.bin", "wb") as f:
    pickle.dump(dados, f)


print("Lista gravada no arquivo 'dados_lista.bin'.")


print(dados)
