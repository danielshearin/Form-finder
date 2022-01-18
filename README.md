# Find the forms!

This project achieves two main purposes.

First, with `return_json.py`, you can input a list of IRS form names and receive information about that form. Specifically, they wil receive the form number, the form title, and the minimum and maximum years that the form is available for download. This information will be returned as json.

Second, with `download_forms.py` you can specify a tax form name and a list of years, and receive downloads for all PDFs of that name within that date range. These files will be downloaded into a subdirectory titled with the name of the form.

## Description

This project is built with Python 3.9.5 and uses three python modules:
* return_json.py
* download_forms.py
* find_forms.py

`find_forms.py` will be run by either `return_json.py` or `download_forms.py`. 
This file is responsible for:
* Getting the IRS wepbage
* Performing a search
* Requesting HTML
* Retrieving a number of results
* Scraping all pages of search results (paginating when there are multiple pages)
* Parsing the search results
* Returning a nested list of items:
    * each item in the list will have the following information for each form requested:
        * form number
        * form title
        * year
        * download url
        * name to be used for downloaded file 
            
            
You, the user, can run `return_json.py` with a list of IRS form names and you will receive information about each form.

This file is responsible for:
* Receiving user input via the command line
* Handling errors resulting from bad user input
* Calling and running "find_forms.py" to receive data based on user input.
* From that data, finding the minimum year and the maximum year for the requested form.
* Alerting the user if no results were found. 
    * In case the user believes they should have received results, this function also reminds the user of the proper formatting for their input (in case of user error).
* Formatting each successful data set to json and adding that to a final list of results.
* Printing the results to the console in the following format:
    
            [
                    {
                        "form_number": "Form Number",
                        "form_title": "Form Title",
                        "min_year": ####,
                        "max_year": ####
                    },
                    ... 
            ]


You, the user, can run `download_forms.py` with a IRS form name, a maximum year and a minimum year and receive downloads for all PDFs of that name within that date range.

This file is responsible for:
* Receiving user input via the command line
* Handling errors resulting from bad user input
* Calling and running "find_forms.py" to receive data based on user input.
* Filtering results based on minimum and maximum years.
* Alerting the user if no results were found. 
    *  In case the user believes they should have received results, this function also reminds the user of the proper formatting for their input (to help with user error).
* Creating a directory with the name of the form that was requested
* Downloading all PDFs of the requested form within the requested date range.
    * PDF files will be named with this format: "Form Name - Year"
    * Downloaded to the directory with the cooresponding form name.



## Getting Started

### Dependencies

* python 3.9.5
* beautifulsoup4 4.10.0
* certifi 2021.10.8
* charset-normalizer 2.0.10
* idna 3.3
* lxml 4.7.1
* requests 2.27.1
* soupsieve 2.3.1
* urllib3 1.26.8

### Installing

Once downloading the package. You can unzip it in your directory of choice. Then run the following commands.

Find_the_forms
* pipenv install
* pipenv shell


### Executing program

To run the program, you will run either `return_json.py` or `download_forms.py` via the command line.

`$ python3 return_json.py <input>`
or
`$ python3 download_forms.py <input>`

Your input should be in the following formats.

For `return_json.py`:

`"Form Number 1", "Form Number 2", "Form Number 3" ...`
or
`"Form Number 1" "Form Number 2" "Form Number 3" ...`

For example:
`python3 return_json.py "Form W-2", "Publ 1", "Form 990 (Schedule K)"`

Form numbers must be in quotations and separated by a space.
Commas are optional.
Input is not case-sensitive.


For `download_forms.py`:

`"Form Number" minumum_year maximum_year`

For example:
`"Form W-2" 1999 2004`

If you would only like to download one year, enter that year as both minimum and maximum values.
For example:
`"Form W-2" 1999 1999`

Form numbers must be in quotations.
Both minimum year and maximum year need to be four-digit integers.
The form name and the two years should each be separated by a space.
Commas are optional.
Input is not case-sensitive.


## Help

Any advise for common problems or issues.


## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)


## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

