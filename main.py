import flask
import functions_framework

@functions_framework.http
def main(request: flask.wrappers.Request):
    """ HTTP Cloud Functions """
    log_headline: str = "main()"
    print(f"{log_headline} · Init")


if __name__ == '__main__':
    print("version-tracker local run")

    app = flask.Flask(__name__) # Creates a Flask app instance
    request = flask.request
    main(request)

