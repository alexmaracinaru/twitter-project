from bottle import error, get, post, redirect, request, run, static_file, view

import globals
##############################
import index_get
import signup_get
import admin_get
import login_get
import files_get
import signup_ok_get
import posts_get
import edit_get
import logout_get
import profile_get
##############################
import login_post
import signup_post
import posts_post
import delete_post_post
import edit_post


##############################


@get("/app.css")
def _():
    return static_file("app.css", ".")


@get("/tailwind.css")
def _():
    return static_file("tailwind.css", ".")


@get("/validator.js")
def _():
    return static_file("validator.js", ".")


##############################
@error(404)
@view("404")
def _(error):
    print(error)
    return


run(host="127.0.0.1", port=3333, debug=True, reloader="True")
