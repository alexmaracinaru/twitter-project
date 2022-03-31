from bottle import get, redirect, request, view

##############################


@get("/login")
@view("login")
def _():
    return
