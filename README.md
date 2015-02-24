# Selenium Automation Suite (Python)

For the automation testing framework that I was requested to make, I decided to go with Selenium. I have used Selenium in the past so I knew it would get me started in the right direction. When I did use selenium, it was building off an already existing framework. I have never started from scratch in creating an automation suite so this experience was very fun and rewarding.

Due to time constraints with school, work, etc., the work here is what I had time to complete. With more time, I could have added additional test to the suite for more test coverage.

# Set Up

If you wish to run my test locally:

 1. Fork my repo locally so you have the files listed. 
 
  		git clone https://github.com/daotoo/automation.git /your/local/path
    
 2. Assuming you have python installed or a python virtual environment created run this command from the root:

		pip install -r requirements.txt
This will install the necessary python packages.

3. Set environment variables

In the code, environment variables are used for storing data such as emails, file paths, and other personal data. Set these variables to the correct values in your `.bash_profile`

	export HUDL_EMAIL="your_hudl_email@email.com"

	export HUDL_PASS="your_hudl_pass"
	
	export HUDL_IMPORT_FILE="/Aboslute/path/to/roster_csv_or_xlsx_file"
	
	export Chrome_driver="/path/to/local/chromedriver"

4. Run `python Suite.py` 

This will run the suite of tests using FireFox as the webdriver. If you wish to run with chrome, in `Suite.py` change `self.driver = webdriver.Firefox()` to `self.driver = webdriver.Chrome(self.chrome_driver_path)`. Assuming you have the `Chrome_driver` set in your environment variables. The latest `chromedriver` can be found in this repo.

**Note:** I had some consistency issues with chrome so left Firefox as the default.

[Screencast](http://screencast.com/t/PzsV0JqD8JFs): Screen cast of the test run.

# Manual Testing

Manual testing should never be disregarded as its just as important as automation. When small changes are made to applications, it can be easy to just jump in, manually test it, and verify the functionality. Automation is great for this as well, but also for regression testing. Since I wasn't able to get as many tests in as I could, things to manually test would include all the functions that I have automation tests already, exporting files, and filtering by name, or season. 

# Extras

For the `edit_player` and `add_player` functions. I could have gone into further depth and allowed for testers to add more information (cell phone carrier, number, address, etc.) but stuck with the core information that was shown. I'm hoping you got the gist of what I was going for there with those functions.