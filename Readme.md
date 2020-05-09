#### Install Python 3
`sudo apt-get install python3.6`

#### Install pip for managing dependencies
`sudo apt-get install python-pip`

#### Set up virtual Environment
`virtualenv -p python3 venv`

#### Activate Virtual Envirnoment
`source venv/bin/activate`

#### Apply The Database Schema
`python manage.py migrate`

#### create user
`python manage.py createsuperuser`

#### Start the server
`python manage.py runserver`

#### Run Unit tests
`python manage.py test`

#### Api endpoint's

##### All api requests can be made through  browser
`http://127.0.0.1:8000/api/`
`http://127.0.0.1:8000/api/fan/`
`http://127.0.0.1:8000/api/bulb/`

### Urls for portal


- Homepage `http://127.0.0.1:8000/`

- Login page - `http://127.0.0.1:8000/accounts/login/`

- Logout page - `http://127.0.0.1:8000/accounts/logout/`

#### DB Schema

- We have a base model called Device Which can be extended to create new types of devices.
- The tools used are Django framework for web portal, DRF for the API, Sqlite for Database, Django test runner for running tests
- We Use Djangos built in authentication system and api browser
- Unit tests cover all the CRUD tests
- Frontend templates use a `base.html` from which all other templates are extended.





  npm start
    Starts the development server.

  npm run build
    Bundles the app into static files for production.

  npm test
    Starts the test runner.

  npm run eject
    Removes this tool and copies build dependencies, configuration files
    and scripts into the app directory. If you do this, you can’t go back!

We suggest that you begin by typing:

  cd myfirstreact
  npm start

Happy hacking!




