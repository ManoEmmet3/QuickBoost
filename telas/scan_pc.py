import customtkinter as ctk
from PIL import Image
from pathlib import Path
import platform
import psutil
import wmi  # pip install wmi

def pegar_temperatura_cpu():
    try:
        w = wmi.WMI(namespace="root\\wmi")
        temps = w.MSAcpi_ThermalZoneTemperature()
        for t in temps:
            celsius = (t.CurrentTemperature / 10) - 273.15
            if celsius > 0:
                return celsius
    except:
        pass
    return None

def cor_por_valor(valor, tipo="uso"):
    if tipo == "uso":
        if valor <= 50: return "#00FF00"
        elif valor <= 75: return "#FFFF00"
        else: return "#FF0000"
    else:
        if valor <= 50: return "#00FF00"
        elif valor <= 70: return "#FFFF00"
        else: return "#FF0000"

def obter_nome_cpu():
    nome = platform.processor() or "Desconhecido"
    freq = psutil.cpu_freq()
    if freq:
        nome += f" @ {freq.current/1000:.2f}GHz"
    return nome

def obter_so_formatado():
    so = platform.system()
    versao = platform.release()
    arch = platform.machine()
    return f"{so} {versao} {arch}"

def mostrar(frame_pai):
    for w in frame_pai.winfo_children():
        w.destroy()

    caminho_assets = Path(__file__).parent.parent / "assets"
    icone_win = ctk.CTkImage(Image.open(caminho_assets / "windows.png"), Image.open(caminho_assets / "windows.png"), size=(25,25))
    icone_cpu = ctk.CTkImage(Image.open(caminho_assets / "cpu.png"), Image.open(caminho_assets / "cpu.png"), size=(25,25))

    # Frame SO
    frame_so = ctk.CTkFrame(frame_pai, fg_color="transparent")
    frame_so.place(x=27, y=25)
    ctk.CTkLabel(frame_so, image=icone_win, text="").grid(row=0, column=0, rowspan=2, sticky="n")
    ctk.CTkLabel(frame_so, text="Sistema Operacional", text_color="#9375FF", font=("Inter",15)).grid(row=0,column=1, sticky="w", padx=(20,0))
    ctk.CTkLabel(frame_so, text=obter_so_formatado(), text_color="#fff", font=("Inter",13)).grid(row=1,column=1, sticky="w", padx=(50,0))
    frame_so.update_idletasks()

    # Frame CPU
    frame_cpu = ctk.CTkFrame(frame_pai, fg_color="transparent")
    frame_cpu.place(x=27, y=frame_so.winfo_height() + 45)
    ctk.CTkLabel(frame_cpu, image=icone_cpu, text="").grid(row=0,column=0, sticky="n")
    ctk.CTkLabel(frame_cpu, text="CPU", text_color="#9375FF", font=("Inter",15)).grid(row=0,column=1, sticky="w", padx=(20,0))

    # Labels do texto da CPU com cores dinâmicas só em uso e temp
    ctk.CTkLabel(frame_cpu, text="CPU: ", text_color="#fff", font=("Inter",13)).grid(row=1,column=1, sticky="w", padx=(50,0))
    nome_cpu_lbl = ctk.CTkLabel(frame_cpu, text=obter_nome_cpu(), text_color="#fff", font=("Inter",13))
    nome_cpu_lbl.grid(row=1,column=2, sticky="w")
    ctk.CTkLabel(frame_cpu, text=" — Uso: ", text_color="#fff", font=("Inter",13)).grid(row=1,column=3, sticky="w")
    uso_lbl = ctk.CTkLabel(frame_cpu, text="0%", text_color="#0f0", font=("Inter",13))
    uso_lbl.grid(row=1,column=4, sticky="w")
    ctk.CTkLabel(frame_cpu, text=" — Temp: ", text_color="#fff", font=("Inter",13)).grid(row=1,column=5, sticky="w")
    temp_lbl = ctk.CTkLabel(frame_cpu, text="0°C", text_color="#0f0", font=("Inter",13))
    temp_lbl.grid(row=1,column=6, sticky="w")

    def atualizar():
        uso = psutil.cpu_percent(interval=None)
        temp = pegar_temperatura_cpu()
        nome_cpu_lbl.configure(text=obter_nome_cpu())
        uso_lbl.configure(text=f"{uso:.0f}%", text_color=cor_por_valor(uso, "uso"))
        if temp is None:
            temp_lbl.configure(text="N/A", text_color="#fff")
        else:
            temp_lbl.configure(text=f"{temp:.0f}°C", text_color=cor_por_valor(temp, "temp"))
        frame_pai.after(1000, atualizar)

    atualizar()
