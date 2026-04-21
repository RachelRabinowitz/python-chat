from fastapi import FastAPI
import socketio
import uvicorn

# Async Socket.IO server running as an ASGI app alongside FastAPI
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
fastapi_app = FastAPI()

# Wrap the FastAPI app with the Socket.IO ASGI app so both are served
app = socketio.ASGIApp(sio, other_asgi_app=fastapi_app)


@sio.event
async def connect(sid, environ):
    print('Client connected:', sid)


@sio.on('message')
async def message(sid, message):
    print('Socket ID:', sid)
    print(message)

    await sio.emit('message', message)


if __name__ == '__main__':
    # Run the combined ASGI app (Socket.IO + FastAPI)
    # Note: uvicorn can take an ASGI app instance directly.
    uvicorn.run(app, host='0.0.0.0', port=4000)
