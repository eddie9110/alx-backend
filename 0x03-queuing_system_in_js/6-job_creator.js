import kue from 'kue';
const queue = kue.createQueue();

const data = {
  phoneNumber: '722989898',
  message: "This is the code to verify your account"
}

const job = queue.create('push_notification_code', data).save((error) => {
  if (!error) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));
