from flask import Flask
import time

TreintaDias = Flask(__name__)

@TreintaDias.route('/time')
def get_current_time():
    return {'time': time.time()}
