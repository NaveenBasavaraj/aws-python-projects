import boto3


def list_all_users():
    iam = boto3.client("iam")
    paginator = iam.get_paginator("list_users")

    for response in paginator.paginate():
        for user in response["Users"]:
            username = user["UserName"]
            Arn = user["Arn"]
            print(f"user : {username} and arn: {Arn}")


if __name__ == "__main__":
    list_all_users()
