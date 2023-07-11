import argparse
import json
import os


# parser = argparse.ArgumentParser(
#     description="Publish Github event to RabbitMq Messanger")
# github_event = parser.add_argument('--event',
#                                    help='Provide Github event',
#                                    required=True)
# args = parser.parse_args()


def validate_workflow_json():
    # data = json.loads(args.github_event)
    # print(type(data))
    print(os.environ)


if __name__ == "__main__":
    validate_workflow_json()
