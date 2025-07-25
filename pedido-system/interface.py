import tkinter as tk
from tkinter import messagebox
from pedido_service import criar_pedido, buscar_pedido_por_id

# ----- JANELA DE CADASTRO -----
def janela_cadastro():
    cadastro = tk.Toplevel()
    cadastro.title("Cadastrar Pedido")
    cadastro.geometry("400x300")

    tk.Label(cadastro, text="Nome do Cliente").pack(pady=5)
    entry_nome = tk.Entry(cadastro, width=40)
    entry_nome.pack()

    tk.Label(cadastro, text="Produto").pack(pady=5)
    entry_produto = tk.Entry(cadastro, width=40)
    entry_produto.pack()

    tk.Label(cadastro, text="Quantidade").pack(pady=5)
    entry_quantidade = tk.Entry(cadastro, width=40)
    entry_quantidade.pack()

    def enviar():
        nome = entry_nome.get()
        produto = entry_produto.get()
        quantidade = entry_quantidade.get()

        if not nome or not produto or not quantidade:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        try:
            pedido = criar_pedido(nome, produto, int(quantidade))
            messagebox.showinfo("Sucesso", f"Pedido criado com ID: {pedido.id}")
            cadastro.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar pedido: {e}")

    tk.Button(cadastro, text="✅ Criar Pedido", command=enviar, bg="lightgreen").pack(pady=15)


# ----- JANELA DE BUSCA -----
def janela_busca():
    busca = tk.Toplevel()
    busca.title("Buscar Pedido por ID")
    busca.geometry("400x250")

    tk.Label(busca, text="ID do Pedido").pack(pady=10)
    entry_id = tk.Entry(busca, width=40)
    entry_id.pack()

    def buscar():
        pedido_id = entry_id.get()
        if not pedido_id:
            messagebox.showwarning("Atenção", "Informe o ID do pedido.")
            return

        pedido = buscar_pedido_por_id(pedido_id)
        if pedido:
            resultado = f"""
Cliente: {pedido.nome_cliente}
Produto: {pedido.produto}
Quantidade: {pedido.quantidade}
Data: {pedido.data_criacao}
"""
            messagebox.showinfo("Pedido Encontrado", resultado)
            busca.destroy()
        else:
            messagebox.showerror("Erro", "Pedido não encontrado.")

    tk.Button(busca, text="🔍 Buscar", command=buscar, bg="lightblue").pack(pady=15)


# ----- JANELA PRINCIPAL -----
def janela_principal():
    root = tk.Tk()
    root.title("📦 Sistema de Pedidos")
    root.geometry("500x300")
    root.configure(bg="#f0f0f0")

    tk.Label(root, text="Bem-vindo ao Sistema de Pedidos", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=30)

    tk.Button(root, text="➕ Cadastrar Pedido", command=janela_cadastro, width=25, height=2, bg="lightgreen").pack(pady=10)
    tk.Button(root, text="🔍 Buscar Pedido por ID", command=janela_busca, width=25, height=2, bg="lightblue").pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    janela_principal()
