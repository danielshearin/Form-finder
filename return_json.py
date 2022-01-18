import json
from typing import List
from find_forms import FindForms
import sys


def error_message_json():
    """ Prints error message for return_json.py """

    print('\nPlease re-run "return_json.py" and enter your request in one of the follwing formats:\n\n"Form Number 1", "Form Number 2", "Form Number 3" ...\nor\n"Form Number 1" "Form Number 2" "Form Number 3" ...\n\nFor example:\n"Form W-2", "Publ 1", "Form 990 (Schedule K)"\n\n** Do not forget form numbers should be in quotations and separated by a space.\nCommas are optional and input is not case-sensitive.\n\nStill not getting what you expect? You can search here to make sure you are using the form name exactly as it is listed on the site:\nhttps://apps.irs.gov/app/picklist/list/priorFormPublication.html')


def return_json(form_list: List[str]):
    json_results = []
    no_results = []

    for form_request in form_list:
        form_request = form_request.replace(",", "")
        get_forms = FindForms(form_request)
        results = get_forms.get_forms()
        years = []

        # Populating list of years
        for result in results:
            form_name = result["form_name"]
            form_title = result["form_title"]
            year = result["year"]
            if form_request.lower() == form_name.lower():
                years.append(year)

        # Catch queries that have no results
        if len(years) == 0:
            no_results.append(form_request)

        # Save data to json file
        if len(years) > 0:
            min_year = min(years)
            max_year = max(years)
            json_results.append({
                "form_number": form_name,
                "form_title": form_title,
                "min_year": min_year,
                "max_year": max_year
            })

    final_json = (json.dumps(json_results, indent=4))
    if len(final_json) > 2:
        print(final_json)

    if len(no_results) != 0:
        print("\nNo results found for the following:")
        print(*no_results, sep=", ")
        print("\nIf you think this is incorrect:")
        error_message_json()


if __name__ == '__main__':
    input_list = sys.argv[1:]
    if len(input_list) > 0:
        return_json(input_list)
    else:
        error_message_json()
