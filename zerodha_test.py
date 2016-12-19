from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

#Login to Zerodha
driver.get("https://kite.zerodha.com")
driver.find_element_by_name('user_id').send_keys('PA5204')
driver.find_element_by_id('inputtwo').send_keys('anshikme@16')
driver.find_element_by_name('login').click()
a= driver.find_element_by_class_name('first').text

if (a == "In Which bank did you first open your account? ( e.g. HDFC ,SBI, etc.)"):
    driver.find_element_by_name('answer1').send_keys('Axis')
elif (a== "What is the brand name of the first watch you owned? (e.g. Titan, Times, etc)"):
    driver.find_element_by_name('answer1').send_keys('Sonata')
elif(a=="Which year did you join your current company? (e.g. 2000, 2005, etc)"):
    driver.find_element_by_name('answer1').send_keys('2014')
elif (a== "Which brand of mobile phone do you use? (e.g. Nokia, LG etc)"):
    driver.find_element_by_name('answer1').send_keys('Mi')
elif(a=="Which year did you complete your graduation? (e.g. 2000, 1990 etc)"):
    driver.find_element_by_name('answer1').send_keys('2013')

b= driver.find_element_by_class_name('second').text

if (b == "In Which bank did you first open your account? ( e.g. HDFC ,SBI, etc.)"):
    driver.find_element_by_name('answer2').send_keys('Axis')
elif (b == "What is the brand name of the first watch you owned? (e.g. Titan, Times, etc)"):
    driver.find_element_by_name('answer2').send_keys('Sonata')
elif(b =="Which year did you join your current company? (e.g. 2000, 2005, etc)"):
    driver.find_element_by_name('answer2').send_keys('2014')
elif (b == "Which brand of mobile phone do you use? (e.g. Nokia, LG etc)"):
    driver.find_element_by_name('answer2').send_keys('Mi')
elif(b =="Which year did you complete your graduation? (e.g. 2000, 1990 etc)"):
    driver.find_element_by_name('answer2').send_keys('2013')

driver.find_element_by_name('twofa').click()
#Login to Zerodha end
driver.find_element_by_link_text('5').click()
driver.find_element_by_class_name('button button-clear sell ng-scope ng-isolate-scope hint--top hint--rounded').click()

print b
