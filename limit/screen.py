class Screen:
    
    def options(self):
        print("")
        print("")
        print("====================================")
        print("------------------------------------")
        print("---------- TRABALHINHO 01 ----------")
        print("----------- PILHA E FILA -----------")
        print("------------------------------------")
        print("====================================")
        print("")
        print("")

        while True:
            try:
                option = int(input("Escolha [1] - Pilha | [2] - Fila: "))

            except ValueError:
                print("Conteúdo Inválido. Digite o conteúdo correto.")
            else:
                return option
