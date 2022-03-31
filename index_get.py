from bottle import get, view


##############################
# The Home Page


@get("/index")
@view("index")
def _():
    return
