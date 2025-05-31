import os
import aws_cdk as cdk
from dotenv import load_dotenv
from stack.cdk_StackNameHere import ReplaceStackNameHere
from config.setup_stack import setup_stack

load_dotenv(".env", override=True)

#Specify the Environment that you want to deploy the stack to
env = "dev"
# env = "qat"
# env = "zen"

app = cdk.App()

# Stack for the SQS and Response Lambda
setup_stack(env, app, "PROJECT_NAME", ReplaceStackNameHere)

app.synth()