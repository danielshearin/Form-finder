from bs4 import BeautifulSoup
from typing import List, Dict
import requests
from urllib.parse import quote
import re
import math


class FindForms:

    def __init__(self, form_request: str):
        self.form_request = form_request

    def request_html(self, index_of_first_row: int, form_request: str) -> BeautifulSoup:
        """
        Makes initial HTML request to webpage and retrieves data.
        """

        html_text = requests.get(
            f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow={index_of_first_row}&sortColumn=sortOrder&value={quote(form_request)}&criteria=formNumber&resultsPerPage=200&isDescending=false').text
        soup = BeautifulSoup(html_text, 'lxml')
        return soup


    def get_forms(self) -> List[Dict]:
        """
        THIS NEEDS TO BE COMPLETED
        """
        results = []
        soup = self.request_html(0, self.form_request)
        
        # Pagination
        try:
            result_number_str = soup.find('th', class_="ShowByColumn").text.strip()[-12:-5].replace(',', '')
            result_num = int(re.findall('[0-9]+', result_number_str)[0])
            num_of_pages = math.ceil(result_num / 200)
            
            for i in range(num_of_pages):
                index_of_first_row = (i - 1) * 200
                soup = self.request_html(index_of_first_row, self.form_request)
                lines_even = soup.find_all('tr', class_="even")
                lines_odd = soup.find_all('tr', class_="odd")
                lines = lines_even + lines_odd

                # Parse search results
                for line in lines:
                    form_number = line.find('td', class_="LeftCellSpacer").text.strip()
                    if self.form_request.lower() == form_number.lower():
                        download_url = line.find('a').attrs['href']
                        form_title = line.find('td', class_="MiddleCellSpacer").text.strip()
                        year = line.find('td', class_="EndCellSpacer").text.strip()
                        download_file_name = form_number + ' - ' + year
                        results.append({
                            "form_number": form_number,
                            "form_title": form_title,
                            "year": year,
                            "download_url": download_url,
                            "download_file_name": download_file_name
                        })

                return results

        except:
            return results