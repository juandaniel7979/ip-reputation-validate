import csv
import os

from bs4 import BeautifulSoup
import pandas as pd

class Extracciones:
    def VT(page,ip):
        selector='#detections'
        html = page.inner_html("#detections")
        soup = BeautifulSoup(html, 'lxml')
        title = page.wait_for_selector(selector)
        detecciones = soup.find_all('span', class_="engine-name")
        categorias = soup.find_all('span', class_="individual-detection")
        motor = []
        reputacion = []
        # print(len(detecciones))
        for i in range(len(detecciones)):
            motor.append(detecciones[i].getText())
            reputacion.append(categorias[i].getText())

        # saving the dataframe
        df = pd.DataFrame()
        df['motor']=motor
        df['reputacion']=reputacion
        # print(df)
        
        #Creando el directorio con la información asociada a cada ip
        temp_ip=ip.replace(".","_")
        outname = f'VT_{temp_ip}.csv'
        outdir = f'./ip-info/{temp_ip}'
        if not os.path.exists(outdir):
            os.mkdir(outdir)
        fullname = os.path.join(outdir, outname)    
        df.to_csv(f'{fullname}', encoding='utf-8', index=False, mode='w+')
    
    
    def TI(page,ip):
        selector='//*[@id="location-data-wrapper"]/table/tr/td'

        #Creando el directorio con la información asociada a cada ip
        temp_ip=ip.replace(".","_")
        outname = f'TI_{temp_ip}.csv'
        outdir = f'./ip-info/{temp_ip}'
        if not os.path.exists(outdir):
            os.mkdir(outdir)
            fullname = os.path.join(outdir, outname)  
            html = page.inner_html("#blocklist-data-wrapper")
            soup = BeautifulSoup(html, 'lxml')
            title = page.wait_for_selector(selector)
            # //*[@id="location-data-wrapper"]/table/tr/td'
            lista_negra = soup.find_all('td', class_="chart-data-label col_left")
            deteccion = soup.find_all('td', attrs={"class": None})
            print(deteccion)
            blocklist = []
            reputacion = []
            for i in range(len(lista_negra)):
                blocklist.append(lista_negra[i].getText())
            for i in range(len(deteccion)):
                if 'span' in deteccion[i]:
                    reputacion.append(deteccion[i].find('span').getText())
                else:
                    reputacion.append(deteccion[i].getText())
            # print(blocklist)
            # print(reputacion)
            if "" in reputacion:
                reputacion.remove("")
            # # saving the dataframe
            df = pd.DataFrame()
            df['blocklist']=blocklist
            df['reputacion']=reputacion
            print(df)
            df.to_csv(f'{fullname}', encoding='utf-8', index=False, mode='w+')
        else:
            print('Esta ip ya se analizó')