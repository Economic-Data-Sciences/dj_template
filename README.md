# dj_template
A Template for Django Projects

# Activate virtual environment
source ./bin/activate

# ensure ownership of folder
mkdir app
chown -R 1000:1000 app

# startup docker environment
docker compose up

# connect to docker environment
docker exec -it tmppy bash

# install node via nvm
nvm install v20.12.2
npm install from proj directory
chown -R 1001:1001 app/proj/node_modules/

### Project Setup
1. docker compose up
2. docker exec -it tmppy bash
    - cd app/proj
    - python manage.py migrate
    - python manage.py runserver 0.0.0.0:8000
3. mkdir app/proj/node_modules
    - sudo chown -R 1001:1001 app/proj/node_modules/
    - sudo chown 1001:1001 app/proj/package-lock.json
    - docker exec -it tmppy bash
    - cd app/proj
    - nvm install v20.12.2
    - npm install
4. sudo chown -R 1001:1001 app/proj/ui/styles/vendor/
    - docker exec -it tmppy bash
    - cd ui/styles/vendor/
    - tar -xzf uikit-3.15.21.tar.gz
    - cd /app/app/proj/
    - mkdir app/proj/ui/public/compiled
    - sudo chown -R 1001:1001 app/proj/ui/public/compiled/
    - npm run watch