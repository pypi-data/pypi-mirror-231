# Retraction Watch Database Importer
This Airflow script imports the Retraction Watch database into the annotations system of the Crossref Labs API.

![license](https://img.shields.io/gitlab/license/crossref/labs/retraction-watch-import) ![activity](https://img.shields.io/gitlab/last-commit/crossref/labs/retraction-watch-import)

![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white) ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Input Format
The script expects an S3 folder that contains CSV files with Retraction Watch data.

The CSV file should have the headings (with this capitalization):
* `DOI`
* `RetractionDOI`
* `Reason`
* `RetractionNature`
* `Notes`
* `URLS`

The first row of the CSV should be the headings. Multiple entries are possible (e.g. an expression of concern and a retraction), but only one type of each, for each DOI, will be imported. (I.e. you cannot have two retractions or two expressions of concern.)

## Idempotency
The script is idempotent. If you run it multiple times, it will only import new data and the results should be the same after multiple runs.

## Archiving
After processing a JSON input file, the script will move it to an archive folder in the same S3 bucket.

## Periodic Runs and Missing Input Files
The script is designed to be run periodically. If it does not find any input files, it will raise an exception. This is by design.

&copy; Crossref 2023