from Components import components

from DesktopPage import desktop
from Driver import driverInstance
from LaptopandNotebooksPage import laptopandnotebook


class Test:

        def test(self):
                driver=driverInstance()
                tDesktop = desktop()
                tDesktop.Desktops.findElements().click()
                tDesktop.MAC1.findElements().click()
                tLaptop = laptopandnotebook()
                tLaptop.LaptopandNotebooks.findElements().click()
                tLaptop.MAC2.findElements().click()
                tLaptop.LaptopandNotebooks.findElements().click()
                tLaptop.windows.findElements().click()
                tcomponents= components()
                tcomponents.component.findElements().click()
                tcomponents.miceandtrackballs.findElements().click()
                tcomponents.component.findElements().click()
                tcomponents.monitors.findElements().click()
                tcomponents.component.findElements().click()
                tcomponents.printers.findElements().click()
                tcomponents.component.findElements().click()
                tcomponents.scanners.findElements().click()

#dropdown actionchains
#def test_abc():
    # driver = webdriver.Chrome(executable_path="C:/ChromeDriver/chromedriver.exe")
    #driver.maximize_window()
    #driver.get("http://www.tutorialsninja.com/demo/")
    #driver.implicitly_wait(2)
    #testdesktop(driver)
    #sleep(2)
    #testlaptopandnotebook(driver)
    #sleep(2)
    #signIn = driver.find_element_by_xpath("//a[contains(text(),'Sign in')]")
    #signIn.click()
    #driver.save_screenshot('screenshots' +str(random.randInt(0,101)) +'.png')
    #signup_element = find_element(driver)
    #for i in range(0,5):
     #   signIn.click()
    #action.ActionChains(driver)
    #action.move_to_element(signIn).perform()


