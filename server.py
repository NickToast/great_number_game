from flask import Flask, render_template, redirect, session, request  # Import Flask to allow us to create our app, if u need render_template
import random           #import the random module
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'life' 	#key goes into here

@app.route('/')
def home():
    if "number" not in session:
        session['number'] = random.randint(1,100)
    if "tries" not in session:
        session['tries'] = 0
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    session['tries'] += 1
    # if "guessed" not in session:
    #     session['guessed'] = session['guess']
    # else:
    #     session['guessed'].extend(str(session['guess']))
    
    return redirect('/')

@app.route('/playagain')
def reset():
    session.clear()
    return redirect('/')







if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.