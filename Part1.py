import boto3

'''
Specify the region, access key and secret key to obtain the connection
'''

my_connection = boto3.resource('ec2', region_name="us-east-2",
	aws_access_key_id = 'ACCESS_KEY',
	aws_secret_access_key = 'SECRET_KEY')

'''
Create a connection without security group of key pair.
'''

instance = my_connection.create_instances(
	 ImageId='AMI_HASH',
	 MinCount=1,
	 MaxCount=1,
	 InstanceType='t2.micro')
print('EC2 instance was created with the id :' + instance[0].id)

'''
List all instances
'''

print('List of existing instances')
for instance in my_connection.instances.all():
	print('Instace ID :'+ instance.id)
	print('Instace State')
	print(instance.state)

'''
Terminate all instances
'''
print('Terminating all the existing instances')
for instance in my_connection.instances.all():
	response = instance.terminate()
	print(response)
