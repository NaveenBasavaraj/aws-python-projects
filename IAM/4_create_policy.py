import boto3
import json


def create_policy(policy_name, user_policy):
    iam = boto3.client("iam")

    response = iam.create_policy(
        PolicyName=policy_name, PolicyDocument=json.dumps(user_policy)
    )
    print(response)


user_policy = {
    "Version": "2012-10-17",
    "Statement": [{"Effect": "Allow", "Action": "*", "Resource": "*"}],
}

if __name__ == "__main__":
    policy_name = "pyFullAccess"
    create_policy(policy_name, user_policy)
