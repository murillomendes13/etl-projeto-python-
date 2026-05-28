import csv

# EXTRACT
with open(r'C:\Users\Murillo\Downloads\Desafio DIO\dados_familia.csv', mode='r', encoding='utf-8') as file:
    leitor = csv.DictReader(file)
    clientes = list(leitor)

print("\nClientes carregados:")
for cliente in clientes:
    print(cliente)

# TRANSFORM
clientes_transformados = []

for cliente in clientes:
    mensagem = (
        f"Olá {cliente['nome']},\n"
        f"Sua conta {cliente['conta']} está ativa.\n"
        f"Seu cartão {cliente['cartao']} foi validado com sucesso."
    )

    clientes_transformados.append({
        "nome": cliente["nome"],
        "mensagem": mensagem
    })

# LOAD
with open('output_clientes.csv', mode='w', encoding='utf-8', newline='') as file:
    campos = ['nome', 'mensagem']
    escritor = csv.DictWriter(file, fieldnames=campos)

    escritor.writeheader()
    escritor.writerows(clientes_transformados)