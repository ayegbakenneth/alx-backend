#!/usr/bin/yarn dev
import { createQueue } from 'kue';

const the_queue = createQueue();

const sendNotification = (phoneNumber, message) => {
  console.log(
    `Sending notification to ${phoneNumber},`,
    'with message:',
    message,
  );
};

the_queue.process('push_notification_code', (the_job, finished) => {
  sendNotification(the_job.data.phoneNumber, the_job.data.message);
  finished();
});
