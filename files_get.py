##############################
# All the images and the logo


from bottle import get, redirect, run, static_file, view


@get("/Ellipse20.png")
def _():
    return static_file("images/Ellipse20.png", ".")


@get("/3dhexagon.svg")
def _():
    return static_file("images/3dhexagon.svg", ".")


@get("/profilepic.svg")
def _():
    return static_file("images/profilepic.svg", ".")


@get("/ppic.svg")
def _():
    return static_file("images/ppic.svg", ".")


@get("/userpic.png")
def _():
    return static_file("images/userpic.png", ".")


@get("/3dcircle.svg")
def _():
    return static_file("images/3dcircle.svg", ".")


@get("/chatty.png")
def _():
    return static_file("images/chatty.png", ".")


@get("/lightblue.png")
def _():
    return static_file("images/lightblue.png", ".")


@get("/lightpurple.png")
def _():
    return static_file("images/lightpurple.png", ".")


@get("/circles.png")
def _():
    return static_file("images/circles.png", ".")


@get("/square.png")
def _():
    return static_file("images/square.png", ".")


@get("/logo.svg")
def _():
    return static_file("images/logo.svg", ".")


@get("/images/<image_name>")
def _(image_name):
    return static_file(image_name, root="./images")
