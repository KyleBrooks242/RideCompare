# Flask file
import flask, jinja2, ast, json, re
from flask import Flask, json, jsonify, render_template, request, make_response
from jinja2 import Environment, select_autoescape
from os.path import dirname

env = Environment(autoescape=select_autoescape(['html', 'xml']),
                  loader=jinja2.FileSystemLoader(dirname(__file__) + "/templates/"))

app = Flask(__name__)

@app.route('/trains/')
def getName():
    data = getAllCompetitions()
    return render_template( "home.html", name="Jimmy CrackCorn" )