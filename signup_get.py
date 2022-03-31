from bottle import get, redirect, request, view

##############################


@get("/signup")
@view("signup")
def _():
    return
