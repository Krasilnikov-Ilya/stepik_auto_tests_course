from selenium import webdriver
import time        # здравствуй!

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/registration1.html') # это первая форма
    input1 = browser.find_element_by_css_selector("input[required].first").send_keys("Ivan") # составные CSS селекторы уникальны
    input2 = browser.find_element_by_css_selector("input[required].second").send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("input[required].third").send_keys("mail@mail.com") 
    button = browser.find_element_by_css_selector("button.btn").click() # я не стал заполнять необязательные поля, условия задачи этого не требуют
    time.sleep(5)
    assert "Congratulations! You have successfully registered!" == welcome_text
    
finally:
    time.sleep(5)  # посмотри какой я молодец
    browser.quit() # ещё не всё, это только половина
    
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/registration2.html') # это вторая форма
    input1 = browser.find_element_by_css_selector("input[required].first").send_keys("Ivan") 
    input2 = browser.find_element_by_css_selector("input[required].second").send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("input[required].third").send_keys("mail@mail.com")
    button = browser.find_element_by_css_selector("button.btn").click()
    time.sleep(5)
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)  # не проходит именно второй элемент, потому что его нет во второй форме
    browser.quit() # загляни в командную строку, там будет нужная ошибка по нужному элементу
    # в последней строке ты увидишь:
    # selenium.common.exceptions.NoSuchElementException:
    # Message: no such element: Unable to locate element: 
    # {"method":"css selector","selector":"input[required].second"}
    # (Session info: chrome=100.0.4896.127)
    