from find_forms import FindForms
import requests
from requests.models import Response
import os
import sys

def error_message_download_forms():
    print('\nPlease re-run "download_forms.py" and enter your request in the follwing format: \n"Form Number" minumum_year maximum_year\n\nFor example:\n"Form W-2" 1999 2004\n\nOr for only one year, enter the same year as both minimum and maximum values.\nFor example:\n"Form W-2" 1999 1999\n\n** Do not forget to use quotations around the form number, and that both minimum year and maximum year need to be four-digit integers.\nThe three arguments should each be separated by a space.\nCommas are optional and input is not case-sensitive.')


def click_link(form_number: str, download_name: str, r: Response):
    with open(f'{form_number}/{download_name}.pdf', 'wb') as f:
        f.write(r.content)

def download_forms(form_request: str, min_year: int, max_year: int):
    count = 0
    get_forms = FindForms(form_request)
    results = get_forms.get_forms()
    
    # Filtering results and downloading forms
    for result in results:
        form_number = (result["form_number"])
        year = int(result["year"])
        download_url = result["download_url"]
        download_file_name = result["download_file_name"]
        
        # Create directory and download forms
        if year >= min_year and year <= max_year:
            count += 1
            r = requests.get(download_url, allow_redirects=True)
            if not os.path.exists(form_number):
                os.mkdir(form_number)
                print(f"Directory {form_number} created.")
                click_link(form_number, download_file_name, r)
            else:
                click_link(form_number, download_file_name, r)  
        
    # Catch queries that have no results
    if count == 0:
        print(f'\nNo forms called "{form_request}" were found in that date range.\nNo forms downloaded.\n\nIf you think this is incorrect:')
        error_message_download_forms()
        
    #Print confirmation of downloads
    else:
        print(f'{count} forms downloaded to "{form_number}" directory.')


if __name__ == '__main__':
    try:
        # Check for correct number of arguments
        if len(sys.argv) == 4:
            
            # Populate paramters and remove unnecessary commas
            form_request = sys.argv[1].replace(",", "")
            min_year = sys.argv[2].replace(",", "")
            max_year = sys.argv[3].replace(",", "")
            
            # Swap years if out of order
            if max_year < min_year:
                max_year, min_year = min_year, max_year
                
            # Call main download function and catch bad "year" inputs
            if len(min_year) == 4 and len(max_year) == 4:
                download_forms(form_request, int(min_year), int(max_year))
                
            else:
                error_message_download_forms()
                
        else:
            error_message_download_forms()
            
    except:
        error_message_download_forms()
