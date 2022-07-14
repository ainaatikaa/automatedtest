from selenium.webdriver.common.keys import Keys
import Driver
import time
import random
import string

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def login():
    Driver.driver.get('https://vhsmartqsrtest.azurewebsites.net/') # Go to VH Smart website login
    Driver.driver.fullscreen_window()
    try:
        username_box = Driver.driver.find_element_by_xpath('//*[@id="Input_Email"]')
        password_box = Driver.driver.find_element_by_xpath('//*[@id="Input_Password"]')

        username = "cubacuba@gmail.com"
        password = "p@ssw0rd1234"

        # 1. Login into VH SMART
        username_box.send_keys(username)
        password_box.send_keys(password)
        password_box.send_keys(Keys.ENTER)

        print('TEST PASSED! Able to login to VH Smart')
    except Exception as e:
        print('TEST FAILED! Unable to login to VH Smart. Error', e)

time.sleep(2)
#Manage companies
def TC_JAKIM_ManageCompanies():
        
        try:
            
            Driver.driver.find_element_by_xpath('//*[@id="ManageCompanies"]').click()
            time.sleep(2)
            
            #ADD FIRST DATA OF MANAGE COMPANIES
            #Click add button 
            Driver.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[2]/div/div/div/div[1]/div/button').click()
            time.sleep(2)

            #Company name
            Driver.driver.find_element_by_xpath('//*[@id="CompanyName"]')
            Name_box = Driver.driver.find_element_by_xpath('//*[@id="CompanyName"]')
            Name = ''.join(random.choices(string.digits, k=3))
            Name_box.send_keys("COMPANY DEMO 1 " + Name)

            #Certificate Body
            CertificationBody_list = Driver.driver.find_element_by_xpath('// *[ @ id = "CertificationBodiesId"]')
            dropdownCB = Select(CertificationBody_list)
            dropdownCB.select_by_index('7')  

            #Company Register Type
            CompanyRegistrationType_list = Driver.driver.find_element_by_xpath('// *[ @ id = "RegistrationTypeId"]')
            dropdownCRT = Select(CompanyRegistrationType_list)  # CRT is shortform for Company Registration Type
            dropdownCRT.select_by_index('2')  

            #Business Registration No.
            Driver.driver.find_element_by_xpath('// *[ @ id = "CompanyRegNumber"]')
            BusinessRegistrationNo_box = Driver.driver.find_element_by_xpath('// *[ @ id = "CompanyRegNumber"]')
            BusinessRegNo = "23112021/6"
            BusinessRegistrationNo_box.send_keys(BusinessRegNo)

            #Company Owner Status
            CompanyOwnerStatus_list = Driver.driver.find_element_by_xpath('// *[ @ id = "CompanyOwnerStatusId"]')
            dropdownCOS = Select(CompanyOwnerStatus_list)  # COS is shortform for Company Owner Status
            dropdownCOS.select_by_index('2') 

            time.sleep(3)
            #Brand
            #sel = Select(Driver.driver.find_element_by_xpath('//*[@id="BrandId"]'))
            #sel.select_by_visible_text("KFC")
            #time.sleep(3)

            #ADD SECOND DATA MANAGE COMPANIES
            #Click add button 
            Driver.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[2]/div/div/div/div[1]/div/button').click()
            time.sleep(2)

            #Company name
            Driver.driver.find_element_by_xpath('//*[@id="CompanyName"]')
            Name_box = Driver.driver.find_element_by_xpath('//*[@id="CompanyName"]')
            Name = ''.join(random.choices(string.digits, k=3))
            Name_box.send_keys("COMPANY DEMO 2 " + Name)

            #Certificate Body
            CertificationBody_list = Driver.driver.find_element_by_xpath('// *[ @ id = "CertificationBodiesId"]')
            dropdownCB = Select(CertificationBody_list)
            dropdownCB.select_by_index('10')  

            #Company Register Type
            CompanyRegistrationType_list = Driver.driver.find_element_by_xpath('// *[ @ id = "RegistrationTypeId"]')
            dropdownCRT = Select(CompanyRegistrationType_list)  # CRT is shortform for Company Registration Type
            dropdownCRT.select_by_index('1')  

            #Business Registration No.
            Driver.driver.find_element_by_xpath('// *[ @ id = "CompanyRegNumber"]')
            BusinessRegistrationNo_box = Driver.driver.find_element_by_xpath('// *[ @ id = "CompanyRegNumber"]')
            BusinessRegNo = "280118/6"
            BusinessRegistrationNo_box.send_keys(BusinessRegNo)

            #Company Owner Status
            CompanyOwnerStatus_list = Driver.driver.find_element_by_xpath('// *[ @ id = "CompanyOwnerStatusId"]')
            dropdownCOS = Select(CompanyOwnerStatus_list)  # COS is shortform for Company Owner Status
            dropdownCOS.select_by_index('1') 

            time.sleep(3)
            
            #Click Add Button
            Driver.driver.find_element_by_xpath('//*[@id="btnAdd"]').click()
            time.sleep(5)
            # Click Save button
            Driver.driver.find_element_by_xpath('//*[@id="btnAdd2"]').click()

            print('TEST PASSED! Able to save Add new to manage companies')
        except Exception as e:
            print('TEST FAILED! Unable to save Add new to manage companies', e)
time.sleep(2)
#Manage Users
def TC_JAKIM_ManageUsers():
    try:
        
        Driver.driver.find_element_by_xpath('//*[@id="ManageUser"]').click()
        time.sleep(2)

        #ADD FIRST DATA OF MANAGE USERS
        #Click button Add to add Manage Users
        Driver.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[2]/div/div/div/div[1]/div/button').click()
        time.sleep(2)

        #manage Users Employee Name
        Driver.driver.find_element_by_xpath('//*[@id="EmployeeName"]')
        EmployeeName_box = Driver.driver.find_element_by_xpath('//*[@id="EmployeeName"]')
        EmployeeNm = " Auditor Food Premise "
        EmployeeName_box.send_keys(EmployeeNm)
        time.sleep(2)

        #Manage Users Email
        Driver.driver.find_element_by_xpath('//*[@id="Email"]')
        EmployeeEmail_box = Driver.driver.find_element_by_xpath('//*[@id="Email"]')
        EmployeeE = "  auditorfoodpremise@comp<rand>.com "
        EmployeeEmail_box.send_keys(EmployeeE)
        time.sleep(2)

        #Manage Users Role
        EmployeeRole_list = Driver.driver.find_element_by_xpath('//*[@id="RoleId"]')
        dropdownER = Select(EmployeeRole_list)
        dropdownER.select_by_index('1')
        time.sleep(2)

        #Manage Users Status
        EmployeeStatus_list = Driver.driver.find_element_by_xpath('//*[@id="UserStatusId"]')
        dropdownES = Select(EmployeeStatus_list)
        dropdownES.select_by_index('2')
        time.sleep(2)

        time.sleep(2)

        #ADD SECOND DATA OF MANAGE USERS
        #Click button Add to add Manage Users
        Driver.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[2]/div/div/div/div[1]/div/button').click()
        time.sleep(2)

        #manage Users Employee Name
        Driver.driver.find_element_by_xpath('//*[@id="EmployeeName"]')
        EmployeeName_box = Driver.driver.find_element_by_xpath('//*[@id="EmployeeName"]')
        EmployeeNm = " Auditor Food Product "
        EmployeeName_box.send_keys(EmployeeNm)
        time.sleep(2)

        #Manage Users Email
        Driver.driver.find_element_by_xpath('//*[@id="Email"]')
        EmployeeEmail_box = Driver.driver.find_element_by_xpath('//*[@id="Email"]')
        EmployeeE = "  auditorfoodproduct@comp<rand>.com"
        EmployeeEmail_box.send_keys(EmployeeE)
        time.sleep(2)

        #Manage Users Role
        EmployeeRole_list = Driver.driver.find_element_by_xpath('//*[@id="RoleId"]')
        dropdownER = Select(EmployeeRole_list)
        dropdownER.select_by_index('1')
        time.sleep(2)

        #Manage Users Status
        EmployeeStatus_list = Driver.driver.find_element_by_xpath('//*[@id="UserStatusId"]')
        dropdownES = Select(EmployeeStatus_list)
        dropdownES.select_by_index('2')
        time.sleep(2)

        Driver.driver.find_element_by_xpath('//*[@id="btnAdd"]').click()
        time.sleep(5)


        print('TEST PASSED! Able to add to Manage Users Page')
    except Exception as e:
        print ('TEST FAILED! Unable to add to Manage Users Page')

login()
TC_JAKIM_ManageCompanies()
TC_JAKIM_ManageUsers()