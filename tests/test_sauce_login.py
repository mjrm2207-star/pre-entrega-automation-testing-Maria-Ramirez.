import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")

    assert len(productos) > 0, f"Error: No se encontraron productos en el inventario"


    primer_producto = productos[0]

    assert primer_producto.is_displayed(), ("Error: El primer producto no está visible")


    nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text

    precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert nombre.strip() != "", ("Error: El primer producto no muestra su nombre")

    assert precio.strip() != "", ("Error: El primer producto no muestra su precio")

    print(f"\nPrimer producto: {nombre} | Precio: {precio}")


def test_04_verificar_elementos_interfaz(driver):
    menu = driver.find_element(By.ID, "react-burger-menu-btn")

    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")

    assert menu.is_displayed(), f"Error: El botón del menú no está visible"

    assert filtro.is_displayed(), f"Error: El filtro de productos no está visible"

def test_05_verificar_agregar_producto_al_carrito(driver):
    
    wait = WebDriverWait(driver, 10)
    
    boton_locator = (By.CSS_SELECTOR, ".inventory_item:first-child button")
    carrito_locator = (By.CLASS_NAME, "shopping_cart_badge")

    boton_agregar = wait.until(EC.element_to_be_clickable(boton_locator))
    boton_agregar.click()

    # Volver a localizar el botón después de que la página se actualice.
    wait.until(
        EC.text_to_be_present_in_element(boton_locator, "Remove"),
        "Error: El botón no cambió a 'Remove' después de agregar el producto",
    )
    boton_actualizado = driver.find_element(*boton_locator)
    assert boton_actualizado.text.strip() == "Remove", (
        "Error: El botón no cambió a 'Remove' después de agregar el producto"
    )
def test_06_verificar_contador_carrito(driver):
    
    wait = WebDriverWait(driver, 10) 

    contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert contador_carrito == "1", f"Error: El contador del carrito debería mostrar '1' pero muestra '{contador_carrito}'"

def test_07_navegar_carrito(driver):
    
    wait = WebDriverWait(driver, 10) 

    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    carrito.click()

    wait.until(EC.url_contains("/cart.html"), "Error: No se redirigió a la página del carrito")

    assert "/cart.html" in driver.current_url, "Error: No se redirigió a la página del carrito"    

def test_08_verificar_producto_en_carrito(driver):
    wait = WebDriverWait(driver, 10) 

    productos_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")

    assert len(productos_carrito) > 0, "Error: No se encontraron productos en el carrito"

    primer_producto_carrito = productos_carrito[0]

    nombre_carrito = primer_producto_carrito.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio_carrito = primer_producto_carrito.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert nombre_carrito.strip() != "", "Error: El primer producto en el carrito no muestra su nombre"
    assert precio_carrito.strip() != "", "Error: El primer producto en el carrito no muestra su precio"

    print(f"\nPrimer producto en el carrito: {nombre_carrito} | Precio: {precio_carrito}")