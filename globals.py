import datetime

USERS = [
    {
        "first_name": "Hard",
        "last_name": "Coded",
        "user_email": "hard@coded.com",
        "user_password": "pass",
        "user_id": "123123123131231231232131",
        "username": "hardcoded"
    },
    {
        "first_name": "John",
        "last_name": "Smith",
        "user_email": "john@email.com",
        "user_password": "cat",
        "user_id": "131231312321123123123123",
        "username": "thesquiggle"
    },
    {
        "first_name": "Alex",
        "last_name": "Maracinaru",
        "user_email": "alexandramaracinaru@gmail.com",
        "user_password": "asdf",
        "user_id": "123123123131231231232165",
        "username": "badget"
    },
]


time = datetime.datetime.now()

POSTS = [
    {
        "first_name": "Hard",
        "last_name": "Coded",
        "username": "hardcoded",
        "createdAt": time,
        "tweet": "This is a hardcoded tweet",
        "post_id": "1231578439201",
        "formattedCreatedAt": time.strftime("%H:%M %d-%m-%Y"),
    },
    {
        "first_name": "Hard",
        "last_name": "Wood",
        "username": "hardcoded",
        "createdAt": time,
        "tweet": "This is a teet",
        "post_id": "123157843920123",
        "formattedCreatedAt": time.strftime("%H:%M %d-%m-%Y"),
    }

]

SESSIONS = []

COOKIE_SECRET = "cookie secret"

REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'

TABS = [
    {"icon": "fas fa-home fa-fw", "title": "Home", "id": "home"},
    {"icon": "fas fa-hashtag fa-fw", "title": "Explore", "id": "explore"},
    {"icon": "far fa-bell fa-fw", "title": "Notifications", "id": "notifications"},
    {"icon": "far fa-envelope fa-fw", "title": "Messages", "id": "messages"},
    {"icon": "far fa-bookmark fa-fw", "title": "Bookmarks", "id": "bookmarks"},
    {"icon": "fas fa-clipboard-list fa-fw", "title": "Lists", "id": "lists"},
    {"icon": "far fa-user fa-fw", "title": "Profile", "id": "profile"},
    {"icon": "fas fa-ellipsis-h fa-fw", "title": "More", "id": "more"}
]


PEOPLE = [
    {"src": "stephie.png", "name": "Stephie Jensen", "handle": "@sjensen"},
    {"src": "monk.jpg", "name": "Adrian Monk", "handle": "@detective :)"},
    {"src": "kevin.jpg", "name": "Kevin Hart", "handle": "@miniRock"}
]

TRENDS = [
    {"category": "Music", "title": "We Won", "tweets_counter": "135K"},
    {"category": "Pop", "title": "Blue Ivy", "tweets_counter": "40k"},
    {"category": "Trending in US", "title": "Denim Day", "tweets_counter": "40k"},
    {"category": "News", "title": "Ukraine", "tweets_counter": "20k"},
    {"category": "Politics", "title": "Russia", "tweets_counter": "10k"},
    {"category": "Trending in US", "title": "Denim Day", "tweets_counter": "40k"},
    {"category": "Trending", "title": "Jesus", "tweets_counter": "10k"},
    {"category": "Music", "title": "We Won", "tweets_counter": "135K"},
    {"category": "Pop", "title": "Blue Ivy", "tweets_counter": "40k"},
    {"category": "Trending in US", "title": "Denim Day", "tweets_counter": "40k"},
    {"category": "News", "title": "Ukraine", "tweets_counter": "20k"},
    {"category": "Politics", "title": "Russia", "tweets_counter": "10k"},
    {"category": "Trending in US", "title": "Denim Day", "tweets_counter": "40k"},
    {"category": "Trending", "title": "Jesus", "tweets_counter": "10k"},
]

ITEMS = [
    {"img": "shapiro.jpg", "title": "Ben Shapiro", "user_name": "benshapiro"},
    {"img": "peterson.jpg", "title": "Jordan B. Peterson",
        "user_name": "jordanpeterson"},
    {"img": "babylonbee.jpg", "title": "Babylon Bee",
        "user_name": "babylonbee"},
]
