import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import extract_glossary

def open_google_and_search(query)-> None:
	"""Open Chrome, navigate to Google, and perform a search for `query`.

	Requires a matching ChromeDriver on PATH.
	"""
	chrome_options = Options()
	# keep browser open after script ends (set False to close automatically)
	chrome_options.add_experimental_option("detach", True)

	driver = webdriver.Chrome(options=chrome_options)
	driver.get("https://www.google.com/search?" + query)

	# Wait for the search box to appear, then type the query and submit
	wait = WebDriverWait(driver, 10)
	search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
	search_box.clear()
	search_box.send_keys(query)
	search_box.send_keys(Keys.RETURN)

	# Wait for results to load
	wait.until(EC.title_contains(query))
	# print("Opened Google and searched for:", query)

	# keep open briefly for manual inspection
	time.sleep(2)


if __name__ == "__main__":
	# change the argument if you want a different search term
	# print(extract_glossary.main())
	open_google_and_search(str(extract_glossary.main()))
	
