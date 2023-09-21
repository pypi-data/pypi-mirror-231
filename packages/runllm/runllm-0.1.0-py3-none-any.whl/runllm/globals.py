from runllm.backend.api_client import APIClient

current_task = None

# Initialize an unconfigured api client. It will be configured when the user construct a runllm client.
__GLOBAL_API_CLIENT__ = APIClient()
