from flask import Flask 
app=flask(__name__)
@app.route("/")
def home ():
    return "<h1>hello deployed in vercel</h1>"
if __name__=="__main__":
    app.run(debug=true)