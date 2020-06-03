from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
sio = SocketIO(app, async_mode='eventlet')

colors = {
    'red': 128,
    'green': 128,
    'blue': 128

}


@app.route('/')
def hello_world():
    return render_template('index.html', title="Главная стр", colors=colors)


@app.route('/remote')
def remote():
    return render_template('remote.html', colors=colors)


@sio.on('colors', namespace='/flask')
def colors(msg):
    sio.emit('square', msg, namespace='/flask')




if __name__ == '__main__':
    sio.run(app, debug=True)