from flask import *
from admin import admin
from public import public

app=Flask(__name__)
app.secret_key="hai"
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')


app.run(debug=True,port=5466)
