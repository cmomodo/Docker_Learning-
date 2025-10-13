from flask import Flask, request, jsonify, render_template
import redis
import os
import time

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
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/count')
def count():
    value = r.incr('counter')  # INCR command increments and returns the value
    return f'Counter value: {value}'

@app.route('/reset')
def reset():
    r.set('counter', 0)
    return 'Counter has been reset to 0'

@app.route('/health')
def health_check():
    status = 'healthy' if r and r.ping() else 'unhealthy'
    return jsonify({
        'status': status,
        'redis_connection': bool(r)
    })

@app.route('/store', methods=['POST'])
def store_value():
    data = request.get_json()
    if not data or 'key' not in data or 'value' not in data:
        return jsonify({'error': 'Missing key or value'}), 400

    r.set(data['key'], data['value'])
    return jsonify({'status': 'success'})

@app.route('/retrieve/<key>')
def retrieve_value(key):
    value = r.get(key)
    if value is None:
        return jsonify({'error': 'Key not found'}), 404
    return jsonify({'key': key, 'value': value})

@app.route('/stats')
def stats():
    if not r:
        return jsonify({'error': 'Redis not connected'}), 500

    info = r.info()
    return jsonify({
        'uptime_in_seconds': info.get('uptime_in_seconds'),
        'connected_clients': info.get('connected_clients'),
        'used_memory_human': info.get('used_memory_human'),
        'total_commands_processed': info.get('total_commands_processed')
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
