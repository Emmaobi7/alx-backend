import createPushNotificationsJobs from './8-job.js';
const kue = require('kue')
const queue = kue.createQueue();
const { expect } = require('chai')

describe('Test job', function() {

  before(function() {
    queue.testMode.enter();
  })


  afterEach(function() {
    queue.testMode.clear();
  })

  after(function() {
   queue.testMode.exit()
  })

  it('should check for array', function() {
    expect(() => createPushNotificationsJobs(emma, queue)).to.throw();
  });

  it('should check for valid kue', function() {
    expect(() => createPushNotificationsJobs(jobs, 4)).to.throw();
  });

})
