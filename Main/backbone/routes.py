from backbone import webapp


@webapp.route("/")
def index():
    return "hello world!"
