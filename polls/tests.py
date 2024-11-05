from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

class MySeleniumTests(StaticLiveServerTestCase):
	#fixtures = ['testdb.json',]

	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		opts = Options()
		cls.selenium = WebDriver(options=opts)
		cls.selenium.implicitly_wait(5)
		user = User.objects.create_user("isard", "isard@isardvdi.com", "pirineus")
		user.is_superuser = True
		user.is_staff = True
		user.save()

	def test_login(self):
		self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))

		username_input = self.selenium.find_element(By.NAME,"username")
		username_input.send_keys('isard')
		password_input = self.selenium.find_element(By.NAME,"password")
		password_input.send_keys('pirineus')
		self.selenium.find_element(By.XPATH,'//input[@value="Log in"]').click()

		self.selenium.find_element(By.XPATH,'/html/body/div/div/main/div/div[1]/div[2]/table/tbody/tr[2]/td[1]/a').click()
		question_input_1 = self.selenium.find_element(By.XPATH,'//*[@id="id_question_text"]')
		question_input_1.send_keys('Testing question 1')
		self.selenium.find_element(By.XPATH,'//*[@id="fieldset-0-date-information-1-heading"]').click()
		self.selenium.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div/form/div/fieldset[2]/details/div/div/div/p/span[1]/a[1]').click()
		self.selenium.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div/form/div/fieldset[2]/details/div/div/div/p/span[2]/a[1]').click()
		self.selenium.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div/form/div/div[2]/input[2]').click()
		question_input_2 = self.selenium.find_element(By.XPATH,'//*[@id="id_question_text"]')
		question_input_2.send_keys('Testing question 2')
		self.selenium.find_element(By.XPATH,'//*[@id="fieldset-0-date-information-1-heading"]').click()
		self.selenium.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div/form/div/fieldset[2]/details/div/div/div/p/span[1]/a[1]').click()
		self.selenium.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div/form/div/fieldset[2]/details/div/div/div/p/span[2]/a[1]').click()
		self.selenium.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div/form/div/div[2]/input[1]').click()

		self.selenium.find_element(By.XPATH,'/html/body/div/div/nav/div[2]/table/tbody/tr[1]/th/a').click()
		self.selenium.find_element(By.XPATH,'/html/body/div/div/main/div/div/ul/li/a').click()

		self.selenium.find_element(By.XPATH,'/html/body/div/div/main/div/div/form/div/fieldset/div[1]/div/div/div/select/option[2]').click()
		choice_input_1 = self.selenium.find_element(By.XPATH,'//*[@id="id_choice_text"]')
		choice_input_1.send_keys('Testing choice 1')
		self.selenium.find_element(By.XPATH,'/html/body/div/div/main/div/div/form/div/div/input[2]').click()
		self.selenium.find_element(By.XPATH,'/html/body/div/div/main/div/div/form/div/fieldset/div[1]/div/div/div/select/option[2]').click()
		choice_input_2 = self.selenium.find_element(By.XPATH,'//*[@id="id_choice_text"]')
		choice_input_2.send_keys('Testing choice 2')
		self.selenium.find_element(By.XPATH,'/html/body/div/div/main/div/div/form/div/div/input[1]').click()

		self.selenium.find_element(By.XPATH,'/html/body/div/div/main/div/div/ul/li/a').click()

		self.selenium.find_element(By.XPATH,'/html/body/div/div/main/div/div/form/div/fieldset/div[1]/div/div/div/select/option[3]').click()
		choice_input_3 = self.selenium.find_element(By.XPATH,'//*[@id="id_choice_text"]')
		choice_input_3.send_keys('Testing choice 3')
		self.selenium.find_element(By.XPATH,'/html/body/div/div/main/div/div/form/div/div/input[2]').click()
		self.selenium.find_element(By.XPATH,'/html/body/div/div/main/div/div/form/div/fieldset/div[1]/div/div/div/select/option[3]').click()
		choice_input_4 = self.selenium.find_element(By.XPATH,'//*[@id="id_choice_text"]')
		choice_input_4.send_keys('Testing choice 4')
		self.selenium.find_element(By.XPATH,'/html/body/div/div/main/div/div/form/div/div/input[1]').click()

		self.selenium.find_element(By.XPATH,'/html/body/div/div/nav/div[2]/table/tbody/tr[2]/th/a').click()
		self.selenium.find_element(By.XPATH,'/html/body/div/div/main/div/div/div/div/form/div[2]/table/tbody/tr[2]/th/a').click()

		try:
			inline_element = self.selenium.find_element(By.CLASS_NAME, "inline-related")
			self.assertIn("inline-related", inline_element.get_attribute("class"))
			print("¡El elemento tiene la clase inline-related! @ragalisteofi")
		except:
			self.fail("El elemento con la clase 'inline-related' no se encontró en la página. @ragalisteofi")

	def tearDown(self):
		self.selenium.quit()