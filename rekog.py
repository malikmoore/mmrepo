import boto3
malik = boto3.client('rekognition')

response = malik.recognize_celebrities(
    Image={
        'S3Object': {
            'Bucket': 'www.malikmoore.cloud',
            'Name': 'celebJD.jpg'
        }
    }
)
print(response)
