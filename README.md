## Scrap Voter List ##

***Not Working Yet, Error : `selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"/html/body/div[4]/div/div[2]/div/form/div[1]/div[1]/select"}
`***

StackTrace : Conda Base Environment
`Traceback (most recent call last):
  File "main.py", line 17, in <module>
    district_selector = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/form/div[1]/div[1]/select')
  File "C:\ProgramData\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 394, in find_element_by_xpath
    return self.find_element(by=By.XPATH, value=xpath)
  File "C:\ProgramData\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 976, in find_element
    return self.execute(Command.FIND_ELEMENT, {
  File "C:\ProgramData\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "C:\ProgramData\Anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"/html/body/div[4]/div/div[2]/div/form/div[1]/div[1]/select"}
  (Session info: chrome=84.0.4147.125)`

StackTrace : Pipenv Virtual Environment
`Traceback (most recent call last):
  File "main.py", line 17, in <module>
    district_selector = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/form/div[1]/div[1]/select')
  File "C:\Users\Abdu\.virtualenvs\Scrap_Voter_List-x57ooo97\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 394, in find_element_by_xpath
    return self.find_element(by=By.XPATH, value=xpath)
  File "C:\Users\Abdu\.virtualenvs\Scrap_Voter_List-x57ooo97\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 976, in find_element
    return self.execute(Command.FIND_ELEMENT, {
  File "C:\Users\Abdu\.virtualenvs\Scrap_Voter_List-x57ooo97\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response) `

----------

***Not Completed Yet, Todo : Automation of captcha challenge***

----------
**Note : Pipenv based developemnt is encouraged, however requirements.txt is also available - if you prefer that way. A conda environment file is also available.**
