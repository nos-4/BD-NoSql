import tkinter as tk
from tkinter import messagebox
from pedido_service import (
    criar_pedido,
    buscar_pedido_por_id,
    atualizar_pedido,
    cancelar_pedido
)

def mostrar_tela_inicial():
    frame_cadastro.pack_forget()
    frame_busca.pack_forget()
    frame_alterar.pack_forget()
    frame_inicial.pack()

def mostrar_tela_cadastro():
    frame_inicial.pack_forget()
    frame_cadastro.pack()

def mostrar_tela_busca():
    frame_inicial.pack_forget()
    frame_busca.pack()

def mostrar_tela_alterar():
    frame_inicial.pack_forget()
    frame_alterar.pack()

root = tk.Tk()
root.title("Sistema de Pedidos")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

# Frame inicial
frame_inicial = tk.Frame(root, bg="#f0f0f0")
tk.Label(frame_inicial, text="Bem-vindo ao Sistema de Pedidos", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=30)
tk.Button(frame_inicial, text=" Cadastrar Pedido", command=mostrar_tela_cadastro, width=30, height=2, bg="lightgreen").pack(pady=10)
tk.Button(frame_inicial, text=" Buscar Pedido", command=mostrar_tela_busca, width=30, height=2, bg="lightblue").pack(pady=10)
tk.Button(frame_inicial, text=" Alterar ou Cancelar Pedido", command=mostrar_tela_alterar, width=30, height=2, bg="orange").pack(pady=10)
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

tk.Button(frame_cadastro, text="Criar Pedido", command=enviar, bg="lightgreen").pack(pady=15)
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

tk.Button(frame_busca, text="Buscar", command=buscar, bg="lightblue").pack(pady=15)
tk.Button(frame_busca, text="← Voltar", command=mostrar_tela_inicial).pack()

# Frame alterar/cancelar
frame_alterar = tk.Frame(root, bg="#f0f0f0")

tk.Label(frame_alterar, text="ID do Pedido", bg="#f0f0f0").pack(pady=10)
entry_id_alt = tk.Entry(frame_alterar, width=40)
entry_id_alt.pack()

tk.Label(frame_alterar, text="Novo Nome do Cliente", bg="#f0f0f0").pack(pady=5)
entry_novo_nome = tk.Entry(frame_alterar, width=40)
entry_novo_nome.pack()

tk.Label(frame_alterar, text="Novo Produto", bg="#f0f0f0").pack(pady=5)
entry_novo_produto = tk.Entry(frame_alterar, width=40)
entry_novo_produto.pack()

tk.Label(frame_alterar, text="Nova Quantidade", bg="#f0f0f0").pack(pady=5)
entry_nova_quantidade = tk.Entry(frame_alterar, width=40)
entry_nova_quantidade.pack()

def alterar():
    pedido_id = entry_id_alt.get()
    novo_nome = entry_novo_nome.get()           # novo campo para nome do cliente
    novo_produto = entry_novo_produto.get()
    nova_quantidade_str = entry_nova_quantidade.get()

    if not pedido_id or not novo_nome or not novo_produto or not nova_quantidade_str:
        messagebox.showwarning("Atenção", "Preencha todos os campos.")
        return

    try:
        nova_quantidade = int(nova_quantidade_str)
    except ValueError:
        messagebox.showerror("Erro", "Quantidade inválida. Digite um número.")
        return

    try:
        atualizado = atualizar_pedido(
            pedido_id,
            novo_nome=novo_nome,
            novo_produto=novo_produto,
            nova_quantidade=nova_quantidade
        )
        if atualizado:
            messagebox.showinfo("Sucesso", "Pedido atualizado com sucesso.")
        else:
            messagebox.showerror("Erro", "Pedido não encontrado.")
        mostrar_tela_inicial()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao atualizar pedido: {e}")


def cancelar():
    pedido_id = entry_id_alt.get()
    if not pedido_id:
        messagebox.showwarning("Atenção", "Informe o ID do pedido.")
        return

    try:
        deletado = cancelar_pedido(pedido_id)
        if deletado:
            messagebox.showinfo("Sucesso", "Pedido cancelado com sucesso.")
        else:
            messagebox.showerror("Erro", "Pedido não encontrado.")
        mostrar_tela_inicial()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cancelar pedido: {e}")

tk.Button(frame_alterar, text=" Alterar Pedido", command=alterar, bg="orange").pack(pady=10)
tk.Button(frame_alterar, text=" Cancelar Pedido", command=cancelar, bg="red", fg="white").pack(pady=10)
tk.Button(frame_alterar, text="← Voltar", command=mostrar_tela_inicial).pack()

root.mainloop()
