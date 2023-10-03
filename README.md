KemzApp
-----

![Kemzapp](https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.wired.com%2Fphotos%2F5926df59f3e2356fd800ab80%2Fmaster%2Fw_2560%252Cc_limit%2FGettyImages-543338600-S2.jpg&tbnid=grpBeTmdiRpyRM&vet=12ahUKEwiZ9rDg69qBAxVUmicCHb2TBTcQMygIegQIARB-..i&imgrefurl=https%3A%2F%2Fwww.wired.com%2F2016%2F07%2Fneuroscientists-still-dont-know-music-sounds-good%2F&docid=133w6XwuQ4kZMM&w=2400&h=1800&q=music&ved=2ahUKEwiZ9rDg69qBAxVUmicCHb2TBTcQMygIegQIARB-)

## Introduction

KemzApp is a musical venue and artist booking site that facilitates the discovery and bookings of shows between local performing artists and venues in Ghana. This site lets you list new artists and venues, discover them, and list shows with artists as a venue owner. The app will do the following:

* creating new venues, artists, and creating new shows.
* searching for venues and artists.
* learning more about a specific artist or venue.


## Tech Stack (Dependencies)

### 1. Backend Dependencies
Our tech stack will include the following:
 * **virtualenv** as a tool to create isolated Python environments
 * **SQLAlchemy ORM** to be our ORM library of choice
 * **SQLite** as our database of choice
 * **Python3** and **Flask** as our server language and server framework
 * **Flask-Migrate** for creating and running schema migrations
You can download and install the dependencies mentioned above using `pip` as:
```
pip install virtualenv
pip install SQLAlchemy
pip install Flask
pip install Flask-Migrate
```
> **Note** - If we do not mention the specific version of a package, then the default latest stable package will be installed. 

### 2. Frontend Dependencies
HTML
CSS
Javascript
Node.js
Bootstrap 3


3. **Initialize and activate a virtualenv using:**
```
python -m virtualenv env
source env/bin/activate
```
>**Note** - In Windows, the `env` does not have a `bin` directory. Therefore, you'd use the analogous command shown below:
```
source env/Scripts/activate
```

4. **Install the dependencies:**
```
pip install -r requirements.txt
```

5. **Run the development server:**
```
export FLASK_APP=myapp
export FLASK_ENV=development # enables debug mode
python3 app.py
```

6. **Verify on the Browser**<br>
Navigate to project homepage [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://localhost:5000](http://localhost:5000) 

