import os
from dotenv import load_dotenv

load_dotenv(".env", override=True)

class StackEnvConfig:
    def __init__(self, sandbox, client_id, client_secret, environment, project_name, auth_token):
        self.aws_account = os.getenv("AWS_ACCOUNT")
        self.region = os.getenv("REGION")
        self.sandbox = sandbox
        self.environment = environment
        self.project_name = project_name
        self.stack_name = f"{project_name}-{sandbox}-{environment}"
        self.name_tag = f"{sandbox}-{environment}"
        self.service_secrets_manager = "secretsmanager"
        self.service_s3 = "s3"

        self.client_id = client_id
        self.client_secret = client_secret

        self.sandbox_url = f"{os.getenv("BASE_URL")}{sandbox}{os.getenv("BASE_URL_END")}"
        self.path_auth_url = os.getenv("PATH_AUTH_URL")
    
        self.api_version = os.getenv("API_VERSION")
        self.path_services = os.getenv("PATH_SERVICES")
        self.path_data = os.getenv("PATH_DATA")
        self.path_sobjects = os.getenv("PATH_SOBJECTS")
        self.path_batches = os.getenv("PATH_BATCHES")
        self.path_jobs = os.getenv("PATH_JOBS")
        self.path_ingest = os.getenv("PATH_INGEST")
        self.path_results_success = os.getenv("PATH_RESULTS_SUCCESS")
        self.path_results_fail = os.getenv("PATH_RESULTS_FAIL")
        self.path_query = os.getenv("PATH_QUERY")

class stackConfig:
    def __init__(self, project_name):
        self.dev = StackEnvConfig(
            sandbox="deving",
            client_id=os.getenv(""),
            client_secret=os.getenv(""),
            environment="test",
            project_name=project_name,
            auth_token=os.getenv("")
        )
        self.qat = StackEnvConfig(
            sandbox="qat",
            client_id=os.getenv(""),
            client_secret=os.getenv(""),
            environment="test",
            project_name=project_name,
            auth_token=os.getenv("")
        )
        self.zen = StackEnvConfig(
            sandbox="qat",
            client_id=os.getenv(""),
            client_secret=os.getenv(""),
            environment="zen",
            project_name=project_name,
            auth_token=os.getenv("")
        )

stack_config = {
    # SQS Stack Config Values
    os.getenv("PROJECT_NAME"): stackConfig(
        project_name=os.getenv("PROJECT_NAME")
    )
}

