import boto3

table.delete_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)