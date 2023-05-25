import csv,time
from selenium import webdriver


import template_scripts
link_list_ = []
final_list = []

#to get the link for the pending universities where scripts are not present
def get_link(csv_file: str):
    """
    Reads and prints a csv file to console
    :param csv_file: The csv file location to be printed
    :return: list of the current instituion and links
    """
    with open(csv_file, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # list of the elements of the .py files
                school_info = (row['\ufeffSchools'], row['Links'],row['Country'])
                link_list_.append(school_info)
    return link_list_


# to check for page source
def check_driver(link_list):
    """
    :param current_list: to get the list of schools and link
    :param final_list: to get the final list with portals
    :param portal: directly based on the name of the template after detection from driver
    :return: None
    """
    driver = webdriver.Chrome()
    current_list = link_list

    for school in current_list:
        current_url = school[1]
        driver.get(url=current_url)
        script_name = school[0].lower().replace(' ', '_')+'.py'
        print(school[0])
        time.sleep(2)
        if 'Use of this software is limited to Ellucian licensees, ' in driver.page_source:
            time.sleep(2)
            portal = 'ellucian'
        elif 'Sign-in options' in driver.page_source:
            time.sleep(2)
            portal = 'microsoft'
        elif '  Powered by Jenzabar' in driver.page_source:
            time.sleep(2)
            portal = 'ics_both'
        elif 'ctcLink - Sign In' in driver.page_source:
            time.sleep(2)
            portal = 'ctc_link'
        elif 'Keep me signed in' in driver.page_source:
            time.sleep(2)
            portal = 'adfs'
        elif 'Okta' in driver.page_source:
            time.sleep(2)
            portal = 'okta'
        elif 'PowerCampus® Self-service' in driver.page_source:
            time.sleep(2)
            portal = 'two_parter'
        else:
            time.sleep(2)
            portal = 'basic'
        final_dict = {'school_name':school[0],'script_name':script_name,'country':school[2],'portal':portal,'link':school[1]}
        final_list.append(final_dict)
    return final_list

# to check for page source
def write_login_function(final_list) :
    """
           Write the login script to the new file as per country code
           """
    for school in final_list:
            print(school)
            portal_name = school['portal'] + '.py'
            script_name = school['script_name']
            current_country = school['country']
            current_url = school['link']
            with open(f'template_scripts\\{portal_name}', 'r') as f:
                portal_file=f.read()
            script_file = portal_file.replace('URL_PLACE_HOLDER', current_url)
            with open(f'login_scripts\\{current_country}\\{script_name}', 'w') as f:
                f.write(script_file)

