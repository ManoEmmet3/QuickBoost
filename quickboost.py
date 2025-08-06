import tkinter as tk
from PIL import Image, ImageTk

janela = tk.Tk()
janela.title("Quickboost")
janela.geometry("640x480")
janela.configure(bg="#252526")
janela.resizable(False, False)

# Ícone da janela (.ico)
janela.iconbitmap("assets\\quick.ico")

# Barra horizontal no topo
barra_topo = tk.Frame(janela, height=45, bg="#434344")
barra_topo.pack(side="top", fill="x")

# Abrir e redimensionar a imagem do ícone (PNG)
imagem = Image.open("assets/quick.png")
imagem = imagem.resize((45, 45))  # tamanho da imagem
icone = ImageTk.PhotoImage(imagem)

# Label com o ícone dentro da barra_topo
label_icone = tk.Label(barra_topo, image=icone, bg="#434344")
label_icone.pack(side="left", padx=10, pady=2)

# Label com o texto QuickBoost usando a fonte Inter
label_texto = tk.Label(
    barra_topo,
    text="QuickBoost",
    font=("Inter", 18),
    fg="white",
    bg="#434344"
)
label_texto.pack(side="left", padx=5)

# Barra vertical no canto esquerdo
barra_lateral = tk.Frame(janela, width=85, bg="#323234")
barra_lateral.pack(side="left", fill="y")

# Conteúdo principal
conteudo = tk.Frame(janela, bg="#252526")
conteudo.pack(expand=True, fill="both")

janela.mainloop()
