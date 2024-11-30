from flask import render_template, request, redirect, url_for, Blueprint, jsonify
from app.models.page_setup_model import page_setup_model
from app.models.text_summarizer_model import text_summarizer_model
#import app.utils.text_summeriser as ts

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/text_summarizer')
def text_summarizer_documentation():
    #page setup
    pages_setup_model = page_setup_model()
    pages_setup_model.page_path = ["Text Summariser", "Documentation"]
    pages_setup_model.page_html_id = "text-summariser-page-1"

    return render_template('text_summarizer_dashboard.html',pages_setup_model=pages_setup_model)

# @bp.route('/text_summarizer/summariser', methods=['GET','POST'])
# def text_summarizer_summariser():
#     #page setup
#     pages_setup_model = page_setup_model()
#     pages_setup_model.page_path = ["Text Summariser", "Text Summariser"]
#     pages_setup_model.page_html_id = "text-summariser-page-2"

#     o_text_summarizer_model = text_summarizer_model()
#     o_text_summarizer_model.input_text = ''
#     if request.method == 'POST':
#         input_text = request.form.get('inputText').strip()
#         if not input_text:
#             o_text_summarizer_model.error_message = "Please enter proper text."
#             return render_template('text_summarizer_summariser.html',pages_setup_model=pages_setup_model,page_model=o_text_summarizer_model)
#         o_text_summarizer_model.input_text = input_text
#         o_text_summarizer_model.output_text = ts.summarize_text(input_text)

#     return render_template('text_summarizer_summariser.html',pages_setup_model=pages_setup_model,page_model=o_text_summarizer_model)

@bp.route('/chatbots')
def chatbots_documentation():
    pages_setup_model = page_setup_model()
    pages_setup_model.page_path = ["Chatbots", "Documentation"]
    pages_setup_model.page_html_id = "chatbot-page-1"

    return render_template('chatbots_documentation.html',pages_setup_model=pages_setup_model)

@bp.route('/chatbots/chatbot')
def chatbots_chatbot():
    pages_setup_model = page_setup_model()
    pages_setup_model.page_path = ["Chatbots", "Chatbot"]
    pages_setup_model.page_html_id = "chatbot-page-2"
    
    return render_template('chatbots_chatbot.html',pages_setup_model=pages_setup_model)

@bp.route('/api/chatbot', methods=['GET','POST'])
def chatbot():
    data = request.get_json()
    message = data.get('message', '')
    return jsonify({'reply': f'reply to: {message}'})
