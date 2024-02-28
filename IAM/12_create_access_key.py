import boto3

def create_access(username):
    iam = boto3.client("iam")
    
    res = iam.create_access_key(
        UserName=username
    )
    return res

def update_access(username):
    iam = boto3.client("iam")
    
    res = iam.update_access_key(
        UserName=username,
        Status='Inactive'
    )
    return res

if __name__ == "__main__":
    res = update_access("cli_testuser01")