
from random import random
from time import sleep

from PageObjects import FindElements


class desktop():
    Desktops = FindElements(By="css selector",locator="div.container:nth-child(3) nav.navbar div.collapse.navbar-collapse.navbar-ex1-collapse ul.nav.navbar-nav li.dropdown:nth-child(1) > a.dropdown-toggle")
   # Desktops.click()
    MAC1 = FindElements(By="css selector",locator="div.container:nth-child(3) nav.navbar div.collapse.navbar-collapse.navbar-ex1-collapse ul.nav.navbar-nav li.dropdown:nth-child(1) div.dropdown-menu div.dropdown-inner ul.list-unstyled li:nth-child(2) > a:nth-child(1)")
   # MAC1 = driver.find_element_by_link_text("Mac (1)")
   # MAC1.click()
    sleep(3)
