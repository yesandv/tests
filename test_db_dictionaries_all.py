def test_dictionaries_display_mode():
    #Open Dictionaries page
    open_lang_db_dictionaries()
    WebDriverWait(config.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//form/div/label[text() = 'Display mode']")))
    #Verify options
    WebDriverWait(config.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//form//div[text() = 'By Languages']")))
    WebDriverWait(config.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//form//div[text() = 'By Grants']")))
    WebDriverWait(config.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//form//div[text() = 'By Organizations']")))


def test_dictionaries_sorting():
    #Sort by Organizations
    #Selecting by Organizations
    WebDriverWait(config.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//form//div[text() = 'By Organizations']"))).click()
    #Verifying Display mode By Organization
    organization_to_verify = u'Институт языка, литературы и истории КарНЦ РАН'
    WebDriverWait(config.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'" + organization_to_verify + "')]")))
    #Selecting by Languages to run following tests
    WebDriverWait(config.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//form//div[text() = 'By Languages']"))).click()
    assert(len(config.driver.find_elements_by_xpath("//div[contains(text(),'" + organization_to_verify + "')]")), 0, "Organizations should be invisible")