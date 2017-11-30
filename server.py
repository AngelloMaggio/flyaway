from flask import Flask
from flask_admin import Admin, BaseView, expose


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class MyView(BaseView):
    @expose('/')
    def index(self):
        return all_users()


app = Flask(__name__)
admin = Admin(app, name='FlyAdmin', template_mode='bootstrap3')
admin.add_view(MyView(name='Users'))



cred = credentials.Certificate("./letsflytomorrow-firebase-adminsdk-m043u-eec1029b81.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://letsflytomorrow.firebaseio.com'
})




@app.route('/users')
def all_users():

    out = ''

    ref = db.reference('users')

    print str(ref.get().values()[0].values())

    for value in ref.get().values()[0].values():
        if not isinstance(value, basestring) or not isinstance(value, unicode):
            out+= 'User: '+value['username']
            out += '<br>'
            out+= 'Description: '+value['description']
            out += '<br>'
            out+= 'Age: '+value['description']
            out += '<br>'
            out+= 'Location: '+value['location']
            out+= '<br>'
            out+= '<br>'
            out+= '<br>'


    return out

if __name__ == '__main__':
    app.run()