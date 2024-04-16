# dj_template
A Template for Django Projects

## Context
This example project is focused on front-end development. It incorporates Docker and will also highlight common permissioning hurdles that sometimes arise.

This project streams random data with three potential states:
1. Positive
2. Negative
3. Volatile

Our goal is to build a simple dashboard which shows the current state, and also explains a little bit about our data.

This project is about more than just your skills, it is also about collaboration. So if some issues seem difficult and you have questions, please feel free to reach out and collaborate! It will also be important to comment within the code to make it easier to read and follow.

## The Task
We need to create a simple dashboard we should create:
1. A navbar
  - Our task is to do some simple styling here.
  - File location app/proj/exp_app/templates/layout/nav.html
2. A single page, which describes our data. This page may rely on underlying components, charts, etc.
  - Our task here is to create:
    - A description of the current state
    - A bar chart of simple metrics
    - A timeseries chart of streaming data
  - File location app/proj/exp_app/templates/index.html
    - This html file loads react javascript which is found in app/proj/ui/ and underlying folders


## The API
This project has 4 APIs which can help us complete our task.
1. An example api
  - http://localhost/api/example
2. Streaming data
  - This must be triggered to populate our database and create our data
  - http://localhost/api/stream
3. Simple metrics
  - Simple metrics about our data by state
  - http://localhost/api/get-metrics
4. Latest Record
  - http://localhost/api/get-latest


### Project Setup
This project setup has several steps because it relies on several components. If working on a linux system, it will be important to keep file permissions in mind. You can find your user id on linux with the command `id -u`

1. Clone the project
  - `git clone git@github.com:Economic-Data-Sciences/dj_template`
2. Activate the pythong virtual environment and setup IDE
  - `source bin/activate`
  - open the project with your favourite editor
3. Start Docker
  - `docker compose up`
4. Connect to docker environment
  - `docker exec -it tmppy bash`
    - The command above is for linux, in windows this can be run from powershell
  - Go to project folder within docker environment
    - `cd app/proj`
  - Migrate database
    - `python manage.py migrate`
  - Start backend server
    - `python manage.py runserver 0.0.0.0:8000`
5. Setup npm with permissions
  - open another terminal or powershell and go to the project root folder (not in the docker environment)
  - `mkdir app/proj/node_modules`
  - `mkdir app/proj/ui/public/compiled`
    - windows equivalent is to create a folder in file explorer
  - `sudo chown -R 1001:1001 app/proj/node_modules/`
    - chown commands are not needed in windows
  - `sudo chown 1001:1001 app/proj/package-lock.json`
  - `sudo chown -R 1001:1001 app/proj/ui/styles/vendor/`
  - `sudo chown -R 1001:1001 app/proj/ui/public/compiled/`
  - Enter docker environment
    `docker exec -it tmppy bash`
    - `cd app/proj`
    - `nvm install v20.12.2`
    - `npm install`
    - `cd ui/styles/vendor/`
    - `tar -xzf uikit-3.15.21.tar.gz`
    - `cd /app/app/proj/`
    - `npm run watch`
    
    
    
    
    
    