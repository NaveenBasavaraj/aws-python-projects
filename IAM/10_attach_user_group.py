import boto3

def add_user_to_group(username, groupname):
    iam = boto3.client("iam")
    response = iam.add_user_to_group(
        UserName=username,
        GroupName=groupname
    )
    return response

if __name__ == '__main__':
    res = add_user_to_group("pynaveen", "RDSAdmins2")
    print(res)