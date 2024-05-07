import kue from 'kue';
import { it, describe } from 'mocha'
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();
const list = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    }
];

describe('does something cool', () => {
  before(() => queue.testMode.enter());
  afterEach(() => queue.testMode.clear());
  after(() => queue.testMode.exit());

  it('should test creation of notifications', () => { 
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs.type).to.equal(Array);
  });
});
