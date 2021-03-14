from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import json
import string
import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      if search_username and search_job :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username and user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      elif search_username  :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      elif search_job  :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd['id'] = randomString()
      users['users_list'].append(userToAdd)
      data = users
      resp = jsonify(userToAdd), 201
      #resp = jsonify(success=True, users[users_list]), 201
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp
   elif request.method == 'DELETE':
      # need to send whole user to the request
      userToDelete = request.get_json()
      users['users_list'].remove(userToDelete)
      resp = jsonify(userToDelete), 200
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp

def randomString():
   letters = string.ascii_lowercase
   digits = string.digits
   randStr = (''.join(random.choice(letters) for i in range(3)))
   randDigs = (''.join(random.choice(digits) for i in range(3)))
   return (randStr + randDigs)
      
# def get_users():
#    search_username = request.args.get('name') #accessing the value of parameter 'name'
#    if search_username :
#       subdict = {'users_list' : []}
#       for user in users['users_list']:
#          if user['name'] == search_username:
#             subdict['users_list'].append(user)
#       return subdict
#    return users
   
@app.route('/users/<id>')

def get_user(id):
   if id :
      for user in users['users_list']:
        if user['id'] == id:
           return user
      return ({})
   return users
   
   