from flask import Flask, render_template, Response
import time
app = Flask(__name__)

@app.route('/content') # render the content a url differnt from index. This will be streamed into the iframe
def content():
    def timer(t):
        for i in range(t):
            time.sleep(5) #put 60 here if you want to have seconds
            yield str(i)
    return Response(timer(10), mimetype='text/html') #at the moment the time value is hardcoded in the function just for simplicity

@app.route('/')
def index():
    return render_template('test.html.jinja') # render a template at the index. The content will be embedded in this template

if __name__ == '__main__':
    app.run(use_reloader=False)
