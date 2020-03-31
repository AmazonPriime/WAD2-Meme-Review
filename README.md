# Meme Review
<b>Repository for the WAD2 project for Group B in LB03.</b>

Live Website: [Meme Review - Python Anywhere](http://memereviews.pythonanywhere.com/)

```Meme Review will allow the user to browse or create memes. The user can create an account on the website by registering. Following a successful registration, the user can log in using their username and the password. After logging in the user can create memes; view/browse memes and rate them and write comments to them. Users under 18 will not be able to view age rated content. The user when creating a meme will give it a title, say whether or not it is NSFW (rated content) and which category it belongs in. The meme creator will allow a user to upload an image and put text at the top and bottom of the image with a selected font, size and outline. If the user is not logged in they can view memes (except for NSFW ones) but they cannot create or rate/comment on memes. To views memes the user will be able to select which category they'd like to use.```

#### Setting up Project
1. Clone or download the zip of the project from this repository
2. Make sure you have Python 3 installed, run `python` or `python3` in your CMD/Terminal
   * If you don't have it installed download and install from here: [python.org](https://www.python.org/)
3. Navigate to the directory via your CMD/Terminal using the `cd <path>` command
4. Create a virtual enviroment:
   * If you're not using Anaconda Navigator use `python[3] -m venv <name>`
   * For Anaconda Navigator use `conda create <name>`
5. Activate the virtual enviroment:
   * For Anaconda Navigator `conda activate <name>`
   * Windows non-anaconda venv `<name>/bin/activate.bat`
   * MacOS and Linux non-anaconda venv `source <name>/bin/activate`
6. Next install the requirements from the `requirements.txt` with `pip[3] install -r requirements.txt`
7. Now navigate to the `meme_review` directory where the `manage.py` is stored

#### Populating the Database
1. First make the migrations as they're not included in the repo `python[3] manage.py makemigrations`
2. Next, migrate the database `python[3] manage.py migrate`
3. Now the database is setup run the population script `python[3] populate.py`
4. Database is now populated with some default data

#### Start the website
* Simply use the command `python[3] manage.py runserver`

---

#### Dependencies (`requirements.txt`)
* asgiref v3.2.3
* [Django](https://www.djangoproject.com/) v3.0.3
* [Pillow](https://pillow.readthedocs.io/en/stable/) v7.0.0
* pytz v2019.3
* sqlparse v0.3.0

#### Sources
* [How to Create a Password Reset View](https://simpleisbetterthancomplex.com/tutorial/2016/09/19/how-to-create-password-reset-view.html)
#### Resources Used
* [Bootstrap](https://getbootstrap.com/)
* [Font Awesome](https://fontawesome.com/)
