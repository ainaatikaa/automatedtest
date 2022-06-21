from cProfile import Profile
import Driver
import Login
import time
import NavigateMenu
import Profiles

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#author aina
#modified date 11 April 2022

# function for login
def login():
    Driver.driver.get("https://vhsmartqsrtest.azurewebsites.net/")
    try:
        username_box = Driver.driver.find_element_by_xpath('//*[@id="Input_Email"]')
        password_box = Driver.driver.find_element_by_xpath('//*[@id="Input_Password"]')
        username = "admin@qsrbrands.com.my"
        password = "p@ssw0rd1234"
        # Login into VHSmart
        username_box.send_keys(username)
        password_box.send_keys(password)
        password_box.send_keys(Keys.ENTER)
        print('TEST PASSED')

    except Exception as e:
        print('TEST FAILED.Unable to Login', e)

# TC Profules 1 --> Open Page
def TC_Profiles1():
    
    try:
        # 1. Go to (Company Information -> Profiles)
        Driver.driver.find_element_by_xpath('//*[@id="CompModule1"]').click()
        time.sleep(2)
        Driver.driver.find_element_by_xpath('//*[@id="Profile"]').click()
        time.sleep(2)
        print("Able to go to Profiles page")
    except Exception as e:
        print("FAILED. ", e)

# TC Profiles 2 --> Add Company to profile
def TC_Profiles2():
    print("\nTesting Profiles 1. Add Company ")
    # 1. Go to (Company information -> Profiles)
    
    try:
        time.sleep(3)
        # 2. Click Button [Add]
        Driver.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[2]/div/div/div/div[1]/div/button').click()
        # 3. Fill in all mandatory fields
        # company name: unique
        time.sleep(2)
        CompanyName_List = Driver.driver.find_element_by_xpath('//*[@id="CompanyName"]')
        dropdownCN = Select(CompanyName_List)
        dropdownCN.select_by_index('1')
        time.sleep(2)
        
        #Company Address
        Driver.driver.find_element_by_xpath('//*[@id="CompanyAddLine1"]')
        CompanyAddress_box = Driver.driver.find_element_by_xpath('//*[@id="CompanyAddLine1"]')
        CompanyAdd = " Jalan Semangka "
        CompanyAddress_box.send_keys(CompanyAdd)
        time.sleep(2)

        #Company Address line 2
        Driver.driver.find_element_by_xpath('//*[@id="CompanyAddLine2"]')
        CompanyAddress2_box = Driver.driver.find_element_by_xpath('//*[@id="CompanyAddLine2"]')
        CompanyAdd2 = " Denai Alam "
        CompanyAddress2_box.send_keys(CompanyAdd2)
        time.sleep(2)

        # Postcode 
        Driver.driver.find_element_by_xpath('//*[@id="Postcode"]')
        PostcodeAddress_box = Driver.driver.find_element_by_xpath('//*[@id="Postcode"]')
        PostcodeAdd = " 40450"
        PostcodeAddress_box.send_keys(PostcodeAdd)
        time.sleep(2)

        #City 
        Driver.driver.find_element_by_xpath('//*[@id="City"]')
        CityAddress_box = Driver.driver.find_element_by_xpath('//*[@id="City"]')
        CityAdd = " Shah Alam "
        CityAddress_box.send_keys(CityAdd)
        time.sleep(2)

        #District
        Driver.driver.find_element_by_xpath('//*[@id="District"]')
        DistrictAddress_box = Driver.driver.find_element_by_xpath('//*[@id="District"]')
        DistrictAdd = " Klang "
        DistrictAddress_box.send_keys(DistrictAdd)
        time.sleep(2)

        # Country
        Country_list = Driver.driver.find_element_by_xpath('//*[@id="for-country"]')
        dropdownCY = Select(Country_list)
        dropdownCY.select_by_value('20')
        time.sleep(2)

        # State
        State_list = Driver.driver.find_element_by_xpath('//*[@id="for-state"]')
        dropdownST = Select(State_list)
        dropdownST.select_by_value('25')
        time.sleep(2)

        # Telephone No
        Driver.driver.find_element_by_xpath('//*[@id="PhoneNumber"]')
        ProfilesTelephoneNo_box = Driver.driver.find_element_by_xpath('//*[@id="PhoneNumber"]')
        ProfilesTelNo = " 0132443231 "
        ProfilesTelephoneNo_box.send_keys(ProfilesTelNo)
        time.sleep(2)

        # Fax No
        Driver.driver.find_element_by_xpath('//*[@id="FaksNumber"]')
        ProfilesFaxNumber_box = Driver.driver.find_element_by_xpath('//*[@id="FaksNumber"]')
        ProfilesFaxNo = " 72995 "
        ProfilesFaxNumber_box.send_keys(ProfilesFaxNo)
        time.sleep(2)

        # scheme
        Scheme_list = Driver.driver.find_element_by_xpath('//*[@id="for-BussType"]')
        dropdownSC = Select(Scheme_list)
        dropdownSC.select_by_index('7')
        time.sleep(2)

        # Industry Size
        IndustrySize_list = Driver.driver.find_element_by_xpath('//*[@id="for-IndustryType"]')
        dropdownIS = Select(IndustrySize_list)
        dropdownIS.select_by_index('2')
        time.sleep(2)

        # Website URL
        Driver.driver.find_element_by_xpath('//*[@id="Website"]')
        WebsiteURL_box = Driver.driver.find_element_by_xpath('//*[@id="Website"]')
        WebURL = " shopee.my "
        WebsiteURL_box.send_keys(WebURL)
        time.sleep(2)
        
        Driver.driver.maximize_window()

        # Company email
        Driver.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[3]/div/div/div[2]/div/div/div[8]/div[2]/input').click()
        CompanyEmail_box = Driver.driver.find_element_by_xpath('//*[@id="CompanyEmail"]')
        CompanyEmail_box.send_keys("Suhaili90@gmail.com")
        time.sleep(2)

        # Click Save button
        Driver.driver.find_element_by_xpath('//*[@id="btnAddCompanyProfile"]').click()

        print("TEST PASSED. Able to add company ")
    except Exception as e:
        print("TEST FAILED. Unable to add company ", e)

        # TC Profiles 3 --> View Company
def TC_Profiles3():
    print("\nTesting Profiles 3. View Company Details ")
    
    try:
        # 2. Click Button [View]
        Driver.driver.find_element_by_xpath('//*[@id="CompanyDataTable"]/tbody/tr[1]/td[1]/a[1]/i').click()
        
        time.sleep(2)
    
        print("TEST PASSED. Able to view company details ")
    except Exception as e:
        print("TEST FAILED. Unable to view company details ", e)

        #TC Profiles 4 --> Edit Company
def TC_Profiles4():
    print("\nTesting Profiles 4. Edit Company Details ")

    try: 
        time.sleep(2)
        # 1.Select any data
        # 2. Click Button [Edit]
        Driver.driver.find_element_by_xpath('//*[@id="CompanyDataTable"]/tbody/tr[1]/td[1]/a[2]').click()
        
        # Edit any fields 
        time.sleep(2)
        
        # Edit Company Address
        Driver.driver.find_element_by_xpath('//*[@id="CompanyAddLine1"]')
        CompanyAddress_box = Driver.driver.find_element_by_xpath('//*[@id="CompanyAddLine1"]')
        CompanyAdd = " Pandan Indah "
        CompanyAddress_box.send_keys(CompanyAdd)

        # Edit Company Address line 2
        Driver.driver.find_element_by_xpath('//*[@id="CompanyAddLine2"]')
        CompanyAddress2_box = Driver.driver.find_element_by_xpath('//*[@id="CompanyAddLine2"]')
        CompanyAdd2 = " Anta Permata "
        CompanyAddress2_box.send_keys(CompanyAdd2)

        # Edit Postcode 
        Driver.driver.find_element_by_xpath('//*[@id="Postcode"]')
        PostcodeAddress_box = Driver.driver.find_element_by_xpath('//*[@id="Postcode"]')
        PostcodeAdd = " 48000 "
        PostcodeAddress_box.send_keys(PostcodeAdd)

        # Edit City 
        Driver.driver.find_element_by_xpath('//*[@id="City"]')
        CityAddress_box = Driver.driver.find_element_by_xpath('//*[@id="City"]')
        CityAdd = " Rawang "
        CityAddress_box.send_keys(CityAdd)

        # Edit District
        Driver.driver.find_element_by_xpath('//*[@id="District"]')
        DistrictAddress_box = Driver.driver.find_element_by_xpath('//*[@id="District"]')
        DistrictAdd = " Hulu Selangor "
        DistrictAddress_box.send_keys(DistrictAdd)

        # Edit Country
        Country_list = Driver.driver.find_element_by_xpath('//*[@id="for-country"]')
        dropdownCY = Select(Country_list)
        dropdownCY.select_by_value('20')

        # Edit State
        State_list = Driver.driver.find_element_by_xpath('//*[@id="for-state"]')
        dropdownST = Select(State_list)
        dropdownST.select_by_value('25')

        # Edit Telephone No
        Driver.driver.find_element_by_xpath('//*[@id="PhoneNumber"]')
        ProfilesTelephoneNo_box = Driver.driver.find_element_by_xpath('//*[@id="PhoneNumber"]')
        ProfilesTelNo = " 0132443231 "
        ProfilesTelephoneNo_box.send_keys(ProfilesTelNo)

        # Edit Fax No
        Driver.driver.find_element_by_xpath('//*[@id="FaksNumber"]')
        ProfilesFaxNumber_box = Driver.driver.find_element_by_xpath('//*[@id="FaksNumber"]')
        ProfilesFaxNo = " 000000 "
        ProfilesFaxNumber_box.send_keys(ProfilesFaxNo)

        # Edit Scheme
        Scheme_list = Driver.driver.find_element_by_xpath('//*[@id="for-BussType"]')
        dropdownSC = Select(Scheme_list)
        dropdownSC.select_by_index('7')

        # Edit Industry Size
        IndustrySize_list = Driver.driver.find_element_by_xpath('//*[@id="for-IndustryType"]')
        dropdownIS = Select(IndustrySize_list)
        dropdownIS.select_by_index('2')

        # Edit Website URL
        Driver.driver.find_element_by_xpath('//*[@id="Website"]')
        WebsiteURL_box = Driver.driver.find_element_by_xpath('//*[@id="Website"]')
        WebURL = " shopee.my "
        WebsiteURL_box.send_keys(WebURL)

        # Edit Company email
        Driver.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[3]/div/div/div[2]/div/div/div[8]/div[2]/input')
        CompanyEmail_box = Driver.driver.find_element_by_xpath('//*[@id="CompanyEmail"]')
        CompEmail = " kiki@gmail.com "
        CompanyEmail_box.send_keys(CompEmail)
       
        #Click Button [Save]
        Driver.driver.find_element_by_xpath('//*[@id="btnUpdateCompanyProfile"]').click()

        Driver.driver.find_element_by_xpath('//*[@id="btnUpdateCompanyProfile"]').click()

        print("TEST PASSED> Able to edit company details")
    except Exception as e:
        print ("TEST FAILED> Unable to edit company details ")
        time.sleep(2)

        #TC Profiles 5 --> Add Contact Person 
def TC_Profiles5():
    print("\nTesting Profiles 5. Add Contact Person ")
    # 1. Go to (Company information -> Profiles)

    try: 
        time.sleep(2)
        # Must select company first 
        # 1. Click Button [Add]
        Driver.driver.find_element_by_xpath('//*[@id="btnContactPerson"]').click()
        
        time.sleep(2)
        
        # Select staff information or not
        # If No 
        # Add Name 
    
        Driver.driver.find_element_by_xpath('//*[@id="EmployeeName"]')
        ContactPersonName_box = Driver.driver.find_element_by_xpath('//*[@id="EmployeeName"]')
        CPName = " "
        ContactPersonName_box.send_keys(CPName)

        # Add Email
        Driver.driver.find_element_by_xpath('//*[@id="Email"]')
        ContactPersonEmail_box = Driver.driver.find_element_by_xpath('//*[@id="Email"]')
        CPEmail = " "
        ContactPersonEmail_box.send_keys(CPEmail)

        # Add ID Number
        Driver.driver.find_element_by_xpath('//*[@id="IdNumber"]')
        ContactPersonID_box = Driver.driver.find_element_by_xpath('//*[@id="IdNumber"]')
        CPID = " "
        ContactPersonID_box.send_keys(CPID)

        # Add Religion
        Religion_list = Driver.driver.find_element_by_xpath('//*[@id="ReligionId"]')
        dropdownR = Select(Religion_list)
        dropdownR.select_by_value('')

        #Add Office Number 
        OfficeNumber_list = Driver.driver.find_element_by_xpath('//*[@id="OfficeNo"]')
        dropdownON = Select(OfficeNumber_list)
        dropdownON.select_by_value('')

        #Add Working Hours (start)
        WorkingHours_list = Driver.driver.find_element_by_xpath('//*[@id="StartWorkingHour"]')
        dropdownWH = Select(WorkingHours_list)
        dropdownWH.select_by_value('')

        #Add Working Hours (end)
        WorkingHours_list = Driver.driver.find_element_by_xpath('//*[@id="EndWorkingHour"]')
        dropdownWH = Select(WorkingHours_list)
        dropdownWH.select_by_value('')

        # if yes (contatct info)
        # Select Name
        Driver.driver.find_element_by_xpath('')
        ContactPersonName_box = Driver.driver.find_element_by_xpath('')
        CPName = " "
        ContactPersonName_box.send_keys(CPName)
        
        #Click Button [Save]
        Driver.driver.find_element_by_xpath('//*[@id="btnUpdateCompanyProfile"]').click()

        Driver.driver.find_element_by_xpath('//*[@id="btnUpdateCompanyProfile"]').click()

        print("TEST PASSED> Able to edit company details")
    except Exception as e:
        print ("TEST FAILED> Unable to edit company details ")
        time.sleep(2)

        #Edit Contact person 





        #TC Profiles 6 --> Add Halal Executive 
def TC_Profiles6():
    print("\nTesting Profiles 6. Add Halal Executive ")
    # 1. Go to (Company information -> Profiles)

    try: 
        time.sleep(2)
        # Must select company first 
        # 1. Click Button [Add]
        Driver.driver.find_element_by_xpath('//*[@id="btnHalalExec"]').click()
        
        time.sleep(2)
        
        # Select staff information or not
        # If No 
        # Add Name 
    
        Driver.driver.find_element_by_xpath('//*[@id="EmployeeName"]')
        ExecutiveName_box = Driver.driver.find_element_by_xpath('//*[@id="EmployeeName"]')
        MHEName = " "
        ExecutiveName_box.send_keys(MHEName)

        # Add Email
        Driver.driver.find_element_by_xpath('//*[@id="Email"]')
        ExecutiveEmail_box = Driver.driver.find_element_by_xpath('//*[@id="Email"]')
        MHEEmail = " "
        ExecutiveEmail_box.send_keys(MHEEmail)

        # Add ID Number
        Driver.driver.find_element_by_xpath('//*[@id="IdNumber"]')
        ExecutiveID_box = Driver.driver.find_element_by_xpath('//*[@id="IdNumber"]')
        MHEID = " "
        ExecutiveID_box.send_keys(MHEID)

        # Add Religion
        Religion_list = Driver.driver.find_element_by_xpath('//*[@id="ReligionId"]')
        dropdownR = Select(Religion_list)
        dropdownR.select_by_value('')

        # Add Designation
        Designation_list = Driver.driver.find_element_by_xpath('//*[@id="DesignationId"]')
        dropdownD = Select(Designation_list)
        dropdownD.select_by_value('')

        #Add Office Number 
        OfficeNumber_list = Driver.driver.find_element_by_xpath('//*[@id="OfficeNo"]')
        dropdownON = Select(OfficeNumber_list)
        dropdownON.select_by_value('')

        #Add Working Hours (start)
        WorkingHours_list = Driver.driver.find_element_by_xpath('//*[@id="StartWorkingHour"]')
        dropdownWH = Select(WorkingHours_list)
        dropdownWH.select_by_value('')

        #Add Working Hours (end)
        WorkingHours_list = Driver.driver.find_element_by_xpath('//*[@id="EndWorkingHour"]')
        dropdownWH = Select(WorkingHours_list)
        dropdownWH.select_by_value('')
        
        # if yes (contatct info)
        # Select Name
        Driver.driver.find_element_by_xpath('')
        ContactPersonName_box = Driver.driver.find_element_by_xpath('')
        CPName = " "
        ContactPersonName_box.send_keys(CPName)

        #Click Button [Save]
        Driver.driver.find_element_by_xpath('//*[@id="btnUpdateCompanyProfile"]').click()

        Driver.driver.find_element_by_xpath('//*[@id="btnUpdateCompanyProfile"]').click()

        print("TEST PASSED> Able to edit company details")
    except Exception as e:
        print ("TEST FAILED> Unable to edit company details ")
        time.sleep(2)

         #TC Profiles 7 --> Add No. Of Employees 
def TC_Profiles7():
    print("\nTesting Profiles 7. Add No. Of Employees ")
    # 1. Go to (Company information -> Profiles)

    try: 
        time.sleep(2)
        # Must select company first 
        # 1. Click Button [Add]
        Driver.driver.find_element_by_xpath('//*[@id="btnHalalExec"]').click()
        
        time.sleep(2)

        #No Of Employees 
        Management_muslim = Driver.driver.find_element_by_xpath('//*[@id="Comp_Muslim_Management"]')
        dropdownMM = Select(Management_muslim)
        dropdownMM.select_by_value('')    

        Management_nonmuslim = Driver.driver.find_element_by_xpath('//*[@id="Comp_NonMuslim_Management"]')
        dropdownMN = Select(Management_nonmuslim)
        dropdownMN.select_by_value('')   

        Production_muslim = Driver.driver.find_element_by_xpath('//*[@id="Comp_Muslim_Production"]')
        dropdownPM = Select(Production_muslim)
        dropdownPM.select_by_value('') 

        Production_nonmuslim = Driver.driver.find_element_by_xpath('//*[@id="Comp_NonMuslim_Production"]')
        dropdownPN = Select(Production_nonmuslim)
        dropdownPN.select_by_value('') 

        Food_muslim = Driver.driver.find_element_by_xpath('//*[@id="Comp_Muslim_FoodHandler"]')
        dropdownFM = Select(Food_muslim)
        dropdownFM.select_by_value('') 

        Food_nonmuslim = Driver.driver.find_element_by_xpath('//*[@id="Comp_NonMuslim_FoodHandler"]')
        dropdownPM = Select(Food_nonmuslim)
        dropdownPM.select_by_value('') 

        Chef_muslim = Driver.driver.find_element_by_xpath('//*[@id="Comp_Muslim_Chef"]')
        dropdownCM = Select(Chef_muslim)
        dropdownCM.select_by_value('') 

        Chef_nonmuslim = Driver.driver.find_element_by_xpath('//*[@id="Comp_NonMuslim_Chef"]')
        dropdownCN = Select(Chef_nonmuslim)
        dropdownCN.select_by_value('') 

         #Click Button [Save]
        Driver.driver.find_element_by_xpath('//*[@id="btnUpdateCompanyProfile"]').click()

        print("TEST PASSED> Able to edit company details")
    except Exception as e:
        print ("TEST FAILED> Unable to edit company details ")
        time.sleep(2)

Profiles.TC_Profiles1()
time.sleep(2)
Profiles.TC_Profiles4()
time.sleep(2)
Profiles.TC_Profiles5
time.sleep(2)
Driver.driver.close()