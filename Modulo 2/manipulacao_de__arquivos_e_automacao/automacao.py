import pyautogui as pg


pg.mouseinfo #abre a janela para coordenadas

pg.moveTo(150, 100, duration=1.5)
pg.moveTo(150, 100, duration=1.5)

pg.press('win') #pressiona o windows

pg.sleep(1)

pg.write('chrome', interval= 0.5) #escreve no menu

pg.press("enter") #pressiona enter
pg.sleep(2)
pg.write('www.youtube.com') #escreve o site
pg.press("enter") #pressiona enter

# move o mouse para a barra de pesquisa do youtube
pg.moveTo(702, 119, duration=0.5)
pg.sleep(2)
pg.click()

pg.write('queen - bohemian rhapsody )', interval=0.5)
pg.press('enter')

#pg.mouseInfo() 

pg.moveTo(787, 586)
pg.click()