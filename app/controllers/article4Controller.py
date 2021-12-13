from app.controllers.controller import ControllerBase
from flask import render_template

class Article4Controller(ControllerBase):
    @staticmethod
    def get():
        return render_template('SoC.html')
