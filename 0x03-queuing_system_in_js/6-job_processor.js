var kue = require('kue')
var new_job = kue.createQueue()

function sendNotification(phoneNumber, message) {
  console.log(`sending notification to ${phoneNumber}, message: ${message}`)
}

new_job.process('push_notification_code', function(job, done) {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
