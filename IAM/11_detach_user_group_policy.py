import boto3

def detach_user_group_policy(user_group,arn):
    iam = boto3.client("iam")
    
    res = iam.detach_group_policy(
        GroupName=user_group,
        PolicyArn=arn
    )
    return res
if __name__ == "__main__":
    
    res = detach_user_group_policy("RDSAdmins2","arn:aws:iam::037591017943:policy/pyFullAccess")