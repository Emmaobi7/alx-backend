import { createClient, print } from 'redis';

const client = createClient()

client.on('error', function(err) {
  console.log(`Redis client not connected to the server: ${err}`)
});

client.on('connect', function() {
  console.log('Redis client connected to server')
});

client
  .MULTI()
  .hset('HolbertonSchools', 'Portland', 50, print)
  .hset('HolbertonSchools', 'Seattle', 80, print)
  .hset('HolbertonSchools', 'New York', 20, print)
  .hset('HolbertonSchools', 'Bogota', 20, print)
  .hset('HolbertonSchools', 'Cali', 40, print)
  .hset('HolbertonSchools', 'Paris', 2, print)
  .EXEC()
client.hgetall('HolbertonSchools', function(err, hash_val) {
  console.log(hash_val)
})
