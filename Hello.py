# @Author: karthick
# @Date:   2017-08-15T14:54:29+02:00
# @Last modified by:   karthick
# @Last modified time: 2017-08-15T15:30:21+02:00

from flask import Flask
app = Flask(__name__)

#route() function is a decorator that tells the application which URL should call the associated function
@app.route('/<name>')
def hello_name(name):
    return "Hello %s! :)" % name



if __name__=="__main__":
    app.run('0.0.0.0', 5000,debug=True) # when debug is enabled, the server will reload itself if the code changes
