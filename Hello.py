# @Author: karthick
# @Date:   2017-08-15T14:54:29+02:00
# @Last modified by:   karthick
# @Last modified time: 2017-08-15T16:22:58+02:00

from flask import Flask
app = Flask(__name__)

#route() function is a decorator that tells the application which URL should call the associated function
@app.route('/blog/<int:postID>')
def show_blog(postID):
    return "Blog Number %d! :)" % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return "Revision Number %0.3f! :)" % revNo

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'



if __name__=="__main__":
    app.run(debug=True) # when debug is enabled, the server will reload itself if the code changes
