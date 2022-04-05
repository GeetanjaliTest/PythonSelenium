from PageObjects import FindElements

class laptopandnotebook():

                    LaptopandNotebooks = FindElements(By="css selector",locator="div.container:nth-child(3) nav.navbar div.collapse.navbar-collapse.navbar-ex1-collapse ul.nav.navbar-nav li.dropdown:nth-child(2) > a.dropdown-toggle")

                    MAC2 = FindElements(By="xpath",locator="//a[contains(text(),'Macs (0)')]")
                    windows = FindElements(By="css selector",locator="div.container:nth-child(3) nav.navbar div.collapse.navbar-collapse.navbar-ex1-collapse ul.nav.navbar-nav li.dropdown:nth-child(2) div.dropdown-menu div.dropdown-inner ul.list-unstyled li:nth-child(2) > a:nth-child(1)")