from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class heb(object):

    def search_smarttv(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()

        #SEARCH AND OPEN WEBPAGE
        self.driver.get("http://www.heb.com.mx/")

        #CLOSING POPUP ABOUT COOKIES
        self.close_popup = self.driver.find_element_by_css_selector("#hs-eu-confirmation-button").click()

        #SCROLL DOWN
        self.driver.execute_script("window.scrollTo(0, 1800);")

        #ASSERT AND CONCATENATE RECOMENDACION DE LA SEMANA
        self.search_text_r = self.driver.find_element_by_xpath(".//*[@id='top']/body/div[2]/div/div[5]/div/div/div[1]/h1").text
        assert "Recomendación de la semana" in self.search_text_r;
        self.search_text_o = self.driver.find_element_by_xpath(".//*[@id='top']/body/div[2]/div/div[5]/div/div/div[2]/div[1]/h2[1]").text
        self.recommend_offer_text = ("La " + self.search_text_r + " es: " + self.search_text_o)
        print(self.recommend_offer_text)

        #SCROLL UP
        self.driver.execute_script("window.scrollTo(0, -1800);")

        #SEARCH OF 1ST ITEM
        self.select_combo = self.driver.find_element_by_xpath(".//*[@id='select-categories']").text
        self.combo_elements = self.driver.find_elements_by_xpath(".//*[@id='select-categories']/option")
        for i in range(len(self.combo_elements)):
            if self.combo_elements[i].text == "Tecnología":
                self.combo_elements[i].click()
                break

        self.search_field = self.driver.find_element_by_css_selector("#search")
        self.search_field.send_keys("Samsung Smart TV")
        self.search_field.send_keys(Keys.ENTER)

        #LISTING, SORTING, AND OPRION SELECTING
        self.select_listado = self.driver.find_element_by_xpath(".//*[@id='top']/body/div[1]/div/div[4]/div/div[2]/div[2]/div[2]/div[1]/div[2]/p[1]/a").click()

        self.select_combo2 = self.driver.find_element_by_xpath(".//*[@id='top']/body/div[1]/div/div[4]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/select").text
        self.combo_elements2 = self.driver.find_elements_by_xpath(".//*[@id='top']/body/div[1]/div/div[4]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/select/option")
        for i in range(len(self.combo_elements2)):
            if self.combo_elements2[i].text == "Precio ▼":
                self.combo_elements2[i].click()
                break

        #SEARCH RESULT VALIDATION
        self.search_result = (self.driver.find_elements_by_xpath(".//*[@id='products-list']/li"))
        if (len(self.search_result)) > 1:
            print ("Si existen resultados..")
        else:
            print ("No existen resultados..")

        #SEARCH FOR ITEM IN RESULTS, ADDING 2 TO CART
        self.search_result_tv = (self.driver.find_elements_by_xpath(".//*[@id='products-list']"))
        self.search_result_name = (self.driver.find_elements_by_css_selector(".product-name>a"))
        self.search_buttons = (self.driver.find_elements_by_css_selector("#addcart-listmode"))
        x = 0
        for i in self.search_result_name:
            if i.text == "Tv Led 55 Full Hd Smart Tv**":
               break
            x = x + 1
            self.driver.execute_script("window.scrollTo(0, 900);")
        sleep(4)
        quantity = (self.driver.find_element_by_xpath(".//*[@id='plus-420517']")).click()
        y = 0
        for b in self.search_buttons:
            if y == x:
                b.click()
                break
            y = y + 1
        sleep(5)

        #CLOSE POPUP STORES
        self.close_popup2 = self.driver.find_element_by_xpath(".//*[@id='closeBtn']").click()

        #VALIDATE THERE ARE ITEMS IN THE CART
        self.validate_carrito = self.driver.find_element_by_xpath(".//*[@id='top']/body/div[1]/div/div[4]/div/div[2]/div[2]/ul[2]/li/ul/li/span").text
        assert "se agregó al carrito" in self.validate_carrito;
        print(self.validate_carrito)

        #NUM OF ITEMS IN THE CART
        self.cart_number = self.driver.find_element_by_xpath(".//*[@id='gotocar']/div/a/span[3]").text
        print ("The cart has: " + self.cart_number + " items.")

        #OPEN CART MENU AND SELECTING PURCHASE
        self.cart_icon = self.driver.find_element_by_xpath(".//*[@id='gotocar']/div/a/span[1]").click()
        self.cart_name = self.driver.find_element_by_xpath(".//*[@id='gotocar']/div/a/span[2]").click()
        sleep(2)
        #indiv_price = driver.find_element_by_xpath(".//*[@id='cart-sidebar']/li/div/table[1]/tbody/tr/td/span").text
        #print (indiv_price)
        #sleep(2)
        self.cart_pur = self.driver.find_element_by_xpath(".//*[@id='btnMinicart']").click()
        self.cart2 = self.driver.find_element_by_css_selector("#car_heb_head").click()

        #POPUP STORE SELECTION
        self.popup_store = self.driver.find_element_by_xpath(".//*[@id='selectStore']").text
        self.popup_store_combo = self.driver.find_elements_by_xpath(".//*[@id='selectStore']/option")
        sleep(1)
        for i in range(len(self.popup_store_combo)):
            if self.popup_store_combo[i].text == "HEB Valle Oriente":
                self.popup_store_combo[i].click()
                break
            sleep(1)
        self.popup_store_button = self.driver.find_element_by_xpath(".//*[@id='sbmStoreSelect']").click()
        sleep(3)
        self.driver.execute_script("window.history.go(-1)")
        sleep(1)

        #VALIDATE THERE ARE NO ITEMS IN THE CART
        self.validate_carrito_vacio = self.driver.find_element_by_xpath(".//*[@id='top']/body/div[1]/div/div[4]/div/div/div[1]/h1").text
        assert "vacío" in self.validate_carrito_vacio;
        print(self.validate_carrito_vacio)

        #END OF FIRST ITEM





    def search_mazapan(self):
        #SEARCH OF 2ND ITEM
        self.select_combom = self.driver.find_element_by_xpath(".//*[@id='select-categories']").text
        self.combo_elementsm = self.driver.find_elements_by_xpath(".//*[@id='select-categories']/option")
        for i in range(len(self.combo_elementsm)):
            if self.combo_elementsm[i].text == "Súper":
                self.combo_elementsm[i].click()
                break

        self.search_field = self.driver.find_element_by_css_selector("#search")
        self.search_field.send_keys("Mazapan")
        self.search_field.send_keys(Keys.ENTER)

        #LISTING, SORTING, AND OPRION SELECTING
        self.select_listadom = self.driver.find_element_by_xpath(".//*[@id='top']/body/div[1]/div/div[4]/div/div[2]/div[2]/div[2]/div[1]/div[2]/p[1]/a").click()

        self.select_combo2m = self.driver.find_element_by_xpath(".//*[@id='top']/body/div[1]/div/div[4]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/select").text
        self.combo_elements2m = self.driver.find_elements_by_xpath(".//*[@id='top']/body/div[1]/div/div[4]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/select/option")
        for i in range(len(self.combo_elements2m)):
            if self.combo_elements2m[i].text == "Precio ▼":
                self.combo_elements2m[i].click()
                break

        #SEARCH RESULT VALIDATION
        self.search_result2 = (self.driver.find_elements_by_xpath(".//*[@id='products-list']/li"))
        if (len(self.search_result2)) > 1:
            print ("Si existen resultados..")
        else:
            print ("No existen resultados..")

        #SEARCH FOR ITEM IN RESULTS, ADDING 2 TO CART
        self.search_result_tv2 = (self.driver.find_elements_by_xpath(".//*[@id='products-list']"))
        self.search_result_name2 = (self.driver.find_elements_by_css_selector(".product-name>a"))
        self.search_buttons2 = (self.driver.find_elements_by_css_selector("#addcart-listmode"))
        x = 0
        for i in self.search_result_name2:
            if i.text == "Mazapan Stevia Variedad":
               break
            x = x + 1
        sleep(4)
        self.quantity2 = (self.driver.find_element_by_xpath(".//*[@id='plus-367043']")).click()
        y = 0
        for b in self.search_buttons2:
            if y == x:
                b.click()
                break
            y = y + 1
        sleep(5)

        #VALIDATE THERE ARE ITEMS IN THE CART
        self.validate_carrito2 = self.driver.find_element_by_xpath(".//*[@id='top']/body/div[1]/div/div[4]/div/div[2]/div[2]/ul[2]/li/ul/li/span").text
        assert "se agregó al carrito" in self.validate_carrito2;
        print(self.validate_carrito2)

        #NUM OF ITEMS IN THE CART
        self.cart_number2 = self.driver.find_element_by_xpath(".//*[@id='gotocar']/div/a/span[3]").text
        print ("The cart has: " + self.cart_number2 + " items.")

        #OPEN CART MENU AND SELECTING PURCHASE

        self.cart_name2 = self.driver.find_element_by_xpath(".//*[@id='gotocar']/div/a/span[2]").click()
        sleep(2)
        indiv_price2 = self.driver.find_element_by_xpath(".//*[@id='cart-sidebar']/li/div/table[1]/tbody/tr/td/span").text
        print (indiv_price2)
        sleep(2)
        self.cart_pur2 = self.driver.find_element_by_xpath(".//*[@id='btnMinicart']").click()
        self.cart22 = self.driver.find_element_by_css_selector("#car_heb_head").click()
        sleep(20)

        #HOLA CARACOLA
        self.comment = self.driver.find_element_by_xpath(".//*[@id='shopping-cart-table']/tbody/tr/td[6]")
        self.comment.send_keys("Hola Caracola!")

    def screenshot(self):
        #SCREENSHOT
        self.driver.get_screenshot_as_png()
        self.driver.save_screenshot('screenshot.png')

search = heb()
search.search_smarttv()
search.search_mazapan()
search.screenshot()


