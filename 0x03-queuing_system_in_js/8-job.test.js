#!/usr/bin/yarn test
import sinon from 'sinon';
import { expect } from 'chai';
import { createQueue } from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  const ken = sinon.spy(console);
  const the_queue = createQueue({ name: 'push_notification_code_test' });

  before(() => {
    the_queue.testMode.enter(true);
  });

  after(() => {
    the_queue.testMode.clear();
    the_queue.testMode.exit();
  });

  afterEach(() => {
    ken.log.resetHistory();
  });

  it('displays an error message if jobs is not an array', () => {
    expect(
      createPushNotificationsJobs.bind(createPushNotificationsJobs, {}, the_queue)
    ).to.throw('Jobs is not an array');
  });

  it('adds jobs to the queue with the correct type', (done) => {
    expect(the_queue.testMode.jobs.length).to.equal(0);
    const jobInfos = [
      {
        phoneNumber: '44556677889',
        message: 'Use the code 1982 to verify your account',
      },
      {
        phoneNumber: '98877665544',
        message: 'Use the code 1738 to verify your account',
      },
    ];
    createPushNotificationsJobs(jobInfos, the_queue);
    expect(the_queue.testMode.jobs.length).to.equal(2);
    expect(the_queue.testMode.jobs[0].data).to.deep.equal(jobInfos[0]);
    expect(the_queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    the_queue.process('push_notification_code_3', () => {
      expect(
        ken.log
          .calledWith('Notification job created:', the_queue.testMode.jobs[0].id)
      ).to.be.true;
      done();
    });
  });

  it('registers the progress event handler for a job', (done) => {
    the_queue.testMode.jobs[0].addListener('progress', () => {
      expect(
        ken.log
          .calledWith('Notification job', the_queue.testMode.jobs[0].id, '25% complete')
      ).to.be.true;
      done();
    });
    the_queue.testMode.jobs[0].emit('progress', 25);
  });

  it('registers the failed event handler for a job', (done) => {
    the_queue.testMode.jobs[0].addListener('failed', () => {
      expect(
        ken.log
          .calledWith('Notification job', the_queue.testMode.jobs[0].id, 'failed:', 'Failed to send')
      ).to.be.true;
      done();
    });
    the_queue.testMode.jobs[0].emit('failed', new Error('Failed to send'));
  });

  it('registers the complete event handler for a job', (done) => {
    the_queue.testMode.jobs[0].addListener('complete', () => {
      expect(
        ken.log
          .calledWith('Notification job', the_queue.testMode.jobs[0].id, 'completed')
      ).to.be.true;
      done();
    });
    the_queue.testMode.jobs[0].emit('complete');
  });
});
