# POP - Paradigma Orientada a Procedimentos
# numero = 876;
# titutar = 'Pablo';
# saldo = 413.57;
# limite = 5000.00;


# POO - Paradigma Orientada a Objetos
# conta = {
#     "numero": 876,
#     "titular": "Pablo",
#     "saldo": 413.57,
#     "limite": 2100.00
# }

def criarConta(numero, titular, saldo, limite):
    conta = {
        "numero": numero,
        "titular": titular,
        "saldo": saldo,
        "limite": limite
    }
    return conta

conta = criarConta(876, 'Aroldo', 413.57, 2100.00)
print(conta)

def depositar(conta, valor):
    conta["saldo"] += valor

def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print(f'Seu saldo atual é {conta["saldo"]}')

depositar(conta, 250)
extrato(conta)
sacar(conta, 500.57)
extrato(conta)