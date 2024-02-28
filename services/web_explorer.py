import os

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

from helpers.extractions import Extracciones as extractions


class WebExplorer:

    def openURL_VT(ip):
        with sync_playwright() as p:
            url=f'https://www.virustotal.com/gui/search/{ip}'
            browser = p.firefox.launch(headless=True)
            page = browser.new_page()

            max_intentos = 3
            intento_actual = 1

            while intento_actual <= max_intentos:
                try:
                    page.goto(url)
                    extractions.VT(page,ip)
                    #Guardar archivo
                    temp_ip=ip.replace(".","_")
                    page.screenshot(path=f'./ip-info/{temp_ip}/{temp_ip}.jpg')
                    # browser.close()

                except TimeoutError as e:
                    print(f"Error de tiempo de espera: {e}")
                    page.screenshot(path=f'./errors/error_{temp_ip}.jpg')

                    # Incrementar el número de intentos
                    intento_actual += 1
                    # Volver a intentarlo después de un tiempo de espera (puedes ajustar esto)
                    page.wait_for_timeout(5000)
            # Cerrar el navegador
            browser.close()


    
    def openURL_TI(ip):
        temp_ip=ip.replace(".","_")
        outname = f'TI_{temp_ip}.csv'
        outdir = f'./ip-info/{temp_ip}'
        if not os.path.exists(outdir):
            os.mkdir(outdir)

        with sync_playwright() as p:
            url=f'https://talosintelligence.com/reputation_center/lookup?search={ip}'
            browser = p.firefox.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            max_intentos = 3
            intento_actual = 1

            while intento_actual <= max_intentos:
                try:
                    page.goto(url)

                    page.wait_for_timeout(5000)
                    page.mouse.wheel(0,400)
                    #Extraer datos con BeautifulSoup
                    extractions.TI(page,ip)
                    #Guardar archivo
                    temp_ip=ip.replace(".","_")
                    page.screenshot(path=f'./ip-info/{temp_ip}/TI_{temp_ip}.jpg')
                except TimeoutError as e:
                    print(f"Error de tiempo de espera: {e}")

                    # Incrementar el número de intentos
                    intento_actual += 1

                    # Volver a intentarlo después de un tiempo de espera (puedes ajustar esto)
                    page.wait_for_timeout(5000)
            browser.close()
    
    def getBlackListURL(ip):
        # bl = [{"url":f'https://www.virustotal.com/gui/search/{ip}', "selector":"//*[@id="location-data-wrapper"]/table/tr/td"},{"url":f'https://talosintelligence.com/reputation_center/lookup?search={ip}',"selector":"//*[@id="location-data-wrapper"]/table/tr/td"},{"url":f'https://mxtoolbox.com/SuperTool.aspx?action=mx%3a{ip}&run=toolpage', "selector":"//*[@id="location-data-wrapper"]/table/tr/td"}]
        bl = {"TI":{"url":f'https://talosintelligence.com/reputation_center/lookup?search={ip}',"selector":'//*[@id="location-data-wrapper"]/table/tr/td'},"VT":{"url":f'https://www.virustotal.com/gui/search/{ip}', "selector":'//*#detections/div'},"MX":{"url":f'https://mxtoolbox.com/SuperTool.aspx?action=mx%3a{ip}&run=toolpage', "selector":'//*[@id="location-data-wrapper"]/table/tr/td'}}
        return bl,ip