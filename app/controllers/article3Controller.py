from app.controllers.controller import ControllerBase
from flask import render_template

class Article3Controller(ControllerBase):
    @staticmethod
    def get():
        return render_template('Article3.html')
