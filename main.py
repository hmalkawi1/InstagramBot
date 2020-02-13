from selenium import webdriver
import time

class InstaBot:

    #initial function: logs in using given username + password, then bypasses notifications
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://www.instagram.com/accounts/login/")
        
        time.sleep(2)

        #will find the input field called : Username 
        self.driver.find_element_by_xpath("//input[@name= \"username\"]")\
            .send_keys(username)

        #will find the input field called : password 
        self.driver.find_element_by_xpath("//input[@name= \"password\"]")\
            .send_keys(password)
        
        #will find log in button
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        #sleep so it will have time to log in before doing anything
        time.sleep(5)

        #will by pass "Turn on notifcaions" and click "not now"
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        
        time.sleep(2)

        
    #main function that will return list of people who do not follow you back
    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        
        time.sleep(3)

        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()

        following = self._get_names()

        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()

        followers = self._get_names()

        not_following_back = [user for user in following if user not in followers]
        print("\nAccounts that do not follow back:\n")
        print(not_following_back)
       

    #function that will be re-used to open following/followers box and return names of users
    def _get_names(self):
        time.sleep(2)

        #using these 2 variables, we will continously compare height after each scroll
        #while loop will exit when we have no more followers to load
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(1)

            scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")

            #continously update height with new value
            #argument[0] can be understood as "scroll_box"
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
            

        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text!= '']
        
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()

        return names








my_bot = InstaBot('INSERT USERNAME HERE', 'INSERT PASSWORD HERE')
my_bot.get_unfollowers()

'''
Extra IF NEEDED:
CODE TO SCROLL TO BOTTOM OF A PAGE:

SCROLL_PAUSE_TIME = 0.5
last_height = self.driver.execute_script("return document.body.scrollHeight")

while True:
    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = self.driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
'''



        
