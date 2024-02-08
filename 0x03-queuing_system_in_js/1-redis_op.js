import { createClient, print } from 'redis';

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
 

function displaySchoolValue(schoolName) {
  client.get(schoolName, function(err, val) {
    console.log(val);
  })
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
