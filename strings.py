menu = """

 ==== MENU ====

  [1] Depositar
  [2] Sacar
  [3] Extrato
  [4] Sair
"""

saldo = 0
depositos = []
saques_total = []
LIMITE_SAQUES_DIARIOS = 3
SAQUE_MAXIMO = 500

while True:
    opcao = float(input("Digite a opção: "))

    if opcao == 1:
        valorDeposito = float(input("Quanto você deseja depositar? "))
        if valorDeposito <= 0:
            print("Deve ser um valor acima de 0.")
            break

        depositos.append(valorDeposito)
        saldo += valorDeposito

        print(
            f"""
            Foi depositado um valor de {valorDeposito} na sua conta.
            Valor atual: {saldo}
            """
        )

    if opcao == 2:
        if saldo > 0:
            saque = float(input("Quanto você deseja sacar? "))
            if saque > saldo:
                print(
                    f"""
Você não tem saldo suficiente.
Saldo atual: {saldo}

            """
                )
                continue
            if saque < 0:
                print(
                    f"""
                Impossível sacar esse valor.

            """
                )
                continue

            saques_total.append(saque)
            saldo -= saque

            print(
                f"""
                Você sacou: {saque}.
                Novo saldo: {saldo}
            """
            )
        else:
            print(
                f"""

            Saldo insuficiente para saque.
            Saldo total: {saldo}

  """
            )
    if opcao == 3:
        print(
            f"""
            Depositos realizados: {depositos}
            Saques realizados: {saques_total}
            Saldo atual: R$ {saldo:.2f}
"""
        )
    if opcao == 4:
        break
