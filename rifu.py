import boto3
ec2 = boto3.resource('ec2')
instances = ec2.create_instances(
     ImageId='ami-0c1a7f89451184c8b',
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='dhoni'
)
