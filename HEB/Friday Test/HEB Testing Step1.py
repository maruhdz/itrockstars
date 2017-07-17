from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
driver.delete_all_cookies()

#SEARCH AND OPEN WEBPAGE
driver.get("http://www.heb.com.mx/")

#CLOSING POPUP ABOUT COOKIES
close_popup = driver.find_element_by_css_selector("#hs-eu-confirmation-button").click()

#SCROLL DOWN
driver.execute_script("window.scrollTo(0, 1800);")

#ASSERT AND CONCATENATE RECOMENDACION DE LA SEMANA
search_text_r = driver.find_element_by_xpath(".//*[@id='top']/body/div[2]/div/div[5]/div/div/div[1]/h1").text
assert "Recomendación de la semana" in search_text_r;
search_text_o = driver.find_element_by_xpath(".//*[@id='top']/body/div[2]/div/div[5]/div/div/div[2]/div[1]/h2[1]").text
recommend_offer_text = "La " + search_text_r + " es: " + search_text_o;
print(recommend_offer_text)

#SCROLL UP
driver.execute_script("window.scrollTo(0, -1800);")

#SEARCH OF 1ST ITEM
select_combo = driver.find_element_by_xpath(".//*[@id='select-categories']").text
combo_elements = driver.find_elements_by_xpath(".//*[@id='select-categories']/option")
for i in range(len(combo_elements)):
    if combo_elements[i].text == "Tecnología":
        combo_elements[i].click()
        break

search_field = driver.find_element_by_css_selector("#search")
search_field.send_keys("Samsung Smart TV")
search_field.send_keys(Keys.ENTER)

#LISTING, SORTING, AND OPRION SELECTING
select_listado = driver.find_element_by_xpath(".//*[@id='top']/body/div[1]/div/div[4]/div/div[2]/div[2]/div[2]/div[1]/div[2]/p[1]/a").click()

select_combo2 = driver.find_element_by_xpath(".//*[@id='top']/body/div[1]/div/div[4]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/select").text
combo_elements2 = driver.find_elements_by_xpath(".//*[@id='top']/body/div[1]/div/div[4]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/select/option")
for i in range(len(combo_elements2)):
    if combo_elements2[i].text == "Precio ▼":
        combo_elements2[i].click()
        break

#SEARCH RESULT VALIDATION
search_result = (driver.find_elements_by_xpath(".//*[@id='products-list']/li"))
if (len(search_result)) > 1:
    print ("Si existen resultados..")
else:
    print ("No existen resultados..")

#SEARCH FOR ITEM IN RESULTS, ADDING 2 TO CART
search_result_tv = (driver.find_elements_by_xpath(".//*[@id='products-list']"))
search_result_name = (driver.find_elements_by_css_selector(".product-name>a"))
search_buttons = (driver.find_elements_by_css_selector("#addcart-listmode"))
x = 0
for i in search_result_name:
    if i.text == "Tv Led 55 Full Hd Smart Tv**":
       break
    x = x + 1
driver.execute_script("window.scrollTo(0, 900);")
sleep(4)
quantity = (driver.find_element_by_xpath(".//*[@id='plus-420517']")).click()
y = 0
for b in search_buttons:
    if y == x:
        b.click()
        break
    y = y + 1
sleep(5)

#CLOSE POPUP STORES
close_popup2 = driver.find_element_by_xpath(".//*[@id='closeBtn']").click()

#VALIDATE THERE ARE ITEMS IN THE CART
validate_carrito = driver.find_element_by_xpath(".//*[@id='top']/body/div[1]/div/div[4]/div/div[2]/div[2]/ul[2]/li/ul/li/span").text
assert "se agregó al carrito" in validate_carrito;
print(validate_carrito)

#NUM OF ITEMS IN THE CART
cart_number = driver.find_element_by_xpath(".//*[@id='gotocar']/div/a/span[3]").text
print ("The cart has: " + cart_number + " items.")

#OPEN CART MENU AND SELECTING PURCHASE
cart_icon = driver.find_element_by_xpath(".//*[@id='gotocar']/div/a/span[1]").click()
cart_name = driver.find_element_by_xpath(".//*[@id='gotocar']/div/a/span[2]").click()
sleep(2)
indiv_price = driver.find_element_by_xpath(".//*[@id='cart-sidebar']/li/div/table[1]/tbody/tr/td/span").text
print (indiv_price)

cart_pur = driver.find_element_by_xpath(".//*[@id='btnMinicart']").click()
sleep(3)
cart2 = driver.find_element_by_css_selector("#car_heb_head").click()

#POPUP STORE SELECTION
popup_store = driver.find_element_by_xpath(".//*[@id='selectStore']").text
popup_store_combo = driver.find_elements_by_xpath(".//*[@id='selectStore']/option")
sleep(1)
for i in range(len(popup_store_combo)):
    if popup_store_combo[i].text == "HEB Valle Oriente":
        popup_store_combo[i].click()
        break
    sleep(1)
popup_store_button = driver.find_element_by_xpath(".//*[@id='sbmStoreSelect']").click()
sleep(3)
driver.execute_script("window.history.go(-1)")
sleep(1)

#VALIDATE THERE ARE NO ITEMS IN THE CART
validate_carrito_vacio = driver.find_element_by_xpath(".//*[@id='top']/body/div[1]/div/div[4]/div/div/div[1]/h1").text
assert "vacío" in validate_carrito_vacio;
print(validate_carrito_vacio)

#END OF FIRST ITEM






#SEARCH OF 2ND ITEM
select_combom = driver.find_element_by_xpath(".//*[@id='select-categories']").text
combo_elementsm = driver.find_elements_by_xpath(".//*[@id='select-categories']/option")
for i in range(len(combo_elementsm)):
    if combo_elementsm[i].text == "Súper":
        combo_elementsm[i].click()
        break

search_field = driver.find_element_by_css_selector("#search")
search_field.send_keys("Mazapan")
search_field.send_keys(Keys.ENTER)

#LISTING, SORTING, AND OPRION SELECTING
select_listadom = driver.find_element_by_xpath(".//*[@id='top']/body/div[1]/div/div[4]/div/div[2]/div[2]/div[2]/div[1]/div[2]/p[1]/a").click()

select_combo2m = driver.find_element_by_xpath(".//*[@id='top']/body/div[1]/div/div[4]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/select").text
combo_elements2m = driver.find_elements_by_xpath(".//*[@id='top']/body/div[1]/div/div[4]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/select/option")
for i in range(len(combo_elements2m)):
    if combo_elements2m[i].text == "Precio ▼":
        combo_elements2m[i].click()
        break

#SEARCH RESULT VALIDATION
search_result2 = (driver.find_elements_by_xpath(".//*[@id='products-list']/li"))
if (len(search_result2)) > 1:
    print ("Si existen resultados..")
else:
    print ("No existen resultados..")

#SEARCH FOR ITEM IN RESULTS, ADDING 2 TO CART
search_result_tv2 = (driver.find_elements_by_xpath(".//*[@id='products-list']"))
search_result_name2 = (driver.find_elements_by_css_selector(".product-name>a"))
search_buttons2 = (driver.find_elements_by_css_selector("#addcart-listmode"))
x = 0
for i in search_result_name2:
    if i.text == "Mazapan Stevia Variedad":
       break
    x = x + 1
sleep(4)
quantity2 = (driver.find_element_by_xpath(".//*[@id='plus-367043']")).click()
y = 0
for b in search_buttons2:
    if y == x:
        b.click()
        break
    y = y + 1
sleep(5)

#VALIDATE THERE ARE ITEMS IN THE CART
validate_carrito2 = driver.find_element_by_xpath(".//*[@id='top']/body/div[1]/div/div[4]/div/div[2]/div[2]/ul[2]/li/ul/li/span").text
assert "se agregó al carrito" in validate_carrito2;
print(validate_carrito2)

#NUM OF ITEMS IN THE CART
cart_number2 = driver.find_element_by_xpath(".//*[@id='gotocar']/div/a/span[3]").text
print ("The cart has: " + cart_number2 + " items.")

#OPEN CART MENU AND SELECTING PURCHASE
cart_name2 = driver.find_element_by_xpath(".//*[@id='gotocar']/div/a/span[2]").click()
sleep(2)
indiv_price2 = driver.find_element_by_xpath(".//*[@id='cart-sidebar']/li/div/table[1]/tbody/tr/td/span").text
print (indiv_price2)
sleep(2)
cart_pur2 = driver.find_element_by_xpath(".//*[@id='btnMinicart']").click()
cart22 = driver.find_element_by_css_selector("#car_heb_head").click()
sleep(5)

#HOLA CARACOLA
#comment = driver.find_element_by_xpath(".//*[@id='cart[7201523][comanda]']")
#comment.clear()
#comment.send_keys("Hola Caracola!")

#SCREENSHOT
driver.get_screenshot_as_png()
driver.save_screenshot('screenshot.png')


