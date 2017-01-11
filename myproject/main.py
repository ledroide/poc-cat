import falcon
from waitress import serve

class Home:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.body = "PLATFORM - API Python"
 
api = falcon.API()

# Define routes
api.add_route('/', Home())

serve(api, host='*', port=8080)