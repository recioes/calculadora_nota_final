import tkinter as tk

print("Cálculo da nota final da disciplina")

#Função de mensagem de erro
def validar_nota(nota):
    if nota < 0 or nota > 100:
        print("Nota inválida. Digite um valor de 0 a 100.")
        exit()

#Nota dos oito exercícios
print("Informe uma nota de 0 a 100")

lista_atividade = []
for i in range(1, 9):
    nota = float(input(f"Informe a nota da atividade {i}: "))
    lista_atividade.append(nota)
    validar_nota(nota)

#Nota do fórum e da sistematização
forum = float(input("Informe a nota do fórum temático:"))
validar_nota(forum)
sistematizacao = float(input("Informe a nota da sistematização:"))
validar_nota(sistematizacao)

#Nota da prova
prova = float(input("Informe a nota da avaliação da disciplina:"))
validar_nota(prova)

# O peso de cada exercício é 0,025. Multiplicando a soma dos exercícios por 0,025, obtemos a contribuição dos exercícios para a nota final (20%)
exercicios = sum([nota * 0.025 for nota in lista_atividade])

#Cálculo da nota final
nota_final = (forum * 0.2) + (sistematizacao * 0.2) + (prova * 0.4) + (exercicios)
print("a nota final do aluno é:", round(nota_final, 2))

if nota_final <= 50:
    print("reprovado")
else:
    print("aprovado")