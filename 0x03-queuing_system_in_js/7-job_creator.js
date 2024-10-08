#!/usr/bin/yarn dev
import { createQueue } from 'kue';

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account',
  },
];

const queue = createQueue({ name: 'push_notification_code_2' });

for (const data_job of jobs) {
  const the_job = queue.create('push_notification_code_2', data_job);

  the_job
    .on('enqueue', () => {
      console.log('Notification job created:', the_job.id);
    })
    .on('complete', () => {
      console.log('Notification job', the_job.id, 'completed');
    })
    .on('failed', (error) => {
      console.log('Notification job', the_job.id, 'failed:', error.message || error.toString());
    })
    .on('progress', (progress, _data) => {
      console.log('Notification job', job.id, `${progress}% complete`);
    });
  the_job.save();
}
