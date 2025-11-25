# Chat Client (Python + Socket.IO)

## Overview

A simple Python chat client using Socket.IO with colored messages and unique client IDs (SIDs).
Supports multiple clients simultaneously.

---

## Features
- Real-time chat using Socket.IO
- Colored messages to differentiate between clients
- Unique SID for each client
- Handles multiple clients simultaneously
- Clean input handling to avoid message overlap
- Supports running inside Docker for easy isolation

---

## Requirements

* Python 3.9+ (for local run)
* Docker (optional, for containerized run)
* Python packages:

### Local run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run chat:

```bash
python server.py
```

```bash
python client.py
```

### Docker run

1. Build the image:

```bash
docker build -t chat-client .
```

2. Run a single client:

```bash
docker run -it --rm chat-client
```

3. Run multiple clients:

```bash
docker run -it --rm chat-client
docker run -it --rm chat-client
```

* Each container acts as a separate client with its own SID.

---

## Notes

* Input prompt stays active even when messages arrive from the server.
