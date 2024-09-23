import redis from 'redis';

// Create a Redis client with explicit configuration
const client = redis.createClient({
  host: '127.0.0.1',
  port: 6379
});

// Log when connected successfully
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Log when an error occurs
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: Error: ${err.message}`);
});

