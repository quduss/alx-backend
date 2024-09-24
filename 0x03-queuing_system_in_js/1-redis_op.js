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

// Function to set a key-value pair in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Function to get the value of a key in Redis
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.log(`Error fetching value for ${schoolName}: ${err}`);
    } else {
      console.log(reply);
    }
  });
}

// Test the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
