import boto3

def create_group(group_name):
    iam = boto3.client("iam")
    response = iam.create_group(GroupName=group_name)
    return response

if __name__ == '__main__':
    res = create_group("RDSAdmins2")
    print(res)