import datetime
from bottle import request

DB_PATH = "./database.sqlite"

USERS = [
    {
        "first_name": "Hard",
        "last_name": "Coded",
        "user_email": "hard@coded.com",
        "user_password": "pass",
        "user_id": "123123123131231231232131",
        "username": "hardcoded",
        "card_post": "My grandmother started walking five miles a day when she was sixty. She's ninety-seven now, and we don't know where the hell she is. My grandmother started walking five miles a day when she was sixty. She's ninety-seven now, and we don't know where the hell she is. My grandmother started walking."
    },
    {
        "first_name": "John",
        "last_name": "Smith",
        "user_email": "john@email.com",
        "user_password": "cat",
        "user_id": "131231312321123123123123",
        "username": "thesquiggle",
        "card_post": "This is the text that comes from the second user."
    },
    {
        "first_name": "Alex",
        "last_name": "Maracinaru",
        "user_email": "alexandramaracinaru@gmail.com",
        "user_password": "asdf",
        "user_id": "123123123131231231232165",
        "username": "badget",
        "card_post": "This is the text that comes from the  third user."
    },
    {
        "first_name": "Alex",
        "last_name": "Maracinaru",
        "user_email": "alexandramaracinaru@gmail.com",
        "user_password": "asdf",
        "user_id": "123123123131231231232165",
        "username": "badget",
        "card_post": "This is the text that comes from the  third user."
    },
]


time = datetime.datetime.now()

POSTS = [
    {
        "first_name": "Hard",
        "last_name": "Coded",
        "username": "hardcoded",
        "created_at": time,
        "tweet": "This is a hardcoded tweet",
        "post_id": "1231578439201",
        "formattedCreatedAt": time.strftime("%H:%M %d-%m-%Y"),
    },
    {
        "first_name": "Hard",
        "last_name": "Wood",
        "username": "hardcoded",
        "created_at": time,
        "tweet": "This is a teet",
        "post_id": "123157843920123",
        "formattedCreatedAt": time.strftime("%H:%M %d-%m-%Y"),
    }

]

SESSIONS = []

COOKIE_SECRET = "cookie secret"

REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'

TABS = [
    {"icon": "ri-home-line", "title": "Home", "id": "home"},
    {"icon": "ri-hashtag", "title": "Explore", "id": "explore"},
    {"icon": "ri-notification-line", "title": "Notifications", "id": "notifications"},
    {"icon": "ri-message-3-line", "title": "Messages", "id": "messages"},
    {"icon": "ri-bookmark-line", "title": "Bookmarks", "id": "bookmarks"},
    {"icon": "ri-file-list-2-line", "title": "Lists", "id": "lists"},
    {"icon": "ri-user-5-line", "title": "Profile", "id": "profile"},
    {"icon": "ri-more-line", "title": "More", "id": "more"}
]


TRENDS = [
    {"category": "Trending in Denmark", "title": "Lost", "tweets_counter": "135K"},
    {"category": "Trending in US", "title": "Denim Day", "tweets_counter": "40k"},
    {"category": "Sports", "title": "Hamilton", "tweets_counter": "120k"},
    {"category": "Always Trending", "title": "Jesus", "tweets_counter": "1m"},
]

ITEMS = [
    {"img": "shapiro.jpg", "title": "Ben Shapiro", "user_name": "benshapiro"},
    {"img": "peterson.jpg", "title": "Jordan B. Peterson",
        "user_name": "jordanpeterson"},
    {"img": "babylonbee.jpg", "title": "Babylon Bee",
        "user_name": "babylonbee"},
]


def create_json_from_sqlite_result(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def check_session():
    user_session_id = request.get_cookie("uuid4")
    # compare the uuid from the cookie to the uuid from the sessions

    for session in SESSIONS:
        if session["session_id"] == user_session_id:
            return session

    return None
