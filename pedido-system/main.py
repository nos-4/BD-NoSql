from pedido_service import criar_pedido, buscar_pedido_por_id, atualizar_pedido, cancelar_pedido

def menu():
    while True:
        print("\n=== Sistema de Pedidos ===")
        print("[1] Criar novo pedido")
        print("[2] Buscar pedido por ID")
        print("[3] Cancelar pedido")     
        print("[4] Atualizar pedido")
        print("[0] Sair") 
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            produto = input("Produto: ")
            try:
                quantidade = int(input("Quantidade: "))
            except ValueError:
                print("⚠️ Quantidade inválida, deve ser um número.")
                continue

            pedido = criar_pedido(nome, produto, quantidade)
            print(f"✅ Pedido criado: ID {pedido.id}")

        elif opcao == "2":
            pedido_id = input("ID do pedido: ")
            pedido = buscar_pedido_por_id(pedido_id)
            if pedido:
                print("\n📄 Dados do Pedido:")
                print(f"Cliente: {pedido.nome_cliente}")
                print(f"ID: {str(pedido.id)}")
                print(f"Produto: {pedido.produto}")
                print(f"Quantidade: {pedido.quantidade}")
                print(f"Data: {pedido.data_criacao}")
            else:
                print("❌ Pedido não encontrado.")

        elif opcao == "0":
            print("👋 Saindo do sistema...")
            break
        elif opcao == "3":
            id_cancelar = input("Digite o ID do pedido para cancelar: ")
            cancelar_pedido(id_cancelar)
        elif opcao == "4":
            id_atualizar = input("Digite o ID do pedido para atualizar: ")
            novo_nome = input("Novo nome do cliente (pressione Enter para manter o mesmo): ")
            novo_produto = input("Novo produto (pressione Enter para manter o mesmo): ")
            nova_quantidade = input("Nova quantidade (pressione Enter para manter a mesma): ")
            nova_quantidade = int(nova_quantidade) if nova_quantidade else None
            atualizar_pedido(id_atualizar, novo_nome or None, novo_produto or None, nova_quantidade)
        else:
            print("⚠️ Opção inválida.")

if __name__ == "__main__":
    menu()
