nome = input("Digite seu nome do corretista: ")
banco = input("Digite o nome do banco: ")
salario = float(input("Quanto foi recebido o salário: "))
ferias = float(input("Quanto foi recebido de férias: "))
pix = float(input("Quanto foi recebido de PIX: "))
saque = float(input("Quanto foi sacado: "))

saldo = salario + ferias + pix - saque
if saldo > 0:
    print("Saldo positivo")
elif saldo < 0:
    print("Saldo negativo, Solicite um empréstimo")
else:
    print("Saldo zerado")
  
print("\n---------------------------------------\n")
print("Nome do corretista: ", nome)
print("Banco: ", banco)
print("Saldo: R$", saldo)
print("\n---------------------------------------\n")
print("Obrigado pela atenção")