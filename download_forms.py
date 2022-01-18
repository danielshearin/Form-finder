from find_forms import FindForms
from typing import List
import requests
from requests.models import Response
import os
import sys


def error_message_download_forms():
    """ Function to print error message for download_forms.py """

    print('\nPlease re-run "download_forms.py" and enter your request in the follwing format: \n"Form Name" minumum_year maximum_year\n\nFor example:\n"Form W-2" 1999 2004\n\nIf you would only like to download one year, enter that year as both the minimum and maximum values.\nFor example:\n"Form W-2" 1999 1999\n\n** Do not forget to use quotations around the form name, and that both minimum year and maximum year need to be four-digit integers.\nThe three arguments should each be separated by a space.\nCommas are optional and input is not case-sensitive.\n\nStill not getting what you want? You can search here to make sure you are using the form name exactly as it is listed on the site:\nhttps://apps.irs.gov/app/picklist/list/priorFormPublication.html')


def click_link(form_name: str, download_name: str, r: Response):
    """
    Function to open download link on website and download PDF to corresponding folder.

    Parameters:
        form_name (str): The name of the form to be downloaded.
        download_name (str): What the downloaded file will be named.
        r (request.models.Reponse): The server's response to our "open" request.
    """
    with open(f'{form_name}/{download_name}.pdf', 'wb') as f:
        f.write(r.content)


def download_forms(form_request: str, min_year: int, max_year: int):
    """
    Function to get forms from server, filter them based on parameters, and download them.

    Parameters:
        form_request (str): The name of the form requested by the user.
        min_year (int): The minimum year requested by the user.
        max_year (int): The maximum year requested by the user.
    """
    count = 0
    get_forms = FindForms(form_request)
    results = get_forms.get_forms()

    # Filter results, create directory and download forms
    for result in results:
        form_name = (result["form_name"])
        year = int(result["year"])
        download_url = result["download_url"]
        download_file_name = result["download_file_name"]

        if year >= min_year and year <= max_year:
            count += 1
            r = requests.get(download_url, allow_redirects=True)
            if not os.path.exists(form_name):
                os.mkdir(form_name)
                print(f"Directory {form_name} created.")
                click_link(form_name, download_file_name, r)
            else:
                click_link(form_name, download_file_name, r)

    # Catch queries that have no results
    if count == 0:
        print(
            f'\nNo forms named "{form_request}" were found in that date range.\nNo forms downloaded.\n\nIf you think this is incorrect:')
        error_message_download_forms()

    # Print confirmation of downloads
    else:
        print(f'{count} forms downloaded to "{form_name}" directory.')


def check_input_call_download(user_input: List):
    """
    Function to check for the proper format of user input, then to catch errors or call a function to download forms.

    Parameters:
        user_input (List): The input entered by the user in the command line.
    """

    # Check for correct number of arguments
    if len(user_input) == 4:

        # Define paramters and remove unnecessary commas
        form_request = user_input[1].replace(",", "")
        min_year = user_input[2].replace(",", "")
        max_year = user_input[3].replace(",", "")

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


if __name__ == '__main__':
    try:
        check_input_call_download(sys.argv)
    except:
        error_message_download_forms()
