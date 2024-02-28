import boto3

def attach_policy_to_group(policy_arn, group_name):
    iam = boto3.client("iam")
    
    response = iam.attach_group_policy(
        PolicyArn=policy_arn,
        GroupName=group_name
    )
    
    return response

if __name__ == '__main__':
    res = attach_policy_to_group("arn:aws:iam::037591017943:policy/pyFullAccess", "RDSAdmins2")
    print(res)
    
