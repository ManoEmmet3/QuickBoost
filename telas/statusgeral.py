import customtkinter as ctk
from PIL import Image, ImageTk
import os
import tkinter as tk
from telas import scan_pc  # importa a função da outra tela

def mostrar(frame_pai):
    # Limpa widgets anteriores
    for widget in frame_pai.winfo_children():
        widget.destroy()

    caminho_icone = os.path.join("assets", "icone.png")
    if os.path.exists(caminho_icone):
        img = Image.open(caminho_icone)
        img = img.resize((153, 153), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        label_icone = tk.Label(frame_pai, image=img_tk, bg="#252526", borderwidth=0)
        label_icone.image = img_tk
        label_icone.pack(pady=(20, 5), anchor="center")

    titulo = ctk.CTkLabel(
        frame_pai,
        text="Bem-vindo ao QuickBoost",
        text_color="white",
        bg_color="#252526",
        font=("Poppins", 30, "normal")
    )
    titulo.pack(pady=(0, 10), anchor="center")

    linha1 = ctk.CTkLabel(
        frame_pai,
        text="Sua ferramenta completa para otimizar",
        text_color="#cccccc",
        bg_color="#252526",
        font=("Inter", 12),
        justify="center"
    )
    linha1.pack(pady=(0, 5), anchor="center")

    linha2 = ctk.CTkLabel(
        frame_pai,
        text="monitorar e manter seu computador rápido e saudável",
        text_color="#cccccc",
        bg_color="#252526",
        font=("Inter", 12),
        justify="center"
    )
    linha2.pack(pady=(0, 20), anchor="center")

    frame_pai.update_idletasks()

    largura_botao = 113
    altura_botao = 40
    espacamento = 60
    largura_total = largura_botao * 2 + espacamento
    largura_frame = frame_pai.winfo_width()
    x_inicial = (largura_frame - largura_total) // 2
    y_inicial = linha2.winfo_y() + linha2.winfo_height() + 40

    fonte_botao = ("Inter", 15)

    # Botão para ir para a tela Scan PC
    botao1 = ctk.CTkButton(
        frame_pai,
        text="Scan PC",
        width=largura_botao,
        height=altura_botao,
        corner_radius=5,
        fg_color="#9375FF",
        text_color="white",
        font=fonte_botao,
        hover_color="#9375FF",
        command=lambda: scan_pc.mostrar(frame_pai)  # chama função da outra tela
    )
    botao1.place(x=x_inicial, y=y_inicial)

    # Botão Ler mais
    botao2 = ctk.CTkButton(
        frame_pai,
        text="Ler mais",
        width=largura_botao,
        height=altura_botao,
        corner_radius=5,
        font=fonte_botao,
        fg_color="white",
        text_color="#0E6FBE",
        border_width=2,
        border_color="#0E6FBE",
        hover_color="#D6E9FB"
    )
    botao2.place(x=x_inicial + largura_botao + espacamento, y=y_inicial)
