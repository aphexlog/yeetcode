'use strict';

const AWS = require('aws-sdk');
const s3 = new AWS.S3();

class EmptyBucketPlugin {
  constructor(serverless, options) {
    this.serverless = serverless;
    this.options = options;

    this.hooks = {
      'before:remove:remove': this.emptyBucket.bind(this),
    };
  }

  async emptyBucket() {
    const stage = this.serverless.service.provider.stage;
    if (stage !== 'prod') {
      const bucketNames = Object.entries(this.serverless.service.custom)
        .filter(([key]) => key.endsWith('_bucket_name'))
        .map(([, value]) => value);

      for (let bucket of bucketNames) {
        const listParams = {
          Bucket: bucket
        };

        let listedObjects;
        do {
          listedObjects = await s3.listObjectVersions(listParams).promise();

          if (listedObjects.Versions.length > 0) {
            const deleteParams = {
              Bucket: bucket,
              Delete: { Objects: [] }
            };

            listedObjects.Versions.forEach(({ Key, VersionId }) => {
              deleteParams.Delete.Objects.push({ Key, VersionId });
            });

            await s3.deleteObjects(deleteParams).promise();
          }
        } while (listedObjects.IsTruncated);
      }
    }
  }
}

module.exports = EmptyBucketPlugin;
