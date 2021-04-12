def test_lex_cognate_analysis_for_perspective_authors():
    dictionary = u'Dictionary of Izhma dialect of Komi-Zyrian language'
    open_lexical_view(dictionary)
    waiting_for_table_to_appear()
    #Open Tools menu
    element = WebDriverWait(config.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Tools')]/../i")))
    scroll_to(element)
    WebDriverWait(config.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Tools')]/../i"))).click()
    time.sleep(1) #Do not remove
    assert(len(config.driver.find_elements_by_xpath("//div[contains(text(), '"+ Cognate_analysis +"')]")), 1)


def test_no_compute_for_nonauthor():
    open_initial_page()
    logout()
    dictionary = u'Dictionary of Izhma dialect of Komi-Zyrian language'
    open_lexical_view(dictionary)
    waiting_for_table_to_appear()
    #Open Tools menu
    element = WebDriverWait(config.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Tools')]/../i")))
    scroll_to(element)
    WebDriverWait(config.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Tools')]/../i"))).click()
    time.sleep(1) #Do not remove
    #Verify that for nonauthors Cognate commands are not accessible
    assert(len(config.driver.find_elements_by_xpath("//div[contains(text(), '"+ Cognate_analysis +"')]")), 0, "Cognate command should not be found")


def test_lex_cognate_analysis():
    open_initial_page()
    login(admin, password)
    dictionary = u'Dictionary of Izhma dialect of Komi-Zyrian language'
    open_lexical_view(dictionary)
    waiting_for_table_to_appear()
    open_tools(Cognate_analysis)    
    WebDriverWait(config.driver, 25).until(EC.visibility_of_element_located((By.XPATH, "//button[text() = 'Compute']"))).click()
    WebDriverWait(config.driver, 240).until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(), 'Analysis results')]")))
    text_to_verify = 'XLSX-exported analysis results'
    WebDriverWait(config.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), '" + text_to_verify + "')]")))
    text_to_verify = u'ЭТИМОЛОГИЧЕСКИЙ АНАЛИЗ'
    WebDriverWait(config.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//pre[contains(text(), '" + text_to_verify + "')]")))