import boto3
from boto3.session import Session

'''
Specify the region, access key and secret key to obtain the connection
'''

my_connection = boto3.resource('ec2', region_name="us-east-2",
	aws_access_key_id = 'ACCESS_KEY',
	aws_secret_access_key = 'SECRET_KEY')


# #delete key pair
# keypair = my_connection.KeyPair('Cloud_Computing')
# keypair.delete()

'''
Create a new key pair
'''

response = my_connection.create_key_pair(KeyName='Cloud_Computing_MiniAssignment_1')
print(response)
print(response.key_material)
s = Session()
ec2_regions = s.get_available_regions(service_name='ec2', partition_name='aws')
print("The available regions are..")
print(ec2_regions)


'''
Create a security group
'''


security_group = my_connection.create_security_group(GroupName="Cloud_Computing_MiniAssignment_1",Description='Assignment to create EC2 instance programmatically')
print('Security Group and metadata\n')
print(security_group)
data = security_group.authorize_ingress(IpProtocol="tcp",CidrIp="0.0.0.0/0",FromPort=22,ToPort=22)
print(data)
#security_group.delete()

'''
Create new instances with security_group and access key
'''

instance = my_connection.create_instances(
	ImageId='ami-0b59bfac6be064b78',
	MinCount=1,
	MaxCount=1,
	InstanceType='t2.micro',
	SecurityGroups=['Cloud_Computing_MiniAssignment_1'], KeyName='Cloud_Computing_MiniAssignment_1')

print('List of existing instances')
for instance in my_connection.instances.all():
	print('Instace ID :'+ instance.id)
	print('Instace State: ')
	print(instance.state)

'''
Terminate all instances
'''
print('Terminating all the existing instances')
for instance in my_connection.instances.all():
	response = instance.terminate()
	print(response)
