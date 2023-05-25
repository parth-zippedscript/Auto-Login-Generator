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
        time.sleep(1)  # auto redirect
        old_src = driver.page_source
        driver = sec.login(driver,password, pop_up=True,user_name=username,url=url)
        PageWorks = True
        if old_src == driver.page_source: # test for login sucessful
            return { 'login_results': False, 'page_works': PageWorks, 'login_works': LoginWorks, 'exception': 'login_doesnt_work', 'driver': driver }
        else: # login sucessful
            LoginWorks = True
            TwoFactor = False
            return { 'login_results': True, 'page_works': PageWorks, 'login_works': LoginWorks, 'two_factor': TwoFactor, 'driver': driver }
    except Exception as e:
        return { 'login_results': False, 'page_works': PageWorks, 'login_works': LoginWorks, 'driver': driver, 'exception': str(e), 'traceback': str(traceback.format_tb(e.__traceback__)[0]) }