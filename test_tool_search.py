def test_map_point():
    #Zoom out and click on the mark on the map
    WebDriverWait(config.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='leaflet-control-zoom-out']"))).click()
    time.sleep(1) 
    WebDriverWait(config.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'leaflet-marker-icon')]/span"))).click()
    time.sleep(1)