from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import importlib, traceback, time, os
# spec = importlib.util.spec_from_file_location("secure_login", os.environ["SECURE_LOGIN_FILE"])
# sec = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(sec)
import secure_login as sec


def login(driver, username, password):
    PageWorks = False
    LoginWorks = False
    try:
        url = 'https://usosweb.ue.wroc.pl/kontroler.php?_action=logowaniecas/index'
        driver.get(url=url)
        time.sleep(1)  # auto redirect
        username_method = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, """userNameInput""")))
        username_method.send_keys(username)
        password_method = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, """passwordInput""")))
        submit_method = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, """passwordInput""")))
        driver = sec.login(driver, password, password_method, submit_method, False)
        PageWorks = True
        try:
            alert = driver.switch_to.alert
            alert.accept()
            driver.switch_to.default_content()
        except:
            pass
        try:  # test for login sucessful
            password_method = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, """passwordInput""")))
            password_method.send_keys(password)
            return { 'login_results': False, 'page_works': PageWorks, 'login_works': LoginWorks, 'exception': 'login_doesnt_work', 'driver': driver }
        except:  # login sucessful
            LoginWorks = True
            TwoFactor = False
            return { 'login_results': True, 'page_works': PageWorks, 'login_works': LoginWorks, 'two_factor': TwoFactor, 'driver': driver }
    except Exception as e:
        return { 'login_results': False, 'page_works': PageWorks, 'login_works': LoginWorks, 'driver': driver, 'exception': str(e), 'traceback': str(traceback.format_tb(e.__traceback__)[0]) }
