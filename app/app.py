"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.historyController import HistoryController
from app.controllers.webController import WebController
from app.controllers.evolutionController import EvolutionController
from app.controllers.softwareController import SoftwareController
from app.controllers.article1Controller import Article1Controller
from app.controllers.article2Controller import Article2Controller
from app.controllers.article3Controller import Article3Controller
from app.controllers.article4Controller import Article4Controller
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/history",methods=['GET'])
def history_get():
    return HistoryController.get()

@app.route("/web",methods=['GET'])
def web_get():
    return WebController.get()

@app.route("/evolution",methods=['GET'])
def evolution_get():
    return EvolutionController.get()

@app.route("/software",methods=['GET'])
def software_get():
    return SoftwareController.get()

@app.route("/article1",methods=['GET'])
def article1_get():
    return Article1Controller.get()

@app.route("/article2",methods=['GET'])
def article2_get():
    return Article2Controller.get()

@app.route("/article3",methods=['GET'])
def article3_get():
    return Article3Controller.get()

@app.route("/article4",methods=['GET'])
def article4_get():
    return Article4Controller.get()