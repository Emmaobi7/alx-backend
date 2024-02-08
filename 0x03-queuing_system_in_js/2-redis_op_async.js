import { createClient, print } from 'redis';
const { promisify } = require('util')

const client = createClient()

client.on('error', function(err) {
  console.log(`Redis client not connected to the server: ${err}`)
});

client.on('connect', function() {
  console.log('Redis client connected to server')
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print)
}
 
const displaySchoolValueAsync = promisify(client.get).bind(client);
async function displaySchoolValue(schoolName) {
  try {
    const val = await displaySchoolValueAsync(schoolName)
    console.log(val)
  } catch(err) {
    console.log(err)
  }
}


(async () => {
await displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
await displaySchoolValue('HolbertonSanFrancisco');
})();
