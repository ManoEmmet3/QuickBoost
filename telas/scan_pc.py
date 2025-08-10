import customtkinter as ctk

def mostrar(frame_pai):
    # Limpa widgets anteriores
    for widget in frame_pai.winfo_children():
        widget.destroy()

    # Título central
    label = ctk.CTkLabel(
        frame_pai,
        text="Aba Scan PC",
        text_color="white",
        font=("Poppins", 25)
    )
    label.place(relx=0.5, rely=0.5, anchor="center")

    # Botão voltar
    botao_voltar = ctk.CTkButton(
        frame_pai,
        text="Voltar",
        command=lambda: voltar(frame_pai)
    )
    botao_voltar.place(relx=0.5, rely=0.65, anchor="center")

def voltar(frame_pai):
    from telas import statusgeral
    statusgeral.mostrar(frame_pai)
