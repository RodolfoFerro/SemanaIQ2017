from selenium import webdriver
from time import sleep
import requests
import argparse

# Global:
molecule = "Caffeine"

# Construct the argument parser:
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--mol", default=molecule, help="Input molecule.")
args = vars(ap.parse_args())


def scraper(mol):
    # Browser launch with chromedriver:
    browser = webdriver.Chrome()
    # browser = webdriver.Safari()

    # Set url and open it on Chrome:
    url = 'http://opsin.ch.cam.ac.uk'
    browser.get(url)

    # Search molecule:
    img, smiles = search_mol(browser, mol)

    # Close browser:
    browser.quit()
    return img, smiles


def get_img(img_url):
    pic = False
    response = requests.get(img_url, stream=True)
    with open('molecule.png', 'wb') as file:
        for chunk in response.iter_content():
            file.write(chunk)
        pic = True
    response.close()
    return pic


def search_mol(browser, mol):
    # Find ID and input test data:
    browser.find_element_by_id('chemicalName').clear()
    browser.find_element_by_id('chemicalName').send_keys(mol)

    # Look for button and click it:
    browser.find_element_by_xpath(
        '//*[@id="chemicalNameForm"]/fieldset/input[2]').click()

    # Wait for content:
    sleep(1)

    # Search results and return them:
    img_url = browser.find_element_by_id('depiction').get_attribute('src')
    smiles = browser.find_element_by_id('smiles').text

    if len(smiles) is not 0:
        image = get_img(img_url)
        return img_url, smiles
    else:
        return None, None


if __name__ == '__main__':
    mol = args["mol"]
    img, smiles = scraper(mol)
    print(img)
    print(smiles)
