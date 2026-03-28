from manager import TaskManager
import os

def menu():
    # Instancia o gerenciador (ele já carrega o JSON se existir)
    manager = TaskManager()

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n--- MENU DE TAREFAS ---")
        print("1. Nova Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir Tarefa")
        print("4. Remover Tarefa por ID")
        print("5. Localizar Tarefa por Título")
        print("6. Listar Tarefas Ordenadas")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            title = input("Título: ")
            desc = input("Descrição: ")
            # O status já tem o padrão "Pendente" no seu código
            manager.new_task(title, desc)

        elif opcao == "2":
            manager.list_task()
            manager.statistics()
            manager.return_menu()

        elif opcao == "3":
            manager.conclude_task()

        elif opcao == "4":
            # Para remover, o usuário digita o ID (ex: 00002)
            try:
                manager.list_task()
                id_for_remove = int(input("Digite o ID para remover: "))
                manager.remove_task(id_for_remove) # Passa o ID já validado
            except ValueError:
                print("Erro: Você precisa digitar um número de ID válido!")
                manager.return_menu()

        elif opcao == "5":
            manager.locate_task()

        elif opcao == "6":
            manager.task_in_order()

        elif opcao == "7":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
