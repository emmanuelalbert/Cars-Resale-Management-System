from flask import *
from admin import admin
from public import public
from customer import customer
from courier import courier

app=Flask(__name__)
app.secret_key="hai"
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(courier,url_prefix='/courier')

@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")


app.run(debug=True,port=5466)
