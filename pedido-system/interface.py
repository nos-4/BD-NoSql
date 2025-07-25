import tkinter as tk
from tkinter import messagebox
from pedido_service import criar_pedido, buscar_pedido_por_id

def mostrar_tela_inicial():
    frame_cadastro.pack_forget()
    frame_busca.pack_forget()
    frame_inicial.pack()

def mostrar_tela_cadastro():
    frame_inicial.pack_forget()
    frame_cadastro.pack()

def mostrar_tela_busca():
    frame_inicial.pack_forget()
    frame_busca.pack()

root = tk.Tk()
root.title("📦 Sistema de Pedidos")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

# Frame inicial
frame_inicial = tk.Frame(root, bg="#f0f0f0")
tk.Label(frame_inicial, text="Bem-vindo ao Sistema de Pedidos", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=30)
tk.Button(frame_inicial, text="➕ Cadastrar Pedido", command=mostrar_tela_cadastro, width=25, height=2, bg="lightgreen").pack(pady=10)
tk.Button(frame_inicial, text="🔍 Buscar Pedido por ID", command=mostrar_tela_busca, width=25, height=2, bg="lightblue").pack(pady=10)
frame_inicial.pack()

# Frame cadastro
frame_cadastro = tk.Frame(root, bg="#f0f0f0")

tk.Label(frame_cadastro, text="Nome do Cliente", bg="#f0f0f0").pack(pady=5)
entry_nome = tk.Entry(frame_cadastro, width=40)
entry_nome.pack()

tk.Label(frame_cadastro, text="Produto", bg="#f0f0f0").pack(pady=5)
entry_produto = tk.Entry(frame_cadastro, width=40)
entry_produto.pack()

tk.Label(frame_cadastro, text="Quantidade", bg="#f0f0f0").pack(pady=5)
entry_quantidade = tk.Entry(frame_cadastro, width=40)
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
        entry_nome.delete(0, tk.END)
        entry_produto.delete(0, tk.END)
        entry_quantidade.delete(0, tk.END)
        mostrar_tela_inicial()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao criar pedido: {e}")

tk.Button(frame_cadastro, text="✅ Criar Pedido", command=enviar, bg="lightgreen").pack(pady=15)
tk.Button(frame_cadastro, text="← Voltar", command=mostrar_tela_inicial).pack()

# Frame busca
frame_busca = tk.Frame(root, bg="#f0f0f0")

tk.Label(frame_busca, text="ID do Pedido", bg="#f0f0f0").pack(pady=10)
entry_id = tk.Entry(frame_busca, width=40)
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
        entry_id.delete(0, tk.END)
        mostrar_tela_inicial()
    else:
        messagebox.showerror("Erro", "Pedido não encontrado.")

tk.Button(frame_busca, text="🔍 Buscar", command=buscar, bg="lightblue").pack(pady=15)
tk.Button(frame_busca, text="← Voltar", command=mostrar_tela_inicial).pack()

root.mainloop()
