# @Author: karthick
# @Date:   2017-08-15T14:54:29+02:00
# @Last modified by:   karthick
# @Last modified time: 2017-08-15T16:08:40+02:00

from flask import Flask
app = Flask(__name__)

#route() function is a decorator that tells the application which URL should call the associated function
@app.route('/blog/<int: postID>')
def show_blog(postID):
    return "Blog Number %d! :)" % postID

@app.route('/blog/<float: revNo>')
def revision(revNo):
    return "Revision Number %f! :)" % revNo

if __name__=="__main__":
    app.run(debug=True) # when debug is enabled, the server will reload itself if the code changes
