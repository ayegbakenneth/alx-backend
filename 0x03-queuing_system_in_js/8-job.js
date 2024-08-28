#!/usr/bin/yarn dev
import { Queue, Job } from 'kue';

export const createPushNotificationsJobs = (created_job, queue) => {
  if (!(created_job instanceof Array)) {
    throw new Error('Jobs is not an array');
  }
  for (const dataJob of jobs) {
    const techJob = queue.create('push_notification_code_3', dataJob);

    techJob
      .on('enqueue', () => {
        console.log('Notification job created:', techJob.id);
      })
      .on('complete', () => {
        console.log('Notification job', techJob.id, 'completed');
      })
      .on('failed', (error) => {
        console.log('Notification job', techJob.id, 'failed:', error.message || error.toString());
      })
      .on('progress', (progress, _data) => {
        console.log('Notification job', techJob.id, `${progress}% complete`);
      });
    techJob.save();
  }
};

export default createPushNotificationsJobs;
