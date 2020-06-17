from flask import Flask, render_template, request, send_file, session
import helper

app = Flask(__name__)
app.secret_key = 'q9ghevuqv'

@app.errorhandler(404)
def not_found(error):
    return render_template('not_found.html')

@app.errorhandler(500)
def internal(error):
    return render_template('internal.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mp3/<variable>')
def mp3(variable):
    additive = (request.full_path).replace("/mp3/", "")
    print (additive)
    session['url'] = "https://youtube.com/" + additive
    session['title'] = helper.retrieve_title(session['url'])
    
    if session['title'] == 'Error Occurred':
        return render_template('internal.html')
    
    while session['title'] == 'YouTube':
        session['title'] = helper.retrieve_title(session['url'])
    length = helper.retrieve_length(session['url'])
    thumbnail_url = helper.retrieve_thumbnail(session['url'])
    
    return render_template('mp3.html', title = session['title'], length = length, thumbnail_url = thumbnail_url)

@app.route('/download/')
def final():
    helper.download(session['title'])
    return send_file('{}.mp3'.format(session['title']), as_attachment = True, attachment_filename = '{}.mp3'.format(session['title']) )