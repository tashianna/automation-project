import time
import os
from turtle import delay
from click import confirm
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

load_dotenv()

EXTENSION_PATH = os.getcwd() + '\\metamask.crx'

EXTENSION_ID = 'chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome'

WEB_SESSION = os.getcwd() + '\\web-session'

driverPath = os.getcwd() + '\\chromedriver.exe'

accountName_metamask = os.getenv('METAMASK_ACC')

password_metamask = os.getenv('METAMASK_PASS')

accountName_myalgo = os.getenv('MYALGO_ACC')

password_myalgo = os.getenv('MYALGO_PASS')

recoveryPhrase_myalgo = os.getenv('MYALGO_MNEMONIC')

m = os.getenv('METAMASK_MNEMONIC').split()

delay = 3

chrome_options = Options()
chrome_options.add_extension(EXTENSION_PATH)
driver = webdriver.Chrome(options=chrome_options, executable_path=driverPath)
driver.maximize_window()

def MetamaskSetup():
    print("Metamask Setup")
    driver.implicitly_wait(3)
    driver.get(EXTENSION_ID)
    driver.find_element(By.XPATH,"//div[@id='app-content']/div/div[2]/div/div/div/button").click()

    #import wallet
    driver.switch_to.window(driver.window_handles[-1])
    driver.find_element(By.XPATH,"//div[@id='app-content']/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button").click()
    driver.find_element(By.XPATH,"//div[@id='app-content']/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]").click()

    #bypass to recovery phase
    driver.find_element(By.ID,'import-srp__srp-word-0').send_keys(m[0])
    driver.find_element(By.ID,'import-srp__srp-word-1').send_keys(m[1])
    driver.find_element(By.ID,'import-srp__srp-word-2').send_keys(m[2])
    driver.find_element(By.ID,'import-srp__srp-word-3').send_keys(m[3])
    driver.find_element(By.ID,'import-srp__srp-word-4').send_keys(m[4])
    driver.find_element(By.ID,'import-srp__srp-word-5').send_keys(m[5])
    driver.find_element(By.ID,'import-srp__srp-word-6').send_keys(m[6])
    driver.find_element(By.ID,'import-srp__srp-word-7').send_keys(m[7])
    driver.find_element(By.ID,'import-srp__srp-word-8').send_keys(m[8])
    driver.find_element(By.ID,'import-srp__srp-word-9').send_keys(m[9])
    driver.find_element(By.ID,'import-srp__srp-word-10').send_keys(m[10])
    driver.find_element(By.ID,'import-srp__srp-word-11').send_keys(m[11])

    #enter password
    driver.find_element(By.ID,'password').send_keys(password_metamask)
    driver.find_element(By.ID,'confirm-password').send_keys(password_metamask)
    driver.find_element(By.ID,'create-new-vault__terms-checkbox').click()
    driver.find_element(By.XPATH,"//div[@id='app-content']/div/div[2]/div/div/div[2]/form/button").click()
    driver.find_element(By.XPATH,"//div[@id='app-content']/div/div[2]/div/div/button").click()
    driver.find_element(By.XPATH,"//div[@id='popover-content']/div/div/section/div[1]/div/button").click()
    print("Done Import Account")

    #switch network to TestNet
    driver.find_element(By.CLASS_NAME,'network-display__icon').click()
    driver.find_element(By.CLASS_NAME,'network-dropdown-content--link').click()
    driver.find_element(By.XPATH,"//div[@id='app-content']/div/div[3]/div/div[2]/div[2]/div[2]/div[7]/div[2]/div/label/div[1]/div[1]/div[2]").click()
    driver.find_element(By.CLASS_NAME,'network-display__icon').click()
    driver.find_element(By.XPATH,"//div[@id='app-content']/div/div[2]/div/div[2]/li[4]/span").click()
    print("Rinkeby TestNet selected")

MetamaskSetup()


def WalletChainSetup():
    #open messina website 
    driver.implicitly_wait(3)
    driver.execute_script("window.open('https://bridge.messina.devucc.name/bridge');")
    driver.switch_to.window(driver.window_handles[2])

    #connnect myalgo source wallet to messina
    driver.implicitly_wait(3)
    driver.switch_to.window(driver.window_handles[2])
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div[2]/form/div[1]/div[1]/div/button/span[2]/img').click()
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div[2]/form/div[1]/div[1]/div/div/div/div[2]/span').click()
    driver.find_element(By.XPATH,'//*[@id="input-source-chain"]/div[2]/button').click()
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div[2]/dialog[1]/div/div[2]/ul/li[2]/span').click()

    #setup wallet
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[3])
    driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[2]/div/div[2]/a').click()

    #agree to terms and agreement
    driver.implicitly_wait(3)
    driver.switch_to.window(driver.window_handles[4])
    driver.find_element(By.XPATH, '//html/body/div/div[2]/div/div[1]/div/div/div/div/div[4]/label/input').click()
    driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[1]/div/div/div/div/div[5]/button').click()
    #insert password
    driver.find_element(By.XPATH,"//div[@id='root']/div[2]/div/div[1]/div/div/div/div[2]/form/div/div[1]/div[2]/div/input").send_keys(password_myalgo)
    driver.find_element(By.XPATH,"//div[@id='root']/div[2]/div/div[1]/div/div/div/div[2]/form/div/div[3]/div/input").send_keys(password_myalgo)
    driver.find_element(By.XPATH,"//div[@id='root']/div[2]/div/div[1]/div/div/div/div[2]/form/button/div/div").click()
    #select testnet
    driver.find_element(By.CLASS_NAME,"_9w6ztc").click()
    driver.find_element(By.CLASS_NAME,"_1s54rqk").click()
    #import account
    driver.find_element(By.XPATH,"//div[@id='root']/div[2]/div[3]/div[1]/div[2]/div[1]/div[3]/div/div[2]/div[1]").click()
    #insert mnemonic words
    driver.find_element(By.XPATH,"//div[@id='root']/div[2]/div[3]/div[1]/div[2]/div[1]/div/input").send_keys(accountName_myalgo)
    driver.find_element(By.NAME,'input-24').send_keys(recoveryPhrase_myalgo)
    driver.find_element(By.CLASS_NAME,"_u02imw").click()
    #reenter password
    driver.implicitly_wait(3)
    driver.find_element(By.CLASS_NAME,"_11oc14n.form-control").send_keys(password_myalgo)
    driver.find_element(By.CLASS_NAME,"_16vtsuu").click()

    #connect myalgo to messina
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[3])
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[1]/div[1]/input').send_keys(password_myalgo)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[2]/button[2]').click()
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div').click()
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/div[1]/div[3]/div/div/button[2]').click()

    #connect ethereum destination wallet to messina
    driver.implicitly_wait(3)
    driver.switch_to.window(driver.window_handles[2])
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div[2]/form/div[3]/div[2]/button[1]').click()
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div[2]/dialog[3]/div/div[2]/ul/li[1]/span').click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[4])
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[3]/div[2]/button[2]').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
    driver.switch_to.window(driver.window_handles[2])
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div[2]/dialog[3]/div/button/img').click()  
    
WalletChainSetup()

def sendAlgo() :
    #sendAlgoTest
    try :
        input_amount = WebDriverWait(driver,delay).until(EC.presence_of_element_located(By.XPATH,'/html/body/div/div/div[2]/div[2]/div[2]/form/div[5]/div[1]/div[2]/div/div[1]/input[1]'))
        input_amount.send_keys('5')
        confirm_tx = WebDriverWait(driver,delay).until(EC.presence_of_element_located(By.XPATH,'/html/body/div/div/div[2]/div[2]/div[2]/form/div[8]/button'))
        confirm_tx.click()
    except TimeoutException :
        print ("cannot fill amount")  
        
sendAlgo()



    
