import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentData')

def lambda_handler(event, context):
    try:
        student_id = event.get('id')
        name = event.get('name')
        student_class = event.get('class')
        age = event.get('age')

        if not all([student_id, name, student_class, age]):
            return {
                'statusCode': 400,
                'body': json.dumps('Missing required fields')
            }

        response = table.put_item(
            Item={
                'studentId': student_id,
                'name': name,
                'class': student_class,
                'age': age
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Student added successfully!')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error adding student: {str(e)}')
        }
# This code is a Lambda function that inserts student data into a DynamoDB table.