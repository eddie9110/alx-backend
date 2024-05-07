import redis from 'redis';
const client = redis.createClient();

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`)
  }).on('connect', () => {
    console.log('Redis client connected to the server');
  });

const keyName = 'HolbertonSchools';
const cities = {'Portland': 50,
               'Seattle': 80,
               'New York': 20,
               'Bogota': 20,
               'Cali': 40,
               'Paris': 2}

for (const [key, val] of Object.entries(cities)) {
  client.hset(keyName, key, val, redis.print);
}

client.hgetall('HolbertonSchools', (error, object) => {
    if (error) {
        console.log(error);
        throw error;
    }
    console.log(object);
});
