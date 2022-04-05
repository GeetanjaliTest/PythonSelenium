from selenium.webdriver.common.by import By


def find_element(driver):
    return driver.find_element(By.CLASS_NAME, SignupPage.sign_in_button)



class SignupPage:

    sign_in_button = "nav__button-secondary"
