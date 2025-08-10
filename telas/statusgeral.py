import customtkinter as ctk
from PIL import Image, ImageTk
import os
import tkinter as tk
import threading
from telas import scan_pc

def mostrar(frame_pai):
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

    def iniciar_scan():
        # Mostra texto ou animação de carregando
        loading_label = ctk.CTkLabel(frame_pai, text="Carregando...", text_color="white", font=("Inter", 14))
        loading_label.place(relx=0.5, rely=0.7, anchor="center")

        def tarefa_scan():
            # Simula demora (ou faz o processamento pesado aqui)
            import time
            time.sleep(2)  # simula scan demorado

            # Após terminar, remove loading e chama scan_pc
            loading_label.destroy()
            scan_pc.mostrar(frame_pai)

        # Roda a tarefa na thread para não travar interface
        threading.Thread(target=tarefa_scan, daemon=True).start()

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
        command=iniciar_scan  # chama função que mostra loading e depois scan_pc
    )
    botao1.place(x=x_inicial, y=y_inicial)

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
