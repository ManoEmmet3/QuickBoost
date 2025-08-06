import tkinter as tk
from PIL import Image, ImageTk
import wmi

# Obter informações do sistema via WMI
w = wmi.WMI()
so_info = w.Win32_OperatingSystem()[0]

# Remove "Microsoft" do nome do SO e limpa espaços
nome_so = so_info.Caption.replace("Microsoft", "").strip()

# Ajusta arquitetura para garantir "64-bit" ou "32-bit" com hífen e singular "bit"
arquitetura_original = so_info.OSArchitecture.strip()
if "64" in arquitetura_original:
    arquitetura_formatada = "64-bit"
elif "32" in arquitetura_original:
    arquitetura_formatada = "32-bit"
else:
    arquitetura_formatada = arquitetura_original

# Monta string final
versao_windows = f"{nome_so}, {arquitetura_formatada}"

# Cria janela principal
janela = tk.Tk()
janela.title("Quickboost")
janela.geometry("820x480")
janela.configure(bg="#252526")
janela.resizable(False, False)

# Ícone da janela (.ico)
janela.iconbitmap("assets\\quick.ico")

# Barra horizontal no topo
barra_topo = tk.Frame(janela, height=70, bg="#434344")
barra_topo.pack(side="top", fill="x")
barra_topo.pack_propagate(False)

# Abrir e redimensionar a imagem do ícone (PNG)
imagem = Image.open("assets/quick.png")
imagem = imagem.resize((50, 50))
icone = ImageTk.PhotoImage(imagem)

# Ícone na barra
label_icone = tk.Label(barra_topo, image=icone, bg="#434344")
label_icone.pack(side="left", padx=10, pady=5)

# Texto "QuickBoost"
label_texto = tk.Label(
    barra_topo,
    text="QuickBoost",
    font=("Inter", 16, "bold"),
    fg="white",
    bg="#434344"
)
label_texto.pack(side="left", padx=5)

# Texto do sistema operacional formatado
label_info = tk.Label(
    barra_topo,
    text=versao_windows,
    font=("Inter", 10),
    fg="lightgray",
    bg="#434344"
)
label_info.pack(side="left", padx=15)

# Barra lateral
barra_lateral = tk.Frame(janela, width=85, bg="#323234")
barra_lateral.pack(side="left", fill="y")

# Conteúdo principal
conteudo = tk.Frame(janela, bg="#252526")
conteudo.pack(expand=True, fill="both")

janela.mainloop()
