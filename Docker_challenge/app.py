from flask import Flask
import redis
import os

redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis_port = int(os.environ.get('REDIS_PORT', 6379))

try:
    r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
    # Test the connection
    r.ping()
    print(f"✓ Connected to Redis at {redis_host}:{redis_port}")
except redis.ConnectionError as e:
    print(f"✗ Failed to connect to Redis at {redis_host}:{redis_port}: {e}")
    r = None



app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'CoderCo Containers Session!'

@app.route('/count')
def count():
    value = r.incr('counter')  # INCR command increments and returns the value
    return f'Counter value: {value}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
