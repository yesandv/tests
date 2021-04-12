def test_search_and_cognates_button():
    open_initial_page()
    dictionary = 'Dictionary of the Middle-Cheptsa Dialect of the Northern Dialect of the Udmurt Language (Village Kabakovo, Glazov District)'
    open_lexical_view(dictionary)
    wait_for_successful_click("//div[contains(@class,'ui tabular menu')]/a[contains(text(), 'Edit')]", 15)
    WebDriverWait(config.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//button[text() = 'Cognates']")))
    element = WebDriverWait(config.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@class, 'white')]")))
    input_text = "perV"
    element.send_keys(input_text)
    WebDriverWait(config.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@type, 'submit')]"))).click()
    WebDriverWait(config.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//button[text() = 'Cognates']"))).click()
    WebDriverWait(config.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//a[text() = 'Add connection']"))).click()
    element = WebDriverWait(config.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder = 'Type to search']")))
    element.clear()
    element.send_keys(input_text)
    WebDriverWait(config.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//i[contains(@class, 'search icon')]"))).click()
    WebDriverWait(config.driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'sc-kgoBCf kRHZvY')]"))).click()
    WebDriverWait(config.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//tbody[*]/tr[1]/td[*]/button[text() = 'Connect']"))).click()
    WebDriverWait(config.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//div[text() = 'Connected']")))
    WebDriverWait(config.driver, 15).until_not(EC.visibility_of_element_located((By.XPATH, "//div[text() = 'Connected']")))
    WebDriverWait(config.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//table[contains(@class, 'ui celled padded table')]")))

    #Return to the original state
    WebDriverWait(config.driver, 15).until(EC.visibility_of_element_located((By.XPATH,  "//body[*]/div[3]/div[*]/div[*]/button[text() = 'Cancel']"))).click()
    WebDriverWait(config.driver, 15).until(EC.visibility_of_element_located((By.XPATH,  "//a[text() = 'View']"))).click()
    WebDriverWait(config.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//button[text() = 'Disconnect']"))).click()
    WebDriverWait(config.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//div[text() = 'Disconnected']")))
    WebDriverWait(config.driver, 15).until_not(EC.visibility_of_element_located((By.XPATH, "//div[text() = 'Disconnected']")))
    WebDriverWait(config.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//button[text() = 'Cancel']"))).click()
    
    #Clear search
    element = WebDriverWait(config.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@class, 'white')]")))
    element.clear()
    element.send_keys(Keys.ENTER)