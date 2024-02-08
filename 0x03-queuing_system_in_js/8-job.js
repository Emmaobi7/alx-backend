function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs))
    throw new Error('Jobs is not an array')
  for (let job of jobs) {
    job = queue.create('push_notification_3', job)
      .save(function(err) {
        if (!err)
	  console.log(`Notification job created: ${job.id}`)
      })
      .on('complete', function(res) {
        console.log(`Notification job ${job.id} completed`)
      })
      .on('failed', function(err) {
        console.log(`Notification job ${job.id} failed: ${err}`)
      })
      .on('progess', function(progress, res) {
        console.log(`Notification job ${job.id} ${progress}% complete`)
      })
  }
}

module.exports = createPushNotificationsJobs;
