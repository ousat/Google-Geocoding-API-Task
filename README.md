## Google GeoCoding API task

#### About
Django application, where an user can upload an excel file with addresses columns and using Google Geocoding API , the latitudes and longitudes are obtained and the download a new excel with latitude and longitude values

#### Run Instructions

- git clone

            git clone https://github.com/ousat/Google-Geocoding-API-Task.git
     
- create venv and activate 

            python3 -m virtualenv venv && source venv/bin/activate
    
- change directory to project root

            cd Google-Geocoding-API-Task

- install requirements

            pip3 install -r requirements.txt

- update GOOGLE_API_KEY on geoUpdater/google_api_config.py on line 4

    - to get API KEY , [click here] (https://developers.google.com/maps/documentation/geocoding/get-api-key?hl=en_US)

- runserver 

            python3 manage.py runserver

#### Additional Notes
- only takes xlsx files 
- was tested with python 3.6.9 on ubuntu 18.04
- works fine on Chrome and Firefox
- Things that can be improved: CSV support, optimisations

#### example 
- check test.xslx and output%%.xslx file in uploads folder


