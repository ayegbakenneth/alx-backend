#!/usr/bin/yarn dev
import { createQueue, Job } from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781'];
const queue = createQueue();

const sendNotification = (PhoneNumber, message, job, done) => {
  let sum_total = 2, pending = 2;
  let sending = setSending(() => {
    if (total - pending <= sum_total / 2) {
      job.progress(total - pending, sum_total);
    }
    if (blacklistedNumbers.includes(phoneNumber)) {
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      clearInterval(sending);
      return;
    }
    if (sum_total === pending) {
      console.log(
        `Sending notification to ${phoneNumber},`,
        `with message: ${message}`,
      );
    }
    --pending || done();
    pending || clearInterval(sending);
  }, 1000);
};

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
