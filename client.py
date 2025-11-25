import sys
import socketio
from config import COLORS

sio = socketio.Client()

@sio.event
def message(data):
    sender = data.get('sid')
    text = data.get('text')
    if sender == sio.sid:
        print(f'{COLORS.GREEN.value}[ME] {text}{COLORS.RESET.value}')
    else:
        print(f'{COLORS.CYAN.value}[OTHER] {text}{COLORS.RESET.value}')


if __name__ == "__main__":
    try:
        sio.connect('http://0.0.0.0:4000')
        print('my sid is', sio.sid)
        while True:
            line = input(":> ")
            if len(line) > 0:
                sio.emit('message', {'text': line, 'sid':  sio.sid})
    except socketio.exceptions.ConnectionError as e:
        print(f'Connection error: {e}')
        print('Make sure the server is running on http://0.0.0.0:4000')
    except KeyboardInterrupt:
        print('\nDisconnecting...')
        sio.disconnect()