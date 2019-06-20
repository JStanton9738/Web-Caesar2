from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

add_form ="""
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            } 
            textera {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/add" method='POST'>
            <label>
                Rotate by:
                <input type="text" name="rot" value="0"/>
            </label>
            <br>
            <textarea name="text"></textarea>
            <br>
            <input type="submit" value="Submit Query"/>
        </form>
    </body>
</html>
"""     


@app.route("/")
def index():
    return add_form

@app.route("/add", methods=['POST'])
def encrypt():
    text = request.form["text"] 
    rot = int(request.form["rot"])
    a = rotate_string(text, rot)
    return "<h1>" + a + "</h1>"
    
    


app.run()   
        