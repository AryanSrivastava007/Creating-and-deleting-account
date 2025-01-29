# Automation Exercise - Selenium Script

## Overview
This Selenium script automates the signup, login, and deletion process for a user account on [Automation Exercise](http://automationexercise.com). It performs the following steps:

1. Launches the browser and navigates to the website.
2. Verifies that the homepage is visible.
3. Clicks on the 'Signup / Login' button.
4. Verifies the presence of the 'New User Signup!' form.
5. Enters user details (name and email) and proceeds with signup.
6. Fills out the account creation form, including:
   - Gender selection
   - Password entry
   - Date of birth selection
   - Newsletter and special offers opt-in
   - Address and contact details
7. Creates an account and verifies successful creation.
8. Logs in and verifies the logged-in status.
9. Deletes the account and confirms deletion.

## Requirements
### Prerequisites
Ensure you have the following installed:
- Python (>=3.7)
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Selenium package

### Installation
1. Install Selenium:
   ```sh
   pip install selenium
   ```
2. Download and set up ChromeDriver:
   - Find the latest version at [ChromeDriver](https://sites.google.com/chromium.org/driver/).
   - Place the executable in your system PATH or specify its location in the script.

## Usage
1. Clone the repository or download the script.
2. Run the script using:
   ```sh
   python script.py
   ```
3. The script will automate account creation and deletion on the website.

## Error Handling
The script includes exception handling for:
- **AssertionError:** Fails when an expected element is not found.
- **General Exception:** Catches other runtime errors and prints them.

## Notes
- The script uses `time.sleep()` to wait for elements to load. Consider replacing it with explicit waits (`WebDriverWait`) for better performance.
- Ensure that the email used in signup is unique for each run or modify the script to generate a new email dynamically.

## Author
[Aryan Srivastava](https://github.com/AryanSrivastava007)

## License
This project is open-source and free to use for educational purposes.
