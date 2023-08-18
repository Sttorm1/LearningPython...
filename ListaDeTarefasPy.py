def adicionar_tarefa(lista, tarefa):
    lista.append(tarefa)
    print(f'Tarefa "{tarefa}" adicionada à lista.')

def remover_tarefa(lista, tarefa):
    if tarefa in lista:
        lista.remove(tarefa)
        print(f'Tarefa "{tarefa}" removida da lista.')
    else:
        print(f'Tarefa "{tarefa}" não encontrada na lista.')

def mostrar_tarefas(lista):
    if lista:
        print("Lista de tarefas:")
        for index, tarefa in enumerate(lista, start=1):
            print(f"{index}. {tarefa}")
    else:
        print("Lista de tarefas está vazia.")

def main():
    lista_de_tarefas = []
    
    while True:
        print("\nMenu:")
        print("1. Adicionar tarefa")
        print("2. Remover tarefa")      
        print("3. Mostrar tarefas")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            tarefa = input("Digite a tarefa a ser adicionada: ")
            adicionar_tarefa(lista_de_tarefas, tarefa)
        elif escolha == "2":
            tarefa = input("Digite a tarefa a ser removida: ")
            remover_tarefa(lista_de_tarefas, tarefa)
        elif escolha == "3":
            mostrar_tarefas(lista_de_tarefas)
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida, escolha novamente.")

if __name__ == "__main__":
    main()
