#!/usr/bin/yarn dev
import { createQueue } from 'kue';

const the_queue = createQueue({name: 'push_notification_code'});

const the_job = the_queue.create('push_notification_code', {
  phoneNumber: '07045679939',
  message: 'Account registered',
});

the_job
  .on('enqueue', () => {
    console.log('Notification job created:', the_job.id);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed attempt', () => {
    console.log('Notification job failed');
  });
the_job.save();
