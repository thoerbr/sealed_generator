
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import chromedriver_binary
import tkinter as tk
import time




def create_sealed_pool(boosters):
    '''
    Function to generate sealed pool based on boosters from mtgadraft.tk

    Parameters
    ----------
    boosters : list
        List containing boosters of sealed pool.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    
    driver = webdriver.Chrome()# Open the website
    driver.get('https://mtgadraft.tk/')
    
    
    timeout = 10
    
    # click on sealed deck generator
    try:
        xpath = '/html/body/div[2]/div[2]/div/span[4]/span/div[2]/div/div[2]/button[1]'
        element_present = EC.presence_of_element_located((By.XPATH, xpath))
        WebDriverWait(driver, timeout).until(element_present)
        
        d = driver.find_element_by_xpath(xpath)
        driver.execute_script("arguments[0].click();", d)
    except TimeoutException:
        print("Timed out waiting for page to load")
    
    # select sealed pool composition
    i = 1
    for b in boosters:
        try:
            xpath = '/html/body/div[3]/div/div[2]/div[1]/div/select[' + str(i) + ']'
            element_present = EC.presence_of_element_located((By.XPATH, xpath))
            WebDriverWait(driver, timeout).until(element_present)
        
            select = Select(driver.find_element_by_xpath(xpath))
            select.select_by_visible_text(b)
            i = i+1
            
        except TimeoutException:
            print("Timed out waiting for page to load")
        
            # xpath = '/html/body/div[3]/div/div[2]/div[1]/div/select[' + str(i) + ']'
        # select = Select(driver.find_element_by_xpath(xpath))
        # select.select_by_visible_text(b)
    
    
    # generate sealed pool
    pool = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/button[1]')
    driver.execute_script("arguments[0].click();", pool)
    
    # copy sealed pool to clipboard
    try:
        xpath = '/html/body/div[2]/div[4]/div/div/div[1]/div/div[1]/button[1]'
        element_present = EC.presence_of_element_located((By.XPATH, xpath))
        WebDriverWait(driver, timeout).until(element_present)
        
        d = driver.find_element_by_xpath(xpath)
        d.click()
    except TimeoutException:
        print("Timed out waiting for page to load")
    
    # print sealed pool
    root = tk.Tk()
    return root.clipboard_get()



#============================================================================================================
#============================================================================================================
    

# sealed pool composition
players = ["Max Mustermann", "Erika Musterfrau", "Gandalf Control", "Monor Inurface"]

boosters = ["Strixhaven: School of Mages", 
            "Kaldheim",
            "Core Set 2021",
            "Ikoria: Lair of Behemoths",
            "Throne of Eldraine",
            "Dominaria"]


for p in players:
    sp = create_sealed_pool(boosters)
    file = open('sealed_pools.txt', 'a')
    file.write(p)
    file.write('\n')
    file.writelines(sp)
    file.write('\n')
    file.write('=============================================\n')
    file.write('=============================================\n')
    file.close()
    time.sleep(15)
    
