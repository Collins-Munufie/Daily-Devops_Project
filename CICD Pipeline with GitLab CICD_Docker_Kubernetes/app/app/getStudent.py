import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')  # Updated to match the GET function

def lambda_handler(event, context):
    try:
        student_id = event.get('id')
        name = event.get('name')
        student_class = event.get('class')
        age = event.get('age')

        if not all([student_id, name, student_class, age]):
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing required fields'})
            }

        response = table.put_item(
            Item={
                'id': student_id,  # Changed from 'studentId' to 'id'
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
            'body': json.dumps({'error': str(e)})
        }
