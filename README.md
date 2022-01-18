# Find the Forms!

Hello and thank you for reading. This is a Python program (written in version 3.9.5) that fulfills two main purposes.

First, with `return_json.py`, you, the user, can provide a list of IRS form names and receive a package of information about each form in the list. Specifically, you will receive the form number, the form title, and the minimum and maximum years that the form is available for download. This information will be returned to you printed in the console in JSON format.

Second, with `download_forms.py`, you can specify a tax form and a range of years, and you will receive downloads for all the PDFs of that form available within that date range. These files will be downloaded into a subdirectory titled with the name of the form.

## Getting Started

### Dependencies

- python 3.9.5
- beautifulsoup4 4.10.0
- certifi 2021.10.8
- charset-normalizer 2.0.10
- idna 3.3
- lxml 4.7.1
- requests 2.27.1
- soupsieve 2.3.1
- urllib3 1.26.8

### Installing

Once you have the `Find_the_Forms` package in your preferred directory, navigate to `Find_the_Forms` in your terminal and run the following commands:

```
pipenv install
pipenv shell
```

### How to Run the Files

Once you've got your virtual environment running in the `Find_the_Forms` directory, simply run either `return_json.py` or `download_forms.py` via the command line, along with your input, like this:

```
python3 return_json.py "Form Name 1", "Form Name 2", "Form Name 3" ...

or

python3 download_forms.py "Form Name" minumum_year maximum_year
```

#### More on input formatting for `return_json.py`:

- Form names must be in quotations and separated by a space.
- Commas are optional.
- Input is not case-sensitive.

Like this:

`"Form Name 1", "Form Name 2", "Form Name 3" ...`

For example:

`python3 return_json.py "Form W-2", "Publ 1", "Form 990 (Schedule K)"`

#### More on input formatting for `download_forms.py`:

- Form names must be in quotations.
- Both minimum year and maximum year need to be four-digit integers.
- The form name and each year should be separated by a space.
- Commas are optional.
- Input is not case-sensitive.

Like this:

`"Form Name" minumum_year maximum_year`

For example:

`python3 download_forms.py "Form W-2" 1999 2004`

If you would only like to download one year, enter that year as both minimum and maximum values.
For example:

`python3 download_forms.py "Form W-2" 1999 1999`

## More Details

This project uses three python files:

- `return_json.py`
- `download_forms.py`
- `find_forms.py`

### `find_forms.py`

`find_forms.py` is a module that will be run internally by either `return_json.py` or `download_forms.py`.
It is responsible for:

- Reaching the IRS webpage
- Performing a search on the page
- Requesting HTML
- Retrieving the number of results
- Scraping search results (multiple pages when there is pagination involved)
- Parsing the search results
- Returning a nested list of items. Each item will be a single version of every form requested (one item per year) and will have the following information:
  - form number (form name)
  - form title
  - year
  - download url
  - name to be used for downloaded PDF file

### `return_json.py`

You can run `return_json.py` with a list of requested IRS form names, and for each form name in the list, you will receive the form number, the form title, and the minimum and maximum years that the form is available for download. These results will be printed as JSON to the console.
(Find more info on input-formatting in the "How to Run the Files" section above).

`return_json.py` is responsible for:

- Receiving user input via the command line.
- Handling errors resulting from bad user input.
- Calling and running `find_forms.py` to receive data based on user input.
- From that data, finding the minimum year and the maximum year for the requested form.
- Alerting the user if no results were found.
  - To help with user error, this function also reminds them of the proper formatting for their input and provides a link to the IRS website for reference.
- Formatting each successful data set into json and adding that to a final list of results.
- Printing the results as JSON to the console in the following format:

```
[
    {
        "form_number": "Form Name",
        "form_title": "Form Title",
        "min_year": ####,
        "max_year": ####
    },
    ...
]
```

### `download_forms.py`

You can run `download_forms.py` in the console with an IRS form name, a maximum year and a minimum year and receive downloads for all PDFs of that name within that date range. These PDF files will be named with this format: "Form Name - Year" and will be downloaded to the directory of the corresponding form name.
(Find more info on input-formatting in the "How to Run the Files" section above).

`download_forms.py` is responsible for:

- Receiving user input via the command line.
- Handling errors resulting from bad user input.
- Calling and running `find_forms.py` to receive data based on user input.
- Filtering results based on the requested minimum and maximum years.
- Alerting the user if no results were found.
  - To help with user error, this function also reminds them of the proper formatting for their input and provides a link to the IRS website for reference.
- Creating a directory with the name of the form that was requested.
- Downloading all PDFs of the requested form within the requested date range.
  - PDF files will be named with this format: "Form Name - Year"
  - They will be downloaded to the directory of the corresponding form name.


## Help

If you find that your requests are not returning the results you are anticipating:

- Double-check that your input formatting is as described above. Do not use any special characters such as "[]" or "{}" unless they are part of the form name.
- Double-check your spelling and make sure that you have typed the complete form name exactly as it is listed on the IRS site. For instance "Form W-2" will work, while "W-2" will not.
- If you are unsure, you can visit https://apps.irs.gov/app/picklist/list/priorFormPublication.html and perform a search there to find the exact version and name of the form you wish to request.

Thank you, hope you enjoy!

## Feedback

Thank you for having me along this far! I really enjoyed working on this challenge. It was a fun one. I liked its real-world context as well as how it utilized many different aspects of software development to solve a lot of little problems that worked toward a larger goal in the end. It was gratifying to see it through to the end. Thank you again!
