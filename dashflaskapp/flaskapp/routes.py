from flask import render_template, flash, redirect, url_for, Markup, request
from flask import current_app as flaskapp
import json

# self made packages
from flaskapp.forms import AllPersonalInfo
from flaskapp.scheme_manager import SchemeManager

@flaskapp.route('/')
def defaultpage():
    return render_template('homepage.html', nav_bar='disable')

@flaskapp.route('/homepage')
def homepage():
    return render_template('homepage.html', nav_bar='disable')

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
