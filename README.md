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