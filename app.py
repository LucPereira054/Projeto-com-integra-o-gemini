import streamlit as st
from lista_tarefas import(adcionar_tarefas,listar_tarefas,marcar_concluida,
                          otimizar_com_ai, tarefas)


def main():
    while True:
        print("\n---------------MENU-----------------")
        print("1.adcionar|2.listar|3.concluir|4.Otimizar|5.sair")
        opcao=input("Escolha: ")
        
        if opcao=="1":
            desc=input("Descrição: ")
            adcionar_tarefas(desc)
        elif opcao=="2":
            lista=listar_tarefas()
            if not lista:
                print("Nenhuma tarefa encontrada: ")
            for i,t in enumerate(lista,1):
                print(f"{i}.{t['descricao']} - {t['status']}")
        elif opcao=="3":
            listando=listar_tarefas()
            if not listando:
                print("Nenhuma tarefa para concluir.")
            else:
                for index,t in enumerate(listando,start=1):
                    print(f"{index}.{t['descricao']} - {t['status']}")
                try:
                    idx=int(input("Número da tarefa a concluir: "))
                    if marcar_concluida(idx):
                        print("Tarefa marcada como concluída.")
                    else:
                        print("Índice inválido. Nenhuma tarefa encontrada.")
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número.")
        elif opcao=="4":
            lista=listar_tarefas()
            if not lista:
                print("Nenhuma tarefa para otimizar.")
            else:
                ordem_otimizada=otimizar_com_ai(lista)
                print("Ordem de execução sugerida:")
                print(ordem_otimizada)
        elif opcao=="5":
            break

if __name__=="__main__":
    main()

    