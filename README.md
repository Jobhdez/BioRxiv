# bioRxiv-web
A web app that lists 100 or so research papers, with pagination, from BioRxiv. It includes a REST API that allows you to access the data and post new research papers.

Here is a link to [BioRxiv](https://www.biorxiv.org/) and here is a link to its [api](https://api.biorxiv.org/).

## Why does this web app exist?
Learning exercise

## what does it do?
Features:
* Use of an external api to seed the database
* Pagination
* REST API

## Requirements
Django: `pip install django`

Rest Framework: `pip install djangorestframework`

## Using the web app

Clone the repo: `git clone https://github.com/Jobhdez/BioRxiv.git`

run: `python3 manage.py runserver`

point your browser to: `http://127.0.0.1:8000/bioarxiv/` 

also point to: `https://127.0.0.1:8000/api`

## License 
MIT License
