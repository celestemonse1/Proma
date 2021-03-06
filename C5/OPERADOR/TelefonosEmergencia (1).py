# from cProfile import label
# from tkinter import messagebox

# from nose.tools import assert_true
from pip._vendor.distlib.compat import raw_input
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import unittest, time, re, codecs, os
from datetime import datetime
from io import open
from selenium.common.exceptions import TimeoutException

def archivo_log_tiempos(text):
    now = datetime.now()
    tiempo = now.strftime("%H:%M:%S")
    log = open("../../../../Downloads/log.txt", "a", encoding="utf-8")
    log.write("\n" + tiempo + " - " + text)
    log.close()
    print(tiempo + "-" + text)
    return True


class UntitledTestCase(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome("C:\dchrome\chromedriver.exe")
        self.driver.set_window_size(1400, 1000)
        self.driver.implicitly_wait(30)
        # self.base_url = "http://promad.opensystems.mx:8081/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_cerrar_evento(self):
        driver = self.driver
        driver.get("http://52.9.236.138:9596")
        wait = WebDriverWait(driver, 15)
        # Almacena el ID de la ventana original
        win_ser_local = driver.current_window_handle
        # Comprueba que no existen otras ventanas abiertas previamente
        assert len(driver.window_handles) == 1
        time.sleep(1)

        # USUARIO
        usuario = driver.find_element_by_id("mat-input-0")
        usuario.send_keys("CFLORES")
        usuario.send_keys(Keys.ENTER)
        time.sleep(1)

        # CENTRO
        centro = driver.find_element_by_id("mat-input-1")
        centro.send_keys("C5")
        centro.send_keys(Keys.ENTER)
        time.sleep(1)

        # PASSWORD
        clave = driver.find_element_by_id("mat-input-2")
        clave.send_keys("12345")
        clave.send_keys(Keys.ENTER)
        time.sleep(1)

        # LOGIN
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='btnmenu']//span"))).click()
            archivo_log_tiempos("Cargo Login")
        except (RuntimeError, TypeError, NameError):
            archivo_log_tiempos("No cargo Login")


        # OPERADOR
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//span[@class='envolventeCircular']//span"))).click()
            archivo_log_tiempos("Cargo Operador")
        except (RuntimeError, TypeError, NameError):
            archivo_log_tiempos("No cargo Operador")
        time.sleep(30)

        # TELEFONOS DE EMERGENCIA
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//span[@class='mat-button-wrapper']//img)[2]"))).click()
            archivo_log_tiempos("Cargo Telefonos de Emergencia")
        except (RuntimeError, TypeError, NameError):
            archivo_log_tiempos("No cargo Telefonos de Emergencia")

        for win_ser_1 in driver.window_handles:
            if win_ser_1 != win_ser_local:
                driver.switch_to.window(win_ser_1)
                break
        busqueda =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Buscar']")))
        busqueda.send_keys("71")
        time.sleep(15)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class,'mat-flat-button mat-primary')]"))).click()


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def createEvent(self):
        driver.find_element_by_id("mat-checkbox-1").click()
        driver.find_element_by_xpath("//button[@id='0']/span").click()

        wait.until(EC.number_of_windows_to_be(2))
        # Recorrelas hasta encontrar el controlador de la nueva ventana
        for win_ser_1 in driver.window_handles:
            if win_ser_1 != win_ser_local:
                driver.switch_to.window(win_ser_1)
                break
        driver.close()

        cont = 100
        i = 1
        # Cambia el controlador a la ventana o pestana original
        driver.switch_to.window(win_ser_local)
        time.sleep(3)
        # EVENTO

        numero = int(raw_input("\nIngresa la unidad: "))
        # numero = messagebox.Dialog(int(raw_input("\nIngresa el numero de EVENTOS a cerrar: ")))

        # numero = label(miFrame, text="eventos")


if __name__ == "__main__":
    unittest.main()
