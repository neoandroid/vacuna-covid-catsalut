import email
import imaplib
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

dni = ''
cip = ''
phone = ''
name = ''
surname = ''
surname2 = ''
mail = ''

imap_ssl_host = 'imap.gmail.com'
imap_ssl_port = 993
imap_folder = '[Gmail]/Enviados'
imap_username = ''
imap_password = ''


def read_catsalut_verification_code():
    server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)

    server.login(imap_username, imap_password)
    server.select(imap_folder)

    status, data = server.search(None, 'SUBJECT', '"SMS Salut"')
    for num in data[0].split():
        status, data = server.fetch(num, '(RFC822)')
        email_msg = data[0][1]
        #print(email_msg.decode('utf-8'))
       
        msg = email.message_from_string(email_msg.decode('utf-8'))
        payload = msg.get_payload(decode=True)
        msg_text = payload.decode()
        code = msg_text
        #print(msg_text)

    if 'La seva clau' in code:
        return code[-6:]
    else:
        return ''


def expand_shadow_element(element):
  shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
  return shadow_root


def choose_demanar_cita():
    root1 = driver.find_element_by_tag_name('vaccinapp-app')
    shadow_root1 = expand_shadow_element(root1)
    
    root2 = shadow_root1.find_element_by_css_selector('uxl-content-switcher')
    shadow_root2 = expand_shadow_element(root2)
    
    root3 = root2.find_element_by_css_selector('vaccinapp-shell')
    shadow_root3 = expand_shadow_element(root3)
    
    root4 = shadow_root3.find_element_by_tag_name('uxl-content-switcher')
    shadow_root4 = expand_shadow_element(root4)
    
    root5 = root4.find_element_by_tag_name('appointment-shell')
    shadow_root5 = expand_shadow_element(root5)
    
    root6 = shadow_root5.find_element_by_tag_name('uxl-content-switcher')
    shadow_root6 = expand_shadow_element(root6)
    
    root7 = root6.find_element_by_tag_name('appointment-onboarding')
    shadow_root7 = expand_shadow_element(root7)
    
    root8 = shadow_root7.find_element_by_tag_name('mwc-button')
    shadow_root8 = expand_shadow_element(root8)
    
    demana_cita_page_click = shadow_root8.find_element_by_tag_name('button').click()


def fill_login_form():
    # User login form
    root1 = driver.find_element_by_tag_name('vaccinapp-app')
    shadow_root1 = expand_shadow_element(root1)
    
    root2 = shadow_root1.find_element_by_css_selector('uxl-content-switcher')
    shadow_root2 = expand_shadow_element(root2)
    
    root3 = root2.find_element_by_css_selector('vaccinapp-shell')
    shadow_root3 = expand_shadow_element(root3)
    
    root4 = shadow_root3.find_element_by_tag_name('uxl-content-switcher')
    shadow_root4 = expand_shadow_element(root4)
    
    root5 = root4.find_element_by_tag_name('appointment-shell')
    shadow_root5 = expand_shadow_element(root5)
    
    root6 = shadow_root5.find_element_by_tag_name('uxl-content-switcher')
    shadow_root6 = expand_shadow_element(root6)
    
    root7 = root6.find_element_by_tag_name('appointment-user-registration')
    shadow_root7 = expand_shadow_element(root7)
    
    root8 = shadow_root7.find_element_by_css_selector('#accept-btn')
    shadow_root8 = expand_shadow_element(root8)
    
    if cip == None:
        shadow_root7.find_element_by_tag_name('mwc-tab-bar').find_element_by_css_selector('#mdc-tab-2').click()
        shadow_root7.find_element_by_css_selector('#documentID').value = dni
        #shadow_root7.find_element_by_css_selector('#cip').remove()
    else:
        shadow_root7.find_element_by_tag_name('mwc-tab-bar').find_element_by_css_selector('#mdc-tab-1').click()
        shadow_root7.find_element_by_css_selector('#cip').send_keys(cip)
        #shadow_root7.find_element_by_css_selector('#documentID').remove()
        
    shadow_root7.find_element_by_css_selector('#phone').send_keys(phone)
    shadow_root7.find_element_by_css_selector('#name').send_keys(name)
    shadow_root7.find_element_by_css_selector('#surname').send_keys(surname)
    shadow_root7.find_element_by_css_selector('#surname2').send_keys(surname2)
    shadow_root7.find_element_by_css_selector('#mail').send_keys(mail)
    
    shadow_root8.find_element_by_tag_name('button').send_keys(Keys.NULL)
    acceptar_page_click = shadow_root8.find_element_by_tag_name('button').click()


def fill_sms_code():
    root1 = driver.find_element_by_tag_name('vaccinapp-app')
    shadow_root1 = expand_shadow_element(root1)
    
    root2 = shadow_root1.find_element_by_css_selector('uxl-content-switcher')
    shadow_root2 = expand_shadow_element(root2)
    
    root3 = root2.find_element_by_css_selector('vaccinapp-shell')
    shadow_root3 = expand_shadow_element(root3)
    
    root4 = shadow_root3.find_element_by_tag_name('uxl-content-switcher')
    shadow_root4 = expand_shadow_element(root4)
    
    root5 = root4.find_element_by_tag_name('appointment-shell')
    shadow_root5 = expand_shadow_element(root5)
    
    root6 = shadow_root5.find_element_by_tag_name('uxl-content-switcher')
    shadow_root6 = expand_shadow_element(root6)
    
    root7 = root6.find_element_by_tag_name('appointment-sms-code')
    shadow_root7 = expand_shadow_element(root7)
    
    # Enter SMS code
    shadow_root7.find_element_by_css_selector('#code').send_keys(code)
    
    # Click accept
    root8 = shadow_root7.find_element_by_css_selector('#accept-btn')
    shadow_root8 = expand_shadow_element(root8)
    shadow_root8.find_element_by_tag_name('button').send_keys(Keys.NULL)
    acceptar_page_click = shadow_root8.find_element_by_tag_name('button').click()


def choose_consultar_centre_massiu():
    root1 = driver.find_element_by_tag_name('vaccinapp-app')
    shadow_root1 = expand_shadow_element(root1)
    
    root2 = shadow_root1.find_element_by_css_selector('uxl-content-switcher')
    shadow_root2 = expand_shadow_element(root2)
    
    root3 = root2.find_element_by_css_selector('vaccinapp-shell')
    shadow_root3 = expand_shadow_element(root3)
    
    root4 = shadow_root3.find_element_by_tag_name('uxl-content-switcher')
    shadow_root4 = expand_shadow_element(root4)
    
    root5 = root4.find_element_by_tag_name('appointment-shell')
    shadow_root5 = expand_shadow_element(root5)
    
    root6 = shadow_root5.find_element_by_tag_name('uxl-content-switcher')
    shadow_root6 = expand_shadow_element(root6)
    
    root7 = root6.find_element_by_tag_name('appointment-welcome')
    shadow_root7 = expand_shadow_element(root7)

    acceptar_centre_massiu = shadow_root7.find_elements_by_css_selector('#make-appointment-btn')[1].click()


def get_available_locations():
    root1 = driver.find_element_by_tag_name('vaccinapp-app')
    shadow_root1 = expand_shadow_element(root1)
    
    root2 = shadow_root1.find_element_by_css_selector('uxl-content-switcher')
    shadow_root2 = expand_shadow_element(root2)
    
    root3 = root2.find_element_by_css_selector('vaccinapp-shell')
    shadow_root3 = expand_shadow_element(root3)
    
    root4 = shadow_root3.find_element_by_tag_name('uxl-content-switcher')
    shadow_root4 = expand_shadow_element(root4)
    
    root5 = root4.find_element_by_tag_name('appointment-shell')
    shadow_root5 = expand_shadow_element(root5)
    
    root6 = shadow_root5.find_element_by_tag_name('uxl-content-switcher')
    shadow_root6 = expand_shadow_element(root6)
    
    root7 = root6.find_element_by_tag_name('appointment-selection')
    shadow_root7 = expand_shadow_element(root7)

    root8 = shadow_root7.find_element_by_tag_name('appointment-center-selection')
    shadow_root8 = expand_shadow_element(root8)

    root9 = shadow_root8.find_element_by_tag_name('mwc-select')
    shadow_root9 = expand_shadow_element(root9)

    locations = []
    root9.click()
    time.sleep(2)
    for item in root9.find_elements_by_tag_name('mwc-list-item'):
        locations.append(item.text)
    return locations


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://vacunacovid.catsalut.gencat.cat")
    assert "Cita Prèvia" in driver.title

    # Choose "demanar cita"
    choose_demanar_cita()

    # Fill login form
    fill_login_form()

    # Wait for SMS code
    time.sleep(15)
    # Read SMS from email
    code = read_catsalut_verification_code()
    if code == '':
        sys.exit(1)
    print(code)
    fill_sms_code()

    # Choose "Consultar centre massiu"
    time.sleep(3)
    choose_consultar_centre_massiu()

    # Get available places
    time.sleep(3)
    locations = get_available_locations()
    if len(locations) > 0:
        for location in locations:
            print(location)
        # Notify if we see "Barcelona"
    else:
        print('0 llocs')

    # Close browser
    driver.close()


