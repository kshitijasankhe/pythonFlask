from flask import Flask, render_template
from flask import jsonify, request

#app= Flask(__name__)

app=Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return "hello world!"

userDetails =[
    {
        "userName": "Kshitija",
        "userId": 1
    }
]
@app.route('/login', methods=['POST'])
def login():
    data=request.json
    u=data['username']
    p=data['password']
    return jsonify(u)


@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message='Sorry ' + name + ' you are too young ' + str(age)), 401
    else:
        return jsonify(message='Welcome' + name), 200


@app.route('/demo', methods=['GET', 'POST'])
def index():
    return render_template('demo.html')

#Creating a new usr
@app.route('/createUser', methods=['POST'])
def create_user():
    request_data = request.get_json()
    new_user={
        'userName': request_data['userName'],
        'userId': request_data['userId']

    }
    return jsonify(new_user)

#retriving a user if name matches
@app.route('/searchUser/<string:userId>')
def get_user(userId):
    for user in userDetails:
        if(user['userId']==userId):
            return jsonify(user)
        else:
             return jsonify({'message': 'user not found'})

app.run(port=5000)