from flask import render_template, flash, redirect, url_for, Markup, request
from flask import current_app as flaskapp
from flask_googlemaps import GoogleMaps, Map
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

# code to render maps
@flaskapp.route('/map', methods=['GET'])
def my_map():
    with open('all_data/transactions/transactions.json', 'r') as f:
        data = json.load(f)
    markers = (float(data['property_1']['x']), float(data['property_1']['y']))
    map = Map(
                identifier="view-side",
                varname="map",
                style="height:720px;width:1100px;margin:0;", # hardcoded!
                lat=1.2729546766736342,
                lng=103.80643708167351,
                zoom=15,
                markers=[markers]
            )
    return render_template('map.html', map=map)
