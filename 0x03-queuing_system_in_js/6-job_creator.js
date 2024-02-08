var kue = require('kue')

var queue = kue.createQueue();

const jobData = {phoneNumber: '+2349084303395', message: 'what a journey.'}

var job = queue
  .create('push_notification_code', jobData)
  .save((err) => {
    if (!err)
      console.log(`Notification job created: ${job.id}`)
  })

job.on('complete', function(res) {
  console.log('Notification job completed')
})

job.on('failed', function(err) {
  console.log('Notification job failed')
})
