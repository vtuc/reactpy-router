from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component,html
# Now import reactpy_router
from reactpy_router import route,simple,link
#For get Parameter
from reactpy_router.core import use_params



@component
def myrouter():
    return simple.router(
        route("/",home()),
        route("/about",about()),
        #and router for get params
        route("/details/{names}",detailspage()),
        # now if you router not found
        route("*",html.h1("You Not Found Route Guys")),
    )

# now create component to view
@component
def home():
    # Now I Send Sample Params
    my_params = "youtube-kids"
    return html.div(
        html.h1("Home Page"),
        #Now I Create Navigation link
        link("about page", to="/about"),
        # And link with parameter
        link("details page", to="/details/{}".format(my_params)),
    )


# For About Page
@component
def about():
    return html.div(
        html.h1("about page"),
        link("Home page", to="/")
    )

# And For Details Page
@component
def detailspage():
    # And Now I Get Params From URL
    names = set(use_params()['names'].split("-"))
    # And Remove - 
    result_names = " ".join(names)
    print(names)
    return html.div(
        html.h1(f"details page , you page paramns is : {result_names}"),
        #Link to about page
        link("about page", to="/about")
    )






app = FastAPI()
configure(app,myrouter)