from gevent import monkey
 
monkey.patch_all()
 
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room
 
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'nuttertools'
socketio = SocketIO(app)
 
 
@app.route('/')
def chat():
    return render_template('chat.html')
 
@app.route('/login')
def login():
    return render_template('login.html')
 
 
@socketio.on('message', namespace='/chat')
def chat_message(message):
    #messageText='Question is '+ str(message.data.message)
    messageText = "Question is "+ message['data']['message']+ "\n Response is Please type in your query";
    print messageText
    emit('message', messageText, broadcast = True)
 
@socketio.on('connect', namespace='/chat')
def test_connect():
    emit('my response', {'data': 'Connected', 'count': 0})
 
 
if __name__ == '__main__':
    socketio.run(app)
