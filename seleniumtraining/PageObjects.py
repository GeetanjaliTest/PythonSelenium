import self

from Driver import noinit


class FindElements:
    def __init__(self, By, locator):
        self.by=By
        self.locator=locator
    def findElements(self):

        return noinit().find_element(self.by, self.locator)
    #Desktops = driver.find_element_by_link_text("Desktops")
