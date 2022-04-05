from selenium import webdriver
driver = None

def driverInstance():
    global driver
    driver = webdriver.Chrome(executable_path="C:/ChromeDriver/chromedriver.exe")
    driver.maximize_window()
    driver.get("http://www.tutorialsninja.com/demo/")
    driver.implicitly_wait(2)
def noinit():
    global driver
    if driver == None:
        return driverInstance()
    else:
        return driver
