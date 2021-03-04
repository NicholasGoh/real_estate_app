from flask import render_template, flash, redirect, url_for, Markup, request
from flask import current_app as flaskapp

# self made packages
from flaskapp.forms import AllPersonalInfo
from flaskapp.scheme_manager import SchemeManager

@flaskapp.route('/')

# things that render on homepage
@flaskapp.route('/homepage')
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

# Financial Scheme portion
# things that render on personal_info_page
@flaskapp.route('/personal_info', methods=['GET', 'POST'])
def personal_info():
    # self made container for user inputs
    form = AllPersonalInfo()
    return render_template('personal_info.html', form=form)

# Financial Scheme portion
@flaskapp.route('/scheme_eligibility', methods=['GET', 'POST'])
def scheme_eligibility():
    form = AllPersonalInfo(request.form)
    if form.validate_on_submit():
        schemeOutputs = SchemeManager(form).foo() # assume list
        string = ''
        for data in schemeOutputs:
            string = str(data.replace('\n', '<br/>').replace('\t', '')) + '<br/>' # end of simple concatenation
            # display on webpage
            flash(Markup(string))

    return render_template('scheme_eligibility.html')
