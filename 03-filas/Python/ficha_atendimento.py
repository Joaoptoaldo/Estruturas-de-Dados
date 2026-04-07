import __main__


class FichaAtendimento:

    @staticmethod
    def gera_ficha_normal(fila_normal, contador_normal):
        """_summary_: metodo de classe que gera ficha normal

        Args:
            fila_normal (_type_): _description_: classe deque que representa a fila normal  
            contador_normal (_type_): _description_: variável do tipo int que representa o contador de fichas normais, inicia em 1 e vai até 500

        Returns:
            _type_: _description_
        """
        print("Imprimindo ficha normal....", end="")
        print(contador_normal)
        fila_normal.append(contador_normal)
        contador_normal += 1

        return contador_normal

    @staticmethod
    def gera_ficha_prioritaria(fila_prioritaria, contador_prioritaria):
        """_summary_: método de classe que gera ficha prioritária

        Args:
            fila_prioritaria (_type_): _description_: classe deque que representa a fila prioritária
            contador_prioritaria (_type_): _description_: variável do tipo int que representa o contador de fichas prioritárias, inicia em 501 e vai até 1000

        Returns:
            _type_: _description_
        """
        print("Imprimindo ficha prioritária....", end="")
        print(contador_prioritaria)
        fila_prioritaria.append(contador_prioritaria)
        contador_prioritaria += 1

        return contador_prioritaria

    @staticmethod
    def gera_atendimento(fila_normal, fila_prioritaria, contador_atendimentos):
        """_summary_: método de classe que gera atendimento, a cada 3 fichas normais, chama uma ficha prioritária, testar se a fila que for chamar não está vazia, se estiver vazia chamar a outra fila

        Args:
            fila_normal (_type_): _description_: classe deque que representa a fila normal
            fila_prioritaria (_type_): _description_: classe deque que representa a fila prioritária
            contador_atendimentos (_type_): _description_: variável do tipo int que representa o contador de atendimentos, inicia em 0 e vai incrementando a cada atendimento gerado

        Returns:
            _type_: _description_
        """
        if (not fila_normal) and (not fila_prioritaria):
            print("Não há fichas para chamar")

            return contador_atendimentos
        
        print("Chamando ficha... ", end="")

        if contador_atendimentos % 3 == 0 or (not fila_normal):
            if fila_prioritaria:
                ficha = fila_prioritaria.pop(0)

                print("PRIORITARIA: " + str(ficha))
                contador_atendimentos += 1

                return contador_atendimentos

        if fila_normal:
            ficha = fila_normal.pop(0)
            print("NORMAL: " + str(ficha))
            contador_atendimentos += 1

        return contador_atendimentos
    
    @staticmethod
    def mostrar_fichas_faltantes(filaNormal, filaPrioritaria):
        """_summary_: método de classe que exibe as fichas faltantes, ou seja, as fichas que ainda estão na fila normal e prioritária

        Args:
            filaNormal (_type_): _description_: classe deque que representa a fila normal
            filaPrioritaria (_type_): _description_: classe deque que representa a fila prioritária
        """
        print("Mostrando fichas faltantes... ")
        if filaNormal:
            print("Fichas normais faltantes: " + str(len(filaNormal)) + " - " + str(filaNormal))
        if filaPrioritaria:
            print("Fichas prioritárias faltantes: " + str(len(filaPrioritaria)) + " - " + str(filaPrioritaria))

        
    @staticmethod
    def menu(filaNormal=None, filaPrioritaria=None):#none para evitar que a fila seja compartilhada entre as chamadas do menu, ou seja, cada vez que o menu for chamado, uma nova fila será criada
        """_summary_: método de classe que exibe o menu para o usuário escolher as opções, a cada opção escolhida, chama o método correspondente, o menu deve ser exibido até que o usuário escolha a opção de sair, ou seja, a opção 5

        Args:
            filaNormal (_type_, optional): _description_. Defaults to None.
            filaPrioritaria (_type_, optional): _description_. Defaults to None.
        """
        if filaNormal is None:# none para evitar que a fila seja compartilhada entre as chamadas do menu, ou seja, cada vez que o menu for chamado, uma nova fila será criada
            filaNormal = []
        if filaPrioritaria is None:
            filaPrioritaria = []

        contadorNormal = 1
        contadorPrioritaria = 501
        contadorAtendimentos = 0

        while True:
            print("\n")
            print("--- MENU ---")
            print("1 - Ficha normal")
            print("2 - Ficha prioritária")
            print("3 - Chamar ficha")
            print("4 - Mostrar fichas faltantes")
            print("5 - Sair")

            opcao = input("Escolha uma opção: \n")

            if opcao == "1":
                contadorNormal = FichaAtendimento.gera_ficha_normal(filaNormal, contadorNormal)
            elif opcao == "2":
                contadorPrioritaria = FichaAtendimento.gera_ficha_prioritaria(filaPrioritaria, contadorPrioritaria)
            elif opcao == "3":
                contadorAtendimentos = FichaAtendimento.gera_atendimento(filaNormal, filaPrioritaria, contadorAtendimentos)
            elif opcao == "4":
                FichaAtendimento.mostrar_fichas_faltantes(filaNormal, filaPrioritaria)
            elif opcao == "5":
                print("Saindo...")
                break
            else:
                print("Opção inválida!")

if __name__ == "__main__":

    FichaAtendimento.menu()