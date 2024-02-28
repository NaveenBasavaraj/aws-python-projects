import boto3


def create_iam_user(username):
    iam = boto3.client("iam")
    response = iam.create_user(UserName=username)
    print(response)


if __name__ == "__main__":
    create_iam_user("cli_testuser1")
    # create_iam_user("cli_testuser1")
