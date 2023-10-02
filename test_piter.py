import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()  


driver.get("https://piter-online.net/")

# В поиске ввести улицу Тестовая линия, дом 1
search_box = driver.find_element_by_class_name( "app142 app151 app149 app148 app144 app161 app143")
search_box.send_keys("Тестовая линия")
search_box = driver.find_element_by_class_name( "app142 app149 app148 app144 app161")
search_box.send_keys("1")
dropdown = Select(driver.find_element_by_class_name("app163 app175"))
dropdown.select_by_class_name("app187")
button = driver.find_element_by_class_name("app206 app239 app235 app230 app219 app236")
button.click()

# На открывшейся странице кликнуть на "подключить" или "подключить по акции" на тарифе
button1 = driver.find_element_by_class_name("app893")
button1.click()

tariff_links = driver.find_elements(By.XPATH, "//a[contains(@href, '/tariff/') and (text()='Подключить' or text()='Подключить по акции')]")
if tariff_links:
    tariff_links[0].click()
else:
    print("Ссылка на тариф не найдена")

# Ожидание загрузки страницы с формой
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.NAME, "tel")))

# Отправить заявку пять раз
for i in range(5):
    # Заполнить форму
   
    phone_field = driver.find_element(By.NAME, "tel")

    phone_field.send_keys("1111111111")

    # Отправить форму
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    # Ожидание ответа сервера (статус 201)
    response_status = driver.execute_script("return performance.getEntries()[0].response.status")
    if response_status == 201:
        print(f"Заявка {i + 1} отправлена успешно (статус 201)")
    else:
        print(f"Ошибка при отправке заявки {i + 1} (статус {response_status})")

    # Очистить поля формы
    name_field.clear()
    phone_field.clear()

# Закрыть браузер после выполнения всех действий
driver.quit()
