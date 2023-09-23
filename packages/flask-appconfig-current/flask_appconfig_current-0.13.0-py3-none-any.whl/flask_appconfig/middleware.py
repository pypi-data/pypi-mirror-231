# -*- coding: utf-8 -*-
# from: http://flask.pocoo.org/snippets/35/
# written by Peter Hansen


class ReverseProxied(object):
    """Wrap the application in this middleware and configure the front-end
    server to add these headers, to let you quietly bind this to a URL other
    than / and to an HTTP scheme that is different than what is used locally.

    In nginx:
    location /myprefix {
        proxy_pass http://192.168.0.1:5001;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Scheme $scheme;
        proxy_set_header X-Script-Name /myprefix;
        }

    :param app: the WSGI application
    """

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        if script_name := environ.get("HTTP_X_SCRIPT_NAME", ""):
            environ["SCRIPT_NAME"] = script_name
            path_info = environ["PATH_INFO"]
            if path_info.startswith(script_name):
                environ["PATH_INFO"] = path_info[len(script_name) :]

        if scheme := environ.get("HTTP_X_SCHEME", ""):
            environ["wsgi.url_scheme"] = scheme
        return self.app(environ, start_response)

    # pass through other attributes, like .run() when using werkzeug
    def __getattr__(self, key):
        return getattr(self.app, key)
