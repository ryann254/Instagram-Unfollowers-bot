from selenium import webdriver
from time import sleep
import secrets

class Instabot:
    def __init__(self, username, pw):
        self.username = username
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)
        # self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]')\
        #     .click()
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        # self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]")\
        #     .click()
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
            .click()
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
            .click()
        sleep(2)

    def get_my_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username))\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}/following')]".format(self.username))\
            .click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}/followers')]".format(self.username))\
            .click()
        followers = self._get_names()

        not_following_back = [username for username in following if username not in followers]
        print(not_following_back)

    def _get_names(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        # self.driver.execute_script('arguments[0].scrollIntoView()', scroll_box)
        # sleep(1)

        last_height, height = 0, 1
        while last_height != height:
            last_height = height
            sleep(1)
            height = self.driver.execute_script("""
                    arguments[0].scrollTo(0, arguments[0].scrollHeight);
                    return arguments[0].scrollHeight
                    """, scroll_box)

        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        #close the followers/following box
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")\
            .click()
        return names


username = 'papa_drac_rn'
ryan_bot = Instabot(username, secrets.pw)
#You can also use python -i(interactive) main.py
ryan_bot.get_my_unfollowers()