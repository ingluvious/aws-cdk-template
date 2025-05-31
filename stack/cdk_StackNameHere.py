from aws_cdk import (
    Duration,
    Stack,
    # aws_lambda as _lambda,
    # aws_iam as iam,
    # aws_sqs as sqs
)
from constructs import Construct

# Replace the Stack name below with e.g., UpertTestAutomationDataStack
class ReplaceStackNameHere(Stack):
    def __init__(self, scope: Construct, construct_id: str, config: dict, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        project_name = config.project_name
        sandbox = config.sandbox
        environment = config.environment
        name_tag = f"{sandbox}-{environment}"