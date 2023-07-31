# Ads Parsing App - app for getting ads from list.am service (the largest Armenian ads platform)
Backend prototype created with Python and MSAL library

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project was created for purposes of finding cheap apartments in Armenia after the property market became super expensive (end of 2022).
This app could parse flats' ads, get their main properties and record it to the database for searching the best option.

## Technologies
Project is created with:
* Python version: 3.10.11
* BeautifulSoup library version: 4.11.1
* Cloudscraper library version:: 1.2.65
* Peewee library version: 3.15.4

## Setup
For using this product you need to have:
* Python 3.10
* Installed database client software (PostreSQL)
* Installed libraries BeautifulSoup, Cloudscraper, Peewee

To run grabbing and processing data to database you just need to run main.py file in the root of repository.
This script will take every page with flat ads on list.am website and will send it to grabber module. Graber module will take properties from web page and will convert it to data transfer objects. After this converter will transfer this objects to the data access objects and will start recoding to database
