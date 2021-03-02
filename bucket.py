from boto3.session import Session
import secrets


def put_file_in_bucket(file_path,
                       bucket_name,
                       s3_bucket=secrets.s3_bucket,
                       s3_bucket_access_key=secrets.s3_bucket_access_key,
                       s3_bucket_secret_key=secrets.s3_bucket_secret_key):
    """Put a file in a bucket"""
    # get S3 bucket session
    session = Session(aws_access_key_id=s3_bucket_access_key, aws_secret_access_key=s3_bucket_secret_key)
    s3 = session.resource('s3')
    your_bucket = s3.Bucket(s3_bucket)

    # upload the file
    your_bucket.upload_file(file_path, bucket_name)
