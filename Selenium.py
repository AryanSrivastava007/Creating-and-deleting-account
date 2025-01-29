from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# Initialize the browser driver (assuming ChromeDriver is in PATH)
driver = webdriver.Chrome()

try:
    # Step 2: Navigate to the URL
    driver.get('http://automationexercise.com')
    driver.maximize_window()
    time.sleep(2)  # Wait for the page to load

    # Step 3: Verify that the home page is visible successfully
    assert "Automation Exercise" in driver.title
    print("Home page is visible successfully.")

    # Step 4: Click on 'Signup / Login' button
    driver.find_element(By.LINK_TEXT, 'Signup / Login').click()
    time.sleep(2)


    #Step 5: Verify 'New User Signup!' is visible
    assert driver.find_element(By.XPATH, '//h2[text()="New User Signup!"]').is_displayed()
    print("'New User Signup!' is visible.")
    time.sleep(2)

    # Step 6: Enter name and email address
    driver.find_element(By.NAME, 'name').send_keys('Aryan Srivastava')
    driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]').send_keys('aryansrivastava04643@gmail.com')
    time.sleep(2)

    # Step 7: Click 'Signup' button
    driver.find_element(By.XPATH, '//button[text()="Signup"]').click()
    time.sleep(2)

    # Step 8: Verify 'ENTER ACCOUNT INFORMATION' is visible
    assert driver.find_element(By.XPATH, '//b[text()="Enter Account Information"]').is_displayed()
    print("'ENTER ACCOUNT INFORMATION' is visible.")
    time.sleep(2)

    # Step 9: Fill account details
    driver.find_element(By.ID, 'id_gender1').click()  # Title: Mr.
    driver.find_element(By.ID, 'password').send_keys('password123')
    time.sleep(2)

    # Date of birth
    Select(driver.find_element(By.ID, 'days')).select_by_value('15')
    Select(driver.find_element(By.ID, 'months')).select_by_value('7')
    Select(driver.find_element(By.ID, 'years')).select_by_value('1998')
    time.sleep(2)

    # Step 10: Select checkbox 'Sign up for our newsletter!'
    driver.find_element(By.ID, 'newsletter').click()
    time.sleep(2)

    # Step 11: Select checkbox 'Receive special offers from our partners!'
    driver.find_element(By.ID, 'optin').click()
    time.sleep(2)

    # Step 12: Fill additional details
    driver.find_element(By.ID, 'first_name').send_keys('Aryan')
    driver.find_element(By.ID, 'last_name').send_keys('Srivastava')
    driver.find_element(By.ID, 'company').send_keys('MyCompany')
    driver.find_element(By.ID, 'address1').send_keys('123 Street Name')
    driver.find_element(By.ID, 'address2').send_keys('Apt 456')
    Select(driver.find_element(By.ID, 'country')).select_by_visible_text('India')
    driver.find_element(By.ID, 'state').send_keys('Uttar Pradesh')
    driver.find_element(By.ID, 'city').send_keys('Lucknow')
    driver.find_element(By.ID, 'zipcode').send_keys('226001')
    driver.find_element(By.ID, 'mobile_number').send_keys('9876543210')
    time.sleep(2)

    # Step 13: Click 'Create Account' button
    driver.find_element(By.XPATH, '//button[text()="Create Account"]').click()
    time.sleep(2)

    # Step 14: Verify that 'ACCOUNT CREATED!' is visible
    assert driver.find_element(By.XPATH, '//b[text()="Account Created!"]').is_displayed()
    print("'ACCOUNT CREATED!' is visible.")
    time.sleep(2)

    # Step 15: Click 'Continue' button
    driver.find_element(By.XPATH, '//a[text()="Continue"]').click()
    time.sleep(2)

    # Step 16: Verify that 'Logged in as username' is visible
    assert driver.find_element(By.XPATH, '//a[contains(text(), "Logged in as")]').is_displayed()
    print("'Logged in as username' is visible.")
    time.sleep(2)

    # Step 17: Click 'Delete Account' button
    driver.find_element(By.LINK_TEXT, 'Delete Account').click()
    time.sleep(2)

    # Step 18: Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    assert driver.find_element(By.XPATH, '//b[text()="Account Deleted!"]').is_displayed()
    print("'ACCOUNT DELETED!' is visible.")
    driver.find_element(By.XPATH, '//a[text()="Continue"]').click()
    time.sleep(2)

except AssertionError as e:
    print("AssertionError:", e)
except Exception as e:
    print("Error:", e)
finally:
    # Close the browser
    driver.quit()
