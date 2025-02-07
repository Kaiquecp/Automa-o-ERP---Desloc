import pyautogui
import pandas as pd
import time
import tkinter as tk
from tkinter import messagebox

df = pd.read_excel(r'C:\Users\user\Documents\DESLOCVAZ.xlsx')

coordenadas_codigo = (171, 183)
coordenadas_aba_dados_veiculo = (78, 156)
coordenadas_aba_parametros_veiculo = (253, 159)
coordenadas_checkbox = (193, 572)
coordenadas_motorista_fixo = (149, 403)
cor_checkbox_marcado = (0, 0, 0)

def verificar_checkbox(coordenadas):
    cor_pixel = pyautogui.pixel(coordenadas[0], coordenadas[1])
    if cor_pixel == cor_checkbox_marcado:
        print("Checkbox está marcado.")
        return True
    else:
        print("Checkbox está desmarcado.")
        return False
def aguardar_localizar_imagem(imagem, timeout=30):
    start_time = time.time()
    pos = None
    while pos is None:
        try:
            pos = pyautogui.locateOnScreen(imagem, confidence=0.7, grayscale=True)
        except Exception as e:
            print(f"Erro ao localizar a imagem: {e}")
        if time.time() - start_time > timeout:
            raise Exception(f"Imagem {imagem} não encontrada dentro do tempo limite.")
    return pos
    
def exibir_janela_concluido():
    root = tk.Tk()
    root.withdraw() 
    messagebox.showinfo("Processo Concluído", "O processo foi concluído com sucesso!")
    root.destroy()

caminho_imagens = r'C:\Users\Kaique\Documents\codigos\automacao_datapar'

try:
    aguardar_localizar_imagem(f'{caminho_imagens}\\campo_codigo.png')
    print("Campo 'Código' encontrado. Iniciando o processo.")
except Exception as e:
    print(e)
    print("Campo 'Código' não encontrado. O processo será interrompido.")
    exit()

for index, row in df.iterrows():
    codvei = str(row['CODVEI']).strip() if pd.notnull(row['CODVEI']) else ''
    
    if codvei:
        pyautogui.click(coordenadas_codigo)
        time.sleep(0.1)
        pyautogui.doubleClick()
        time.sleep(0.1)
        pyautogui.press('delete')
        pyautogui.press('backspace', presses=10)
        pyautogui.typewrite(codvei)
        pyautogui.press('enter')
        time.sleep(5)
        if verificar_checkbox(coordenadas_motorista_fixo):
            pyautogui.click(coordenadas_motorista_fixo)
            time.sleep(1)
        pyautogui.click(coordenadas_aba_parametros_veiculo)
        time.sleep(2)

        if verificar_checkbox(coordenadas_checkbox):
            pyautogui.click(coordenadas_checkbox)
            time.sleep(1)
            try:
                botao_salvar = aguardar_localizar_imagem(f'{caminho_imagens}\\botao_salvar.png')
                pyautogui.click(botao_salvar)
            except Exception as e:
                print(e)
                print("Erro ao localizar o botão 'Salvar'.")
            time.sleep(5)
            pyautogui.press('enter')
            time.sleep(2)
        pyautogui.click(coordenadas_aba_dados_veiculo)
        time.sleep(2)
exibir_janela_concluido()
print("Processo concluído.")
