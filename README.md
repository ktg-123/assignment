# Finvid
Finvid is an application based on Django and Django rest framework that fetches latest videos of finance from youtube. It makes use of celery for the asynchronous fetching of videos and redis as the message broker to communicate between celery and django. It uses postgresql as database.   

Following are the prerequisite for running the application
- Postgresql
- Redis
- Python3
- Pip3

# Setup
- First create a virtual environment `python3 -m venv <name of virtual env>`
- Then enter into the environment using `source` command.
- Then run  `pip install -r requirements.txt` in the terminal.
- Then create `.env` file in the same folder containing the `.env.stencil` file. Copy the contents of stencil in the  `.env` file.
- Then go to https://console.cloud.google.com/ and create a developers account and create a project in it. Then after creation of project enable Youtube Data API v3.  You will get the api key after it. Type it in the `.env` file
- Then create a database in postgresql and enter similar name in `.env` , also enter the username and password for the postgresql.
- Enter a random secret key for the django project. 
- Now enter the project directory and run `python manage.py makemigrations`  and  `python manage.py migrate`.
- Now open 2 terminals and on one run the django server using `python manage.py runserver` while on the other run the celery worker using `celery -A assignment worker --beat -l info`
- Wait for sometime, the default time for fetching videos is 30 seconds, you can change it in `constants.py` if you want. Then visit the following url to see the list of videos. Since the response is paginated so you will also get the link for the previous and next page to browse more results.


![image](https://user-images.githubusercontent.com/58258464/210419857-f0b8af30-a5b3-4fb8-9471-a4ebd113e1ae.png)
