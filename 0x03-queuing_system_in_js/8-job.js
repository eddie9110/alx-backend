export default function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
      throw new Error('Jobs is not an array');
    }
  
    jobs.forEach((data) => {
      let job = queue.create('push_notification_code_3', data);
      job.on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      }).on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      }).on('failed', (error) => {
        console.log(`Notification job ${job.id} failed: ${error}`);
      });
      job.save((err) => {
        if (!err) console.log(`Notification job created: ${job.id}`);
      });
    });
}
