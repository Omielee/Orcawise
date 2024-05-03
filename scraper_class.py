import os

import pandas as pd
from driver import *


class LinkedinScraper:

    def __init__(self, file_name):
        self.file_name = file_name

    def load_config(self):
        # Load MySQL credentials from YAML config file
        return pd.read_csv(self.file_name, usecols=['Name of company'])

    def scrap_company_details(self, output_file, threshold):
        data = self.load_config()
        company_details = []
        count = 0
        try:
            existing_companies = pd.read_csv(output_file)['Company']
            # print(existing_companies)
            for company in data['Name of company']:
                if company not in existing_companies.values:
                    try:
                        # Navigate to LinkedIn and search for company
                        # Assuming the driver is already initialized
                        driver.get(f"https://www.linkedin.com/company/{company}")
                        time.sleep(10)  # Add a wait to let the page load

                        # Click on the "About" button
                        about_btn = '//*[@id[starts-with(., "ember")]]/nav/ul/li[2]'
                        about_btn_click = driver.find_element(By.XPATH, about_btn)
                        about_btn_click.click()
                        time.sleep(5)

                        # Extract and print the company overview
                        text_obj = driver.find_element(By.XPATH,
                                                    '//*[@class="artdeco-card org-page-details-module__card-spacing artdeco-card org-about-module__margin-bottom"]')
                        text = text_obj.text
                        company_details.append({'Company': company, 'About Company': text})

                        print("Company: ", company, "\n About:", text)
                        count+=1
                        print(f"please show me the count::::{count}")
                        if count == threshold:
                            break

                    except Exception as e:
                        print(
                            "--------------------------------------------------------------------------------------------------------------- \n")
                        print(f"Error scraping {company}: {e} \n ")
                        company_details.append({'Company': company, 'About Company': "No data found on linkedln"})
                        print(
                            "--------------------------------------------------------------------------------------------------------------- \n")
        except Exception as e:
            for company in data['Name of company']:
                try:
                    # Navigate to LinkedIn and search for company
                    # Assuming the driver is already initialized
                    driver.get(f"https://www.linkedin.com/company/{company}")
                    time.sleep(10)  # Add a wait to let the page load

                    # Click on the "About" button
                    about_btn = '//*[@id[starts-with(., "ember")]]/nav/ul/li[2]'
                    about_btn_click = driver.find_element(By.XPATH, about_btn)
                    about_btn_click.click()
                    time.sleep(5)

                    # Extract and print the company overview
                    text_obj = driver.find_element(By.XPATH,
                                                   '//*[@class="artdeco-card org-page-details-module__card-spacing artdeco-card org-about-module__margin-bottom"]')
                    text = text_obj.text
                    company_details.append({'Company': company, 'About Company': text})
                    print("Company: ", company, "\n About:", text)
                    count += 1
                    if count == threshold:
                        break

                except Exception as e:
                        #Search the company using the pattern of URL given by LinkedIn passing the name of the company as a keyword
                        driver.get(f"https://www.linkedin.com/search/results/companies/?keywords={company}")
                        time.sleep(10)
                        #Get the quantity of results pages and check if this number is greater than zero
                        result_search= driver.find_element(By.XPATH, '//*[@class[starts-with(.,"pb2 t-black--light t-14")]]')
                        result = result_search.find_element(By.TAG_NAME,'div')
                        qt_result = result.text().split(' ')[0]
                        if(int(qt_result) >=1):
                            #Getting the first link of the results page
                            link_result = driver.find_element(By.XPATH, '//*[@class[starts-with(.,"entity-result__title-text")]]')
                            link_company = link_result.find_element(By.CLASS_NAME, "app-aware-link")
                            link_company.click()
                            time.sleep(5)
                            about_btn = '//*[@id[starts-with(., "ember")]]/nav/ul/li[2]'
                            about_btn_click = driver.find_element(By.XPATH, about_btn)
                            about_btn_click.click()
                            time.sleep(5)

                            # Extract and print the company overview
                            text_obj = driver.find_element(By.XPATH,
                                                        '//*[@class="artdeco-card org-page-details-module__card-spacing artdeco-card org-about-module__margin-bottom"]')
                            text = text_obj.text
                            company_details.append({'Company': company, 'About Company': text})
                            print("Company: ", company, "\n About:", text)
                            count += 1
                            if count == threshold:
                                break
                        else:                                                
                            print(
                                "--------------------------------------------------------------------------------------------------------------- \n")
                            print(f"Error scraping {company}: {e} \n ")
                            company_details.append({'Company': company, 'About Company': "No data found on linkedln"})
                            print(
                                "--------------------------------------------------------------------------------------------------------------- \n")





        company_details_df = pd.DataFrame(company_details)
        if os.path.isfile(output_file):
            company_details_df.to_csv('company_data.csv', index=False, mode='a', header=False)
        else:
            company_details_df.to_csv('company_data.csv', index=False)

        return company_details_df


threshold = int(input("Please enter the number in integer for companies to scrap like if you 1 i.e one company is scraped:::"))

class_obj = LinkedinScraper("companies-data2.csv")
output_file_path = os.getcwd()
output_file = os.path.join(output_file_path, 'company_data.csv')

companies = class_obj.scrap_company_details(output_file, threshold)
print("Work is over and hence quitting the task::::")
driver.quit()
