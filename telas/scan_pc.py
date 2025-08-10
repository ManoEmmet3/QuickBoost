import customtkinter as ctk
from PIL import Image
from pathlib import Path
import platform
import psutil
import wmi  # pip install wmi

SKU_MAP = {
    12: "Home", 13: "Home", 101: "Home",
    121: "Home China",
    3: "Pro", 27: "Pro", 28: "Pro",
    4: "Enterprise", 48: "Enterprise",
    96: "Education", 97: "Education",
}

id_after = None

def pegar_temperatura_cpu():
    try:
        w = wmi.WMI(namespace="root\\wmi")
        for t in w.MSAcpi_ThermalZoneTemperature():
            c = (t.CurrentTemperature / 10) - 273.15
            if c > 0: return c
    except: pass
    return None

def pegar_temperatura_hd():
    return None  # Normalmente não disponível via WMI

def obter_versao_edicao_windows():
    try:
        w = wmi.WMI()
        so = w.Win32_OperatingSystem()[0]
        base = so.Caption.replace("Microsoft ", "").strip()
        edicao = SKU_MAP.get(getattr(so, "OperatingSystemSKU", None), "")
        arquitetura = platform.architecture()[0].replace("bit", " bits")
        return f"{base} {edicao} {arquitetura}".strip()
    except:
        so = platform.system()
        versao = platform.release()
        arquitetura = platform.architecture()[0].replace("bit", " bits")
        return f"{so} {versao} {arquitetura}"

def obter_nome_cpu():
    nome = platform.processor() or "Desconhecido"
    freq = psutil.cpu_freq()
    if freq: nome += f" @ {freq.current/1000:.2f}GHz"
    return nome

def obter_tipo_storage():
    try:
        w = wmi.WMI()
        d = w.Win32_DiskDrive()[0]
        interface = d.InterfaceType.upper()
        modelo = d.Model.strip()
        tamanho_gb = int(d.Size)/(1024**3) if d.Size else 0
        media_type = getattr(d, "MediaType", "").lower() if hasattr(d, "MediaType") else ""
        if "NVME" in interface:
            tipo = "SSD NVMe"
        elif any(x in interface for x in ["SATA", "IDE", "SCSI"]):
            tipo = "SSD SATA" if "ssd" in media_type else "HD"
        else:
            tipo = "HD"
        return tipo, modelo, tamanho_gb
    except: return "HD", "Desconhecido", 0

def obter_info_gpu():
    try:
        w = wmi.WMI()
        gpu = w.Win32_VideoController()[0]
        modelo = gpu.Name.strip()
        memoria = gpu.AdapterRAM or 0
        memoria_gb = int(memoria) / (1024**3)
        uso_pct = 42  # Valor fixo (simulado), adapte para pegar real se quiser
        return modelo, memoria_gb, uso_pct
    except:
        return "Desconhecido", 0, 0

def criar_frame_info(pai, y, icone_path, titulo):
    caminho_assets = Path(__file__).parent.parent / "assets"
    icone = ctk.CTkImage(
        Image.open(caminho_assets / icone_path),
        Image.open(caminho_assets / icone_path),
        size=(25, 25)
    )
    frame = ctk.CTkFrame(pai, fg_color="transparent")
    frame.place(x=27, y=y)
    ctk.CTkLabel(frame, image=icone, text="").grid(row=0, column=0, sticky="n")
    ctk.CTkLabel(frame, text=titulo, text_color="#9375FF", font=("Inter", 15)).grid(row=0, column=1, sticky="w", padx=(20, 0))
    label_info = ctk.CTkLabel(frame, text="", text_color="#fff", font=("Inter", 13))
    label_info.grid(row=1, column=1, columnspan=6, sticky="w", padx=(50, 0))
    frame.update_idletasks()
    return frame, label_info

def mostrar(frame_pai):
    global id_after
    if id_after:
        frame_pai.after_cancel(id_after)
        id_after = None
    for w in frame_pai.winfo_children():
        w.destroy()

    frame_so, lbl_so = criar_frame_info(frame_pai, 25, "windows.png", "Sistema Operacional")
    frame_cpu, lbl_cpu = criar_frame_info(frame_pai, frame_so.winfo_y() + frame_so.winfo_height() + 20, "cpu.png", "CPU")
    frame_ram, lbl_ram = criar_frame_info(frame_pai, frame_cpu.winfo_y() + frame_cpu.winfo_height() + 18, "ram.png", "RAM")
    frame_hd, lbl_hd = criar_frame_info(frame_pai, frame_ram.winfo_y() + frame_ram.winfo_height() + 18, "storage.png", "Storage")
    frame_gpu, lbl_gpu = criar_frame_info(frame_pai, frame_hd.winfo_y() + frame_hd.winfo_height() + 18, "gpu.png", "GPU")

    lbl_so.configure(text=obter_versao_edicao_windows())

    def atualizar():
        global id_after
        try:
            if not all(lbl.winfo_exists() for lbl in (lbl_cpu, lbl_ram, lbl_hd, lbl_gpu)):
                return

            # CPU
            nome_cpu = obter_nome_cpu()
            uso_cpu = psutil.cpu_percent(interval=None)
            temp_cpu = pegar_temperatura_cpu()
            temp_cpu_texto = f"{temp_cpu:.0f}°C" if temp_cpu is not None else "N/A"
            lbl_cpu.configure(text=f"CPU: {nome_cpu} — Uso: {uso_cpu:.0f}% — Temp: {temp_cpu_texto}")

            # RAM
            mem = psutil.virtual_memory()
            lbl_ram.configure(text=(
                f"Total: {mem.total/(1024**3):.1f} GB  -  Uso atual: {mem.used/(1024**3):.1f} GB "
                f"({mem.percent:.0f}%)  Livre: {mem.available/(1024**3):.1f} GB"))

            # Storage
            total_bytes = free_bytes = 0
            for p in psutil.disk_partitions(all=False):
                if 'fixed' in p.opts.lower():
                    try:
                        uso = psutil.disk_usage(p.mountpoint)
                        total_bytes += uso.total
                        free_bytes += uso.free
                    except PermissionError:
                        continue

            pct_livre = (free_bytes / total_bytes * 100) if total_bytes > 0 else 0
            tipo, modelo, tamanho_gb = obter_tipo_storage()
            temp_hd = pegar_temperatura_hd()
            temp_hd_texto = f"{temp_hd:.0f}°C" if temp_hd is not None else "N/A"
            lbl_hd.configure(text=(
                f"{tipo}: {modelo} {tamanho_gb:.0f}GB — "
                f"{free_bytes/(1024**3):.0f} GB livres ({pct_livre:.0f}%) — Temp: {temp_hd_texto}"))

            # GPU
            modelo_gpu, memoria_gpu, uso_gpu = obter_info_gpu()
            lbl_gpu.configure(text=f"Modelo: {modelo_gpu} — Memória: {memoria_gpu:.0f} GB GDDR6 — Uso atual: {uso_gpu}%")

            id_after = frame_pai.after(1000, atualizar)
        except:
            pass

    atualizar()
