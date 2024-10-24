import tkinter as tk
from tkinter import messagebox, scrolledtext

def gerar_codigos(codigos):
    resultados = []
    for codigo in codigos:
        volume_maximo = int(codigo[14:21])
        prefixo = codigo[:14]
        sufixo = codigo[21:]
        for volume in range(1, volume_maximo + 1):
            novo_codigo = f"{prefixo}{volume:07d}{sufixo}"
            resultados.append(novo_codigo)
        resultados.append("")
    return resultados

def processar_codigos():
    codigos_input = text_input.get("1.0", tk.END).strip().splitlines()
    if not codigos_input:
        messagebox.showwarning("Entrada inválida", "Por favor, insira pelo menos um código.")
        return

    try:
        codigos_gerados = gerar_codigos(codigos_input)
        text_output.delete("1.0", tk.END)
        for codigo in codigos_gerados:
            text_output.insert(tk.END, f"{codigo}\n")
        text_output.see(tk.END)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

root = tk.Tk()
root.title("Gerador de Códigos de Barras")
root.geometry("600x550")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

label_input = tk.Label(root, text="Insira os códigos de barras (um por linha):", bg="#f0f0f0", font=("Arial", 12))
label_input.pack(pady=10)

text_input = scrolledtext.ScrolledText(root, height=10, width=60, font=("Arial", 12), fg="gray")
text_input.pack(pady=5)

button_processar = tk.Button(root, text="Processar Códigos", command=processar_codigos, bg="#4CAF50", fg="white", font=("Arial", 12))
button_processar.pack(pady=10)

label_output = tk.Label(root, text="Códigos gerados:", bg="#f0f0f0", font=("Arial", 12))
label_output.pack(pady=10)

text_output = scrolledtext.ScrolledText(root, height=10, width=60, font=("Arial", 12), fg="gray")
text_output.pack(pady=5)

root.mainloop()
