from bs4 import BeautifulSoup
from zipfile import ZipFile
from lxml import etree
import requests, shutil, os

URL = 'https://googlechromelabs.github.io/chrome-for-testing/'

print('Inicia proceso de descarga de Chromedriver')

request = requests.get(URL)
soup = BeautifulSoup(request.text, 'html.parser')
dom = etree.HTML(str(soup))

node = dom.xpath('//h2[.="Stable"]/following-sibling::div[@class="table-wrapper"]/table//th[.="chromedriver"]/following-sibling::th[.="win64"]/following-sibling::td/code')

os.makedirs('tmp')
with open('./tmp/chromedriver.zip', "wb") as file :
    request = requests.get(node[0].text.strip(), stream=True)
    for chunk in request.iter_content(chunk_size=128):
        file.write(chunk)

input_zip = ZipFile('./tmp/chromedriver.zip')
input_zip.extractall('./tmp')
input_zip.close()

shutil.move('./tmp/chromedriver-win64/chromedriver.exe', './chromedriver.exe')
shutil.rmtree('./tmp')

print('Fin de proceso de descarga de Chromedriver')
