#!/bin/bash
gunicorn --worker-class=gevent --workers $NUM_WORKERS --max-requests $MAX_REQUESTS \
 --bind 0.0.0.0:$API_PORT wsgi:app