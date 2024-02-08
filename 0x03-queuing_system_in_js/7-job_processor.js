var kue = require('kue')
var new_job = kue.createQueue()


const blacklistNumbers = ['4153518780', '4153518781']

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0);
  if (blacklistNumbers.includes(phoneNumber))
    return done(new Error(`phone number ${phoneNumber} is blacklisted`))

  job.progress(50);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
  done();
}

new_job.process('push_notification_code_2', 2, function(job, done) {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
