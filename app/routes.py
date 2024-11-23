from flask import render_template, request, redirect, url_for, Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/my_text_summarizer')
def text_summarizer():
    return render_template('text_summarizer.html')

@bp.route('/my_chatbots')
def chatbots():
    return render_template('my_chatbot.html')
