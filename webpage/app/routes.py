from flask import render_template, flash, redirect, url_for, Markup
from app import app

# self made packages
from app.forms import AllPersonalInfo
from app.scheme_manager import SchemeManager

@app.route('/')

# things that render on homepage
@app.route('/hompage')
def homepage():
    # hard coded things to display
    user = {'username': 'Guest'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
    ] # end of hard code

    # pass hard coded variables to homepage.html
    return render_template('homepage.html', title='Home', user=user, posts=posts)

# things that render on personal_info_page
@app.route('/personal_info', methods=['GET', 'POST'])
def personal_info():
    # self made container for user inputs
    form = AllPersonalInfo()
    # simple concatenation of all inputs on submit
    if form.validate_on_submit():
        schemeOutputs = SchemeManager(form).foo() # assume list
        string = ''
        for data in schemeOutputs:
            string += str(data.replace('\n', '<br/>').replace('\t', '')) + '<br/>' # end of simple concatenation

        # display on webpage
        flash(Markup(string))
        return redirect(url_for('display_brackets'))
    return render_template('personal_info.html', title='Enter personal info', form=form)

@app.route('/display_brackets')
def display_brackets():
    return render_template('display_brackets.html', title='Home')
