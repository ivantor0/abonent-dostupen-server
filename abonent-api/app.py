import eve
from eve_elastic import Elastic
from flask_cors import CORS


app = eve.Eve(data=Elastic)
CORS(app)

if __name__ == '__main__':
    app.run()

