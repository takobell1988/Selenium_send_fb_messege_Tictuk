from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


def facebook_login():
    ### CHROME DRIVER WINDOWS LOCATION ###
    Chrome_driver = webdriver.Chrome(executable_path='C:\Temp\chromedriver.exe')
    ### OPEN TICTUK DEMO URL ###
    Chrome_driver.get('https://www.facebook.com/tictukDemo/')
    ### ENTER FACEBOOK CREDENTIALS ###
    Chrome_driver.find_element_by_id("email").send_keys('ofirtako@gmail.com')
    Chrome_driver.find_element_by_id("pass").send_keys('bananasplit1987')
    Chrome_driver.find_element_by_id("u_0_3").click()
    sleep(20)
    ### CLICK ON SEND MESSEGE ##
    Chrome_driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/div/div[2]/div/div[2]/div/div/button').click()
    sleep(3)
    ### SEND HELLO MESSEGE ###
    Chrome_driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[1]/div/div/div[4]/div/div[1]/div/div/div/div/div/div/div/div[2]/div[4]/div/div/div/span/div/div/div[2]/div/div/div/div').send_keys('hello'+Keys.ENTER)
    sleep(10)
    ### BOT RESPONSE ###
    response = Chrome_driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[1]/div/div/div[4]/div/div[1]/div/div/div/div/div/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div').text
    print(response)
    sleep(10)
    ### CLOSE CHROME ###
    Chrome_driver.close()

facebook_login()
