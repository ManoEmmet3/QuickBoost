import tkinter as tk
from PIL import Image, ImageTk
import wmi
import psutil

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

# Monta string final do Windows
versao_windows = f"{nome_so}, {arquitetura_formatada}"

# Obter info do processador via WMI
cpu_info = w.Win32_Processor()[0]
nome_cpu = cpu_info.Name.strip()

# Obter memória RAM total via psutil (em GB, arredondado)
ram_bytes = psutil.virtual_memory().total
ram_gb = round(ram_bytes / (1024**3), 1)
# Formata com vírgula no lugar do ponto decimal
ram_formatada = f"{str(ram_gb).replace('.', ',')}GB RAM"

# Texto do hardware
texto_hardware = f"{nome_cpu} {ram_formatada}"

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

# Frame para os textos do SO e hardware (vertical)
frame_textos = tk.Frame(barra_topo, bg="#434344")
frame_textos.pack(side="left", padx=15)

# Texto do sistema operacional formatado
label_info = tk.Label(
    frame_textos,
    text=versao_windows,
    font=("Inter", 10),
    fg="lightgray",
    bg="#434344"
)
label_info.pack(anchor="w")

# Texto do processador e RAM, abaixo do SO
label_hardware = tk.Label(
    frame_textos,
    text=texto_hardware,
    font=("Inter", 10),
    fg="lightgray",
    bg="#434344"
)
label_hardware.pack(anchor="w")

# Barra lateral
barra_lateral = tk.Frame(janela, width=85, bg="#323234")
barra_lateral.pack(side="left", fill="y")

# Conteúdo principal
conteudo = tk.Frame(janela, bg="#252526")
conteudo.pack(expand=True, fill="both")

janela.mainloop()
