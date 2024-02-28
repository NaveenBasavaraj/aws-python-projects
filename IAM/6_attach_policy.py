import boto3

def attach_policy(policy_arn, username):
    iam = boto3.client('iam')
    response = iam.attach_user_policy(UserName=username,
                                      PolicyArn=policy_arn)
    
    return response

if __name__ == "__main__":
    response = attach_policy("arn:aws:iam::037591017943:policy/pyFullAccess", "pynaveen")
    print(response)