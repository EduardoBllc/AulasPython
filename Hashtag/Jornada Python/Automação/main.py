import pyautogui as pag
from time import sleep
import pandas as pd

pag.PAUSE = 0.3

# Abrindo o Chrome
pag.press("win")
pag.write('Chrome', interval=0)
pag.press('enter')
sleep(1)
pag.hotkey('ctrl', 'l')

# Entrando no site
pag.write(r'https://dlp.hashtagtreinamentos.com/python/intensivao/login', interval=0)
sleep(1)
pag.press('enter')

# Logando no sistema
sleep(1)
pag.press('tab')
pag.write('pythonimpressionador@gmail.com', interval=0)
pag.press('tab')
pag.write('abadabadoo', interval=0)
pag.press('tab')
pag.press('enter')

# Importando a base dados
base_dados = pd.read_csv('produtos.csv')

# Inserindo os dados
for linha in base_dados.index:
    sleep(1)
    pag.click(x=425, y=273) # Clicando no primeiro campo
    pag.write(str(base_dados.loc[linha, 'codigo'])) # Campo código
    pag.press('tab')
    pag.write(str(base_dados.loc[linha,'marca'])) # Campo marca
    pag.press('tab')
    pag.write(str(base_dados.loc[linha,'tipo'])) # Campo tipo
    pag.press('tab')
    pag.write(str(base_dados.loc[linha,'categoria'])) # Campo categoria
    pag.press('tab')
    pag.write(str(base_dados.loc[linha,'preco_unitario'])) # Campo preco_unitario
    pag.press('tab')
    pag.write(str(base_dados.loc[linha,'custo'])) # Campo custo
    pag.press('tab')
    if not pd.isna(base_dados.loc[linha,'obs']):
        pag.write(str(base_dados.loc[linha,'obs'])) # Campo obs
    pag.press('tab')
    pag.press('enter') # Clicando enviar
    pag.scroll(2000) # Scrollando pra cima
