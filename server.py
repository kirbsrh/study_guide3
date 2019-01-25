from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():

        return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form', methods=['POST'])
def show_form():

    session['mood'] = request.form("mood")
    mood = session['mood']
    
    return render_template('form.html', mood = mood)

@app.route('/results')
def show_results():

   
   return render_template('results.html')

@app.route('/save-name')
def save_name():
    session['name'] = request.args.get("name")

    
    return render_template('form.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
