from selenium import webdriver
import time
import smtplib

dik = {
    'title':[],
    'linku':[]
}
browser = webdriver.Chrome()


def top_channel():
    global dik
    browser.get('https://top-channel.tv')
    try:
        for lajmi in browser.find_elements_by_xpath('.//a[@class="story"]'):
            teksti = lajmi.text
            linku = lajmi.get_attribute('href')
            dik['title'].append(teksti)
            dik['linku'].append(linku)
    except:
        dik['title'].append("Nuk mund te marre te dhena nga top-channel")
        dik['linku'].append("None")


def klan():
    global dik
    browser.get('https://tvklan.al/lajme/')
    time.sleep(5)
    try: #main article
        link = browser.find_element_by_xpath('.//div[@class="news-lg w-100 clear text-center"]').find_element_by_xpath(
        './/a').get_attribute('href')
        title = browser.find_element_by_xpath('.//div[@class="news-lg w-100 clear text-center"]').find_element_by_xpath(
        './/h1').text
        dik['title'].append(title)
        dik['linku'].append(link)
    except:
        dik['title'].append("Nuk mund te marre te dhena nga klan main article")
        dik['linku'].append("None")

    try: # right side
        for element in browser.find_elements_by_xpath('.//div[@class="col-lg-12 col-md-6 col-12 news-sm"]'):
            link = element.find_element_by_xpath('.//a').get_attribute('href')
            title = element.find_element_by_xpath('.//h2').text
            dik['title'].append(title)
            dik['linku'].append(link)
    except:
        dik['title'].append("Nuk mund te marre te dhena nga klan side bar article")
        dik['linku'].append("None")

    try: # middle
        for element in browser.find_elements_by_xpath('.//div[@class="col-lg-6 col-md-6 col-12 tile-news"]'):
            title = element.find_element_by_xpath('.//h3').text
            link = element.find_element_by_xpath('.//a').get_attribute('href')
            dik['title'].append(title)
            dik['linku'].append(link)
    except:
        dik['title'].append("Nuk mund te marre te dhena nga klan middle article")
        dik['linku'].append("None")


top_channel()
klan()

message = ''
for i in range(len(dik['title'])):
    message+= dik['title'][i]+ ' ' + dik['linku'][i]
    message+= '\n'

print(message)

gmail_user = 'swagpythonbot@gmail.com'
gmail_password = 'spb@1234'
#message = message.encode('ascii', 'ignore').decode('ascii')
server = smtplib.SMTP('smtp.gmail.com' , 587)
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_password)
server.sendmail(gmail_user, ['erin.manka@akshi.gov.al', 'gerald.cela@gmail.com', 'besian.arizi@akshi.gov.al'], message.encode("utf8"))
server.close()