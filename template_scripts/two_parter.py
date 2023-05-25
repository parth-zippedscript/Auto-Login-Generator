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
        url = 'URL_PLACE_HOLDER'
        driver.get(url=url)
        username_method = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME,'UserName')))
        username_method.send_keys(username)
        continue_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,'continue-login')))
        continue_button.click()
        password_method = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME,'Password')))
        submit_method = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,'login-button')))
        driver = sec.login(driver, password, password_method, submit_method, False)
        PageWorks = True
        try:  # test for login sucessful
            username_method = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME,'UserName')))
            username_method.send_keys(username)
            return { 'login_results': False, 'page_works': PageWorks, 'login_works': LoginWorks, 'exception': 'login_doesnt_work', 'driver': driver }
        except:  # login sucessful
            LoginWorks = True
            TwoFactor = False
            return { 'login_results': True, 'page_works': PageWorks, 'login_works': LoginWorks, 'two_factor': TwoFactor, 'driver': driver }

    except Exception as e:
        return { 'login_results': False, 'page_works': PageWorks, 'login_works': LoginWorks, 'driver': driver, 'exception': str(e), 'traceback': str(traceback.format_tb(e.__traceback__)[0]) }