import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const getProm = promisify(client.get).bind(client);

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`)
}).on('connect', () => {
    console.log('Redis client connected to the server');
});


function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  const res = await getProm(schoolName);
  console.log(res);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
