import Driver
import time
import Login
import NavigateMenu


#Dashboard
def Dashboard():
   try:
   #Click Dashboard
      Driver.driver.find_element_by_xpath('//*[@id="DashboardModule"]').click()
      Driver.driver.find_elements_by_partial_link_text('General')
      Driver.driver.find_elements_by_partial_link_text('Total Halal Certificate')
   except Exception as e:
      print ("TEST FAILED! Unable to navigate Click Menu (Dashboard). Error",e)

#Reference Data - Reference Data - General Data
def GeneralData():
   try:
   #Click GeneralData
      Driver.driver.find_element_by_xpath('//*[@id="AdminModule1"]').click()  # Click on Admin menu
      Driver.driver.find_element_by_xpath('//*[@id="ReferenceData1"]').click()  # Click on Reference Data menu
      Driver.driver.find_element_by_xpath('//*[@id="GeneralData"]').click() # Click on General Data menu
      Driver.driver.find_elements_by_partial_link_text('General Data')
   except Exception as e:
      print ("TEST FAILED! Unable to navigate Click Menu (Reference Data - Reference Data - General Data). Error",e)

#Reference Data - Reference Data - State
def State():
   try:
   #Click GeneralData
      Driver.driver.find_element_by_xpath('//*[@id="AdminModule1"]').click()  # Click on Admin menu
      Driver.driver.find_element_by_xpath('//*[@id="ReferenceData1"]').click()  # Click on Reference Data menu
      Driver.driver.find_element_by_xpath('//*[@id="State"]').click() # Click on State menu
      Driver.driver.find_elements_by_partial_link_text('State')
   except Exception as e:
      print ("TEST FAILED! Unable to navigate Click Menu (Reference Data - Reference Data - State). Error",e)

#Admin Module
def ManageUsers():
   try:
   #Click Menu (Admin -> Manage Users)
      Driver.driver.find_element_by_xpath('//*[@id="AdminModule1"]').click()  # Click on Admin button
      Driver.driver.find_element_by_xpath('//*[@id="ManageUser"]').click() # Click on Manage Users button
   except Exception as e:
      print("TEST FAILED! Unable to navigate Click Menu (Admin -> Manage Users). Error",e)

#Company Information
def ManagePremise():
   try:
   #Click Menu (Premise -> Manage Premise)
      Driver.driver.find_element_by_xpath('//*[@id="CompModule1"]').click() # Click on Manage Premise button
      time.sleep(2);
      Driver.driver.find_element_by_xpath('//*[@id="premise2"]').click()  # Click on Manage Premise button
      time.sleep(2);
      Driver.driver.find_element_by_xpath('//*[@id="ManagePremise2"]').click()  # Click on Manage Premise button
      time.sleep(2);
   except Exception as e:
      print("TEST FAILED! Unable to navigate Click Menu (Admin -> Manage Users). Error",e)

#Verify Halal Search Engine
def verifyHalalSearchEngine():
   try:
   #Click Menu (Premise -> Manage Premise)
      Driver.driver.find_element_by_xpath('//*[@id="VH_Search"]').click() # Click on Manage Premise button
      time.sleep(2);
   except Exception as e:
      print("TEST FAILED! Unable to navigate Click Menu (Admin -> Manage Users). Error",e)


def manageCompany():
    
    try:
        # 1. Go to (Admin -> Manage Companies)
        Driver.driver.find_element_by_xpath('//*[@id="AdminModule1"]').click()
        time.sleep(2)
        Driver.driver.find_element_by_xpath('//*[@id="ManageCompanies"]').click()
        time.sleep(2)
        print("Able to go to Manage Companies page")
    except Exception as e:
        print("FAILED. ", e)