import tkinter as tk
from PIL import Image, ImageTk
import os
from tkinter import font

from telas import statusgeral

def mudar_aba(num_aba):
    print(f"Mudando para aba {num_aba}")
    if num_aba == 1:
        statusgeral.mostrar(frame_principal)

janela = tk.Tk()
janela.title("QuickBoost")
janela.geometry("820x480")
janela.configure(bg="black")

caminho_icone = os.path.join("assets", "quick.ico")
if os.path.exists(caminho_icone):
    janela.iconbitmap(caminho_icone)

# Barra superior
faixa = tk.Frame(janela, bg="#434344", height=60)
faixa.pack(side="top", fill="x")

# Logo
caminho_imagem = os.path.join("assets", "quick.png")
if os.path.exists(caminho_imagem):
    imagem = Image.open(caminho_imagem)
    imagem = imagem.resize((48, 48), Image.Resampling.LANCZOS)
    imagem_tk = ImageTk.PhotoImage(imagem)
    label_imagem = tk.Label(faixa, image=imagem_tk, bg="#434344")
    label_imagem.pack(side="left", padx=10, pady=6)
else:
    label_imagem = tk.Label(faixa, text="[Logo]", bg="#434344", fg="white", font=("Arial", 20))
    label_imagem.pack(side="left", padx=10, pady=6)

# Texto título
fonte_inter = font.Font(family="Inter", size=18, weight="normal")
label_texto = tk.Label(faixa, text="QuickBoost", bg="#434344", fg="#ffffff", font=fonte_inter)
label_texto.pack(side="left", padx=10, pady=12)

# Área principal (barra lateral + conteúdo)
frame_conteudo = tk.Frame(janela, bg="black")
frame_conteudo.pack(side="top", fill="both", expand=True)

# Barra lateral com largura fixa 128px
barra_lateral = tk.Frame(frame_conteudo, bg="#323234", width=128)
barra_lateral.pack(side="left", fill="y")
barra_lateral.pack_propagate(False)  # Não deixa encolher

# Área conteúdo que muda
frame_principal = tk.Frame(frame_conteudo, bg="#252526")
frame_principal.pack(side="left", fill="both", expand=True)

# Carrega o ícone do botão com tamanho 36x36
caminho_icone_botao = os.path.join("assets", "status_icon.png")
if os.path.exists(caminho_icone_botao):
    icone_img = Image.open(caminho_icone_botao)
    icone_img = icone_img.resize((36, 36), Image.Resampling.LANCZOS)
    icone_tk = ImageTk.PhotoImage(icone_img)
else:
    icone_tk = None

# Fonte menor (11) para o botão
fonte_botao = font.Font(family="Inter", size=11, weight="normal")

# Botão configurado para manter texto branco sempre
botao_unico = tk.Button(
    barra_lateral,
    text="Status Geral",
    image=icone_tk,
    compound="top",
    bg="#323234",
    activebackground="#2e2e2f",
    fg="white",               # texto branco normal
    activeforeground="white", # texto branco ao clicar
    font=fonte_botao,
    relief="flat",
    borderwidth=0,
    command=lambda: mudar_aba(1),
    pady=7
)
botao_unico.image = icone_tk
botao_unico.place(x=0, y=0, width=128, height=100)

# Inicializa com a aba 1 aberta
mudar_aba(1)

janela.mainloop()
