from flask import Flask, request, render_template, send_from_directory, jsonify

from views import main_blueprint

app = Flask(__name__)
app.config['DEBUG'] = True

app.run()
