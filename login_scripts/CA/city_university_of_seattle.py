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
    # Microsoft Login
    try:
        url = 'https://login.microsoftonline.com/b3fa96d9-f515-4662-add7-63d854e39e63/saml2?SAMLRequest=jZLNbtswEITvfgpBd0kWJdIWYRtw4%2F4YcG0jdnvoJaDJVUJAIlUu2dZvX0lpm%2BSQoARPw50POwMuULRNx9fBP5hb%2BB4A%2FSSKfrWNQT4%2BLePgDLcCNXIjWkDuJT%2BtP%2B84Sae8c9ZbaZv4heltj0AE57U1g2m7WcaH%2Ffvd4eN2fzcnis3roiSEMprnM8gZBQlyVl6mlJG6IrOiLKgcjF%2FBYc9Yxj1yBCEG2Br0wvhenJIimZL%2BnnPGKeWk%2BjZMbfp82gg%2FOh%2B875BnWWPvtUlbLZ1FW3trGm0glbbNLkUtKqaqpKY5TUrGSCKUmiWsUHNaQlEBK7IhMRngxz9lvNNGaXP%2FdguXxyHkn87nY3I8nM4DYv23mxtrMLTgTuB%2BaAlfbndP%2B7bXVGp%2FDSmokIlOZ9I6GNe4Q7RZvOpBUbQYBD7W4lb%2FaV1kz01PmI7v%2BwDbzdE2Wl5HfTgfrGuFfz1nnuajolVSj6M8GOxA6lqDiv9h1k1jf944EB6WsXcB4ihbTSaPy7z8m6vf&RelayState=https%3A%2F%2Fmy.cityu.edu%2Fapi%2Fcore%2Fsaml_sso'
        driver.get(url=url)
        time.sleep(1)  # auto redirect
        username_method = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='i0116']")))
        username_method.send_keys(username)
        submit_method = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, """//*[@id="i0116"]"""))).send_keys(Keys.ENTER)
        time.sleep(1)  # need to wait because the page redirects from microsoft to school site
        PageWorks = True
        try:
            if "Work or school account" in driver.page_source:
                school_option = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="aadTile"]/div/div[2]')))
                school_option.click()
        except:
            pass
        try:
            username_method = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
            username_method.send_keys(username)
            return {'login_results': False, 'page_works': PageWorks, 'login_works': LoginWorks,
                    'exception': 'login_doesnt_work', 'driver': driver}
        except:
            try:
                password_method = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, """i0118""")))
                submit_method = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, """i0118""")))
                driver = sec.login(driver, password, password_method, submit_method, False)
                if 'Sign-in is blocked' in driver.page_source or 'Connexion bloqu' in driver.page_source:
                    return {'login_results': False, 'page_works': PageWorks, 'login_works': LoginWorks,
                            'exception': 'login_doesnt_work', 'driver': driver}
            except:
                password_method = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.ID, """passwordInput""")))
                submit_method = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.ID, """passwordInput""")))
                driver = sec.login(driver, password, password_method, submit_method, False)
                if 'Sign-in is blocked' in driver.page_source or 'Connexion bloqu' in driver.page_source:
                    return {'login_results': False, 'page_works': PageWorks, 'login_works': LoginWorks,
                            'exception': 'login_doesnt_work', 'driver': driver}
            try:
                try:
                    password_method = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.ID, """i0118""")))
                    password_method.send_keys(password)
                    return {'login_results': False, 'page_works': PageWorks, 'login_works': LoginWorks,
                            'exception': 'login_doesnt_work', 'driver': driver}
                except:
                    password_method = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.ID, """userNameInput""")))
                    password_method.send_keys(password)
                    return {'login_results': False, 'page_works': PageWorks, 'login_works': LoginWorks,
                            'exception': 'login_doesnt_work', 'driver': driver}
            except:  # login sucessful
                try:
                    two_factor_authenticator_app = False
                    LoginWorks = True
                    TwoFactor = True
                    two_factor_dict = []
                    try:
                        # Security Email
                        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, """iProofEmail""")))
                        two_factor_dict.append({
                                                   'choice': f'{WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, """iProofLbl0"""))).text}'})
                        return {'login_results': True, 'page_works': PageWorks, 'login_works': LoginWorks,
                                'two_factor': TwoFactor, 'two_factor_choices': two_factor_dict,
                                'two_factor_authenticator_app': two_factor_authenticator_app, 'driver': driver}
                    except:
                        pass

                    try:
                        # Approve sign in request
                        WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.ID, """idDiv_SAOTCAS_Title""")))
                        two_factor_authenticator_app = True
                        two_factor_dict.append({
                                                   'choice': f'{WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, """idDiv_SAOTCAS_Description"""))).text}'})
                        return {'login_results': True, 'page_works': PageWorks, 'login_works': LoginWorks,
                                'two_factor': TwoFactor, 'two_factor_choices': two_factor_dict,
                                'two_factor_authenticator_app': two_factor_authenticator_app, 'driver': driver}
                    except Exception as e:
                        pass

                    # Approve a request on my Microsoft Authenticator app
                    try:
                        choice = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                            (By.CSS_SELECTOR, """[data-value="PhoneAppNotification"]""")))
                        two_factor_dict.append({'choice': f"{choice.text}"})
                        two_factor_authenticator_app = True
                    except:
                        pass
                    # Use a verification code
                    try:
                        choice = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, """[data-value="PhoneAppOTP"]""")))
                        two_factor_dict.append({'choice': f"{choice.text}"})
                    except:
                        pass
                    # Text +X XXXXXXXXXX
                    try:
                        choice = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, """[data-value="OneWaySMS"]""")))
                        two_factor_dict.append({'choice': f"{choice.text}"})
                    except:
                        pass
                    # Call +X XXXXXXXXXX
                    try:
                        choice = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, """[data-value="TwoWayVoiceMobile"]""")))
                        two_factor_dict.append({'choice': f"{choice.text}"})
                    except:
                        pass

                    if len(two_factor_dict) >= 1:
                        return {'login_results': True, 'page_works': PageWorks, 'login_works': LoginWorks,
                                'two_factor': TwoFactor, 'two_factor_choices': two_factor_dict,
                                'two_factor_authenticator_app': two_factor_authenticator_app, 'driver': driver}
                    else:
                        raise ValueError('2fa_not_found')
                except:
                    LoginWorks = True
                    TwoFactor = False
                    return {'login_results': True, 'page_works': PageWorks, 'login_works': LoginWorks,
                            'two_factor': TwoFactor, 'driver': driver}
    except Exception as e:
        return {'login_results': False, 'page_works': PageWorks, 'login_works': LoginWorks, 'driver': driver,
                'exception': str(e), 'traceback': str(traceback.format_tb(e.__traceback__)[0])}

