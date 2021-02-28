from flaskapp import init_flask_app

plotlyApp = init_flask_app()

if __name__ == "__main__":
    plotlyApp.run(host='0.0.0.0', debug=True)
