import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()

def test_01_login(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "/inventory.html" in driver.current_url , "Error: Login failed, usuario no se redirigio a /inventory.html"

def test_02_verificar_titulo(driver):

    page_title = driver.title
    section_title = driver.find_element(By.CLASS_NAME, "title").text

    assert page_title == "Swag Labs", f"Error: El titulo es incorrecto, se esperaba 'Swag Labs' pero se obtuvo '{page_title}'"
    assert section_title == "Products", f"Error: El titulo de la sección es incorrecto, se esperaba 'Products' pero se obtuvo '{section_title}'"


def test_03_verificar_producto_existente(driver):

    inventory_item = driver.find_elements(By.CLASS_NAME, "inventory_item")

    assert len(inventory_item) > 0, "Error: No se encontraron productos en inventario"

 