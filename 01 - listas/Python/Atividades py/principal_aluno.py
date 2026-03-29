from aluno import Aluno 
lista = []

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break

    aluno = Aluno(nome)
    lista.append(aluno)
    print(f"Email gerado: {aluno.email}\n")

print("\n--- ALUNOS CADASTRADOS ---")
for aluno in lista:
    print(f"Nome: {aluno.nome} | Email: {aluno.email}")