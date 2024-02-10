from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

driver = webdriver.Chrome()
driver.get("https://www.terabyteshop.com.br")

titulos = driver.find_elements(By.XPATH, "//a[@class='prod-name']")
precos = driver.find_elements(By.XPATH, "//div[@class='prod-new-price']")
#cria a planilha
Workbook = openpyxl.Workbook()
#cria a pagina produtos
Workbook.create_sheet("Produtos")
# seleciona a pagina produtos
sheet_produtos = Workbook["Produtos"]
sheet_produtos["A1"].value = "Produto"
sheet_produtos["B1"].value = "Preço"


for titulo, preco in zip(titulos, precos):
  sheet_produtos.append([titulo.text,preco.text])
  
Workbook.save("produto.xlsx")