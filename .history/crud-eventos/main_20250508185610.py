import re

organizadores = []

while True:

    def isCpfValid(cpf):
    
        if not isinstance(cpf,str):
            return False

        # Remove some unwanted characters
        cpf = re.sub("[^0-9]",'',cpf)
        
        # Verify if CPF number is equal
        if cpf=='00000000000' or cpf=='11111111111' or cpf=='22222222222' or cpf=='33333333333' or cpf=='44444444444' or cpf=='55555555555' or cpf=='66666666666' or cpf=='77777777777' or cpf=='88888888888' or cpf=='99999999999':
            return False

        # Checks if string has 11 characters
        if len(cpf) != 11:
            return False

        sum = 0
        weight = 10

        """ Calculating the first cpf check digit. """
        for n in range(9):
            sum = sum + int(cpf[n]) * weight

            # Decrement weight
            weight = weight - 1

        verifyingDigit = 11 -  sum % 11

        if verifyingDigit > 9 :
            firstVerifyingDigit = 0
        else:
            firstVerifyingDigit = verifyingDigit

        """ Calculating the second check digit of cpf. """
        sum = 0
        weight = 11
        for n in range(10):
            sum = sum + int(cpf[n]) * weight

            # Decrement weight
            weight = weight - 1

        verifyingDigit = 11 -  sum % 11

        if verifyingDigit > 9 :
            secondVerifyingDigit = 0
        else:
            secondVerifyingDigit = verifyingDigit

        if cpf[-2:] == "%s%s" % (firstVerifyingDigit,secondVerifyingDigit):
            return True
        return False
    
    class BuscaEndereco:

        def __init__(self, cep):
            cep = str(cep)
            if self.cep_eh_Valido(cep):
                self.cep = cep
            else:
                raise ValueError("CEP inválido!")

        def cep_eh_Valido(self, cep):
            if len(cep) == 8:
                padrao_cep = re.compile(r'(\d){5}(\d){3}')

                match = padrao_cep.match(cep)

                return True
            else:
                return False    

    print("------MENU PRINCIPAL-----")

    print("1 - Organizador")
    print("2 - Participante")
    print("3 - Sair do programa")
    
    opcao = int(input("\nDigite a opção desejada: "))
    
    if (opcao == 1):

        while True:     
            print("------MENU ORGANIZADOR-----")
            
            print("1 - Atualizar Cadastro")
            print("2 - Editar Cadastro")
            print("3 - Excluir Cadastro")
            print("4 - Criar Evento")
            print("5 - Voltar ao menu")
            
            opcao = int(input("\nDigite a opção desejada: "))
            
            if (opcao == 1):
                nome = input("Digite o nome: ")
                while True:
                    telefone = input("Digite o seu telefone: ")
                    # Exemplo de padrão para telefone com DDD e número, como (11) 91234-5678 ou 11912345678
                    padrao = r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$'

                    if re.match(padrao, telefone):
                        print("Telefone válido!")
                    else:
                        print("Telefone inválido. Por favor, insira no formato (XX) XXXXX-XXXX ou XXXXXXXXXX.")
                telefone = input("Digite o seu telefone ")
                email = input("Digite o nome: ")
                while True:
                    cpf = input("Digite o cpf 000.000.000-00: ") 
                    try:
                        isCpfValid(cpf)
                        break
                    except ValueError:
                        print("\nCPF inválido! Digite um cpf válido.")
                endereco = input("Digite o seu endereço: ")
                numero = int(input("Digite o número: "))
                complemento = input("Digite o complemento: ")
                bairro = input("Digite o seu bairro: ")
                cidade = input("Digite o sua Cidade: ")
                estado = input("Digite o seu Estado: ")
                while True:
                    cep = input("Digite o seu cep: ")
                    try:
                        objeto_cep = BuscaEndereco(cep)
                        break
                    except ValueError:
                        print("\nCep inválido! Digite o cep válido.")        

                organizador = {
                    "nome":nome,
                    "cpf":cpf,
                    "endereço":endereco,
                    "número":numero,
                    "complemento":complemento,
                    "bairro": bairro,
                    "cidade": cidade,
                    "estado":estado,
                    "cep":cep
                }

                organizadores.append(organizador)
                print(f"\nA atividade {nome} foi cadastrada com sucesso!\n")

            elif (opcao == 2):
                if organizadores:
                    print("\n--- Editar Organizador ---")
                    for i, organizador in enumerate(organizadores):
                        print(f"{i+1}. Nome: {organizador['nome']}")
                        print(f"   CPF: {organizador['cpf']}")
                        print(f"   Horário: {organizador['endereço']}")
                        print(f"   Número: {organizador['número']}")
                        print(f"   Complemento: {organizador['complemento']}")
                        print(f"   Bairro: {organizador['bairro']}")
                        print(f"   Cidade: {organizador['cidade']}")
                        print(f"   Estado: {organizador['estado']}")
                        print(f"   Cep: {organizador['cep']}")
                    indice_editar = int(input("Digite o número da atividade que deseja excluir: ")) - 1 
                    if 0 <= indice_editar < len(organizadores):
                        organizador = organizadores[indice_editar]

                        print("\nCampos disponíveis para edição: nome, cpf, número, endereço, complemento, bairro, cidade, estado, cep\n")
                        campo_editar = input("\nDigite o campo que deseja editar: ").lower()

                        if campo_editar in organizador:
                            novo_valor = input(f"Digite o novo valor para {campo_editar}: ")
                        organizador[campo_editar] = novo_valor
                        print(f"\nCampo {campo_editar} atualizado com sucesso!\n")
            elif (opcao == 3):
                if organizadores:
                    print("\n--- Excluir Organizador ---")
                    for i, organizador in enumerate(organizadores):
                        print(f"{i+1}. {organizador['nome']}")
                    indice_excluir = int(input("Digite o número da atividade que deseja excluir: ")) - 1
                    if 0 <= indice_excluir < len(organizadores):
                        organizador_excluido = organizadores.pop(indice_excluir)
                        print(f"A atividade '{organizador_excluido['nome']}' foi excluída com sucesso!")
                    else:
                        print("\nOrganizador não existe")
            elif (opcao == 4):
                print("Parte de Nicolly")
            elif (opcao == 5):
                break
            else:
                print("\nOpção inválida! Tente novamento\n")
    elif(opcao ==2 ):
        print("Parte de Thomaz e Heitor")
    elif(opcao == 3):
        print("\nPrograma encerrado. Volte sempre!!")
        break
    else:
        print("\nOpção inválida. Tente novamente\n")