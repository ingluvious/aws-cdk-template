# Welcome to your Custom CDK Python Project Template!

This is a template project for CDK development with Python made by DL
The `cdk.json` file tells the CDK Toolkit how to execute your app.

# Steps to setup your Project

1. Clone this repo and detach it from GitHub
2. Replace cdk_StackNameHere.py with your actual stack project name like `cdk_UpsertTestData.py`
3. Within the cdk_StackNameHere.py file, rename the class to an actual name like `UpsertTestDataCDK` and make sure you import the stack file correctly in app.py
4. Run the file setup.py with the command `python3 -m setup` (This assumes you haven npm installed)
5. Run the command `source .venv/bin/activate` to activate your python environment
6. In the .env file, append the correct AWS_ACCOUNT and REGION variable values

# Project Description

Put a description of the project here!

To add additional dependencies, for example other CDK libraries, just add
them to your `requirements.txt` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation  (https://docs.aws.amazon.com/cdk/api/v2/)