from flask import Flask, render_template, request, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

 
@app.route("/") 
def index_page(): 
    return render_template("index.html.j2", mystyle=url_for('static', filename='styles/mystyles_index.css')) 
 
@app.route("/abonent") 
def abonent_page():
    if request.args.get("full_name"):
        fname = request.args.get("full_name").split(" ")
        surname = fname[0] if len(fname) else ""
        name = fname[1] if len(fname) > 1 else ""
        patronym = fname[2] if len(fname) > 2 else ""
    address = request.args.get("address") if request.args.get("address") else ""
    phone = request.args.get("phone") if request.args.get("phone") else ""
    return render_template("abonent.html.j2", mystyle=url_for('static', filename='styles/mystyles_abonent.css'),
                           surname=surname, name=name, patronym=patronym, address=address, phone=phone)


if __name__ == '__main__': 
    app.run(debug=True, port=8888)

