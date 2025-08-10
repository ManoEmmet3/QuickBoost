import customtkinter as ctk
from PIL import Image, ImageTk
import os
import tkinter as tk

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
        label_icone.image = img_tk  # mantém referência
        label_icone.pack(pady=(20, 5), anchor="center")

    titulo = ctk.CTkLabel(
        frame_pai,
        text="Bem-vindo ao QuickBoost",
        text_color="white",
        bg_color="#252526",
        font=("Poppins", 27, "normal")
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
    espacamento = 60  # distância horizontal entre os botões

    largura_total = largura_botao * 2 + espacamento
    largura_frame = frame_pai.winfo_width()

    x_inicial = (largura_frame - largura_total) // 2
    y_inicial = linha2.winfo_y() + linha2.winfo_height() + 40

    fonte_botao = ("Inter", 15)  # 2 pixels maior que antes (12->14)

    def efeito_clique():
        # muda cor para mais escura
        botao1.configure(fg_color="#6d57b3")
        # depois de 150ms volta a cor original
        frame_pai.after(150, lambda: botao1.configure(fg_color="#9375FF"))
        # aqui você pode chamar a função do scan pc

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
        command=efeito_clique
    )
    botao1.place(x=x_inicial, y=y_inicial)
    botao2 = ctk.CTkButton(
    frame_pai,
    text="Ler mais",
    width=largura_botao,
    height=altura_botao,
    corner_radius=5,
    font=fonte_botao,
    fg_color="white",           # fundo branco
    text_color="#0E6FBE",       # cor da letra
    border_width=2,             # largura da borda
    border_color="#0E6FBE",     # cor da borda
    hover_color="#D6E9FB"       # cor ao passar o mouse (opcional)
)
    botao2.place(x=x_inicial + largura_botao + espacamento, y=y_inicial)



if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("600x500")
    root.configure(bg="#252526")

    mostrar(root)

    root.mainloop()
