from pedido_service import criar_pedido, buscar_pedido_por_id

def menu():
    while True:
        print("\n=== Sistema de Pedidos ===")
        print("[1] Criar novo pedido")
        print("[2] Buscar pedido por ID")
        print("[0] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            produto = input("Produto: ")
            quantidade = input("Quantidade: ")
            pedido = criar_pedido(nome, produto, quantidade)
            print(f"✅ Pedido criado: ID {pedido.id}")

        elif opcao == "2":
            pedido_id = input("ID do pedido: ")
            pedido = buscar_pedido_por_id(pedido_id)
            if pedido:
                print("\n📄 Dados do Pedido:")
                print(f"Cliente: {pedido.nome_cliente}")
                print(f"Produto: {pedido.produto}")
                print(f"Quantidade: {pedido.quantidade}")
                print(f"Data: {pedido.data_criacao}")
            else:
                print("❌ Pedido não encontrado.")

        elif opcao == "0":
            print("👋 Saindo do sistema...")
            break
        else:
            print("⚠️ Opção inválida.")

if __name__ == "__main__":
    menu()
