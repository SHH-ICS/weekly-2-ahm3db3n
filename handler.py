from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return '''
    <!DOCTYPE HTML>
    <html>
      <head>
        <title>Form Page</title>

        <!-- MDL Inclusions -->
        <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
        <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">
        <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>

      </head>
      <body>
        <form name="myForm" action="/handler" method="POST">
          <input type="text" name="myVariable">
          <button type="submit">Submit</button>
        </form>
      </body>
    </html>
    '''

@app.route('/handler', methods=['POST'])
def handler():
    my_variable = request.form.get('myVariable', '')
    return f'<h1>My Program</h1><p>My Variable is = {my_variable}</p>'

if __name__ == "__main__":
    app.run(debug=True)
