from werkzeug.middleware.dispatcher import DispatcherMiddleware
from api import app as api
from server import app as server

application = DispatcherMiddleware(server, {
    '/api': api
})
