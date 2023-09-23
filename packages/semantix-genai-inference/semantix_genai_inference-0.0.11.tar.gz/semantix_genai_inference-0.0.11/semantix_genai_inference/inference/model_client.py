import os
import yaml
from semantix_genai_inference.inference.llm.alpaca import AlpacaInferenceClient
from semantix_genai_inference.inference.llm.llama2 import Llama2InferenceClient
from semantix_genai_inference.inference.llm.cohere import CohereInferenceClient
from semantix_genai_inference.inference.llm.openai import OpenAIInferenceClient
from semantix_genai_inference.inference.llm.azure_openai import AzureOpenAIInferenceClient

class ModelClient:

    @staticmethod
    def create(client_type):
        """
        Create a client for a given model type and inference server id
        
        Args:
            client_type (str): The type of model client to create. Valid options are "alpaca", "llama2", "cohere"
        """
        config = ModelClient()._load_config()
        if client_type == "alpaca":
            semantix = config["providers"]["semantixHub"]
            inference_server_id = semantix["serverId"]
            api_secret = semantix["apiSecret"] if "apiSecret" in semantix else None
            version = semantix["version"]
            return AlpacaInferenceClient(inference_server_id, api_secret, version=version)
        elif client_type == "llama2":
            semantix = config["providers"]["semantixHub"]
            inference_server_id = semantix["serverId"]
            api_secret = semantix["apiSecret"] if "apiSecret" in semantix else None
            version = semantix["version"]
            return Llama2InferenceClient(inference_server_id, api_secret, version=version)
        elif client_type == "cohere":
            cohere = config["providers"]["cohere"]
            api_key = cohere["apiKey"] if "apiKey" in cohere else None
            generate_model = cohere["generate"]["model"]
            version = cohere["generate"]["version"]
            return CohereInferenceClient(api_key, generate_model, version=version)
        elif client_type == "openai":
            openai = config["providers"]["openai"]
            api_key = openai["apiKey"] if "apiKey" in openai else None
            model = openai["chat"]["model"]
            version = openai["chat"]["version"]
            return OpenAIInferenceClient(api_key, model, version=version)
        elif client_type == "azure-openai":
            azure_openai = config["providers"]["azureOpenai"]
            api_key = azure_openai["apiKey"] if "apiKey" in azure_openai else None
            host = azure_openai["chat"]["apiBase"]
            deployment_id = azure_openai["chat"]["deploymentId"]
            api_version = azure_openai["chat"]["apiVersion"]
            return AzureOpenAIInferenceClient(host, deployment_id, api_version, api_key=api_key)
        else:
            raise Exception(f"Invalid model client type: {client_type}")
    
    def _load_config(self):
        """
        Load the semantix.yaml file from the same directory where the application was executed
        """
        # check if SEMANTIX_CONFIG_FILE env exists otherwise use default
        config_file = "semantix.yaml"
        if "SEMANTIX_CONFIG_FILE" in os.environ:
            config_file = os.environ["SEMANTIX_CONFIG_FILE"]
        # check if file exists
        if not os.path.isfile(config_file):
            raise Exception(f"No {config_file} file found. The model client factory will not work, you may work instantiating the models directly.")

    def _update_config_with_env(self, config, env_vars):
        for provider, settings in env_vars.items():
            config["providers"].setdefault(provider, {})
            for key, env_var in settings.items():
                if isinstance(env_var, dict):
                    config["providers"][provider].setdefault(key, {})
                    for sub_key, sub_env_var in env_var.items():
                        config["providers"][provider][key].setdefault(sub_key, os.environ.get(sub_env_var))
                else:
                    config["providers"][provider].setdefault(key, os.environ.get(env_var))

    def _load_config(self):
        config_file = "semantix.yaml"
        if "SEMANTIX_CONFIG_FILE" in os.environ:
            config_file = os.environ["SEMANTIX_CONFIG_FILE"]

        config = {}
        if os.path.isfile(config_file):
            with open(config_file) as f:
                config = yaml.safe_load(f)

        config.setdefault("providers", {})
        env_vars = {
            "semantixHub": {
                "serverId": "SEMANTIX_SERVER_ID",
                "apiSecret": "SEMANTIX_API_SECRET",
                "version": "SEMANTIX_VERSION"
            },
            "cohere": {
                "apiKey": "COHERE_API_KEY",
                "generate": {
                    "model": "COHERE_GENERATE_MODEL",
                    "version": "COHERE_GENERATE_VERSION"
                }
            },
            "openai": {
                "apiKey": "OPENAI_API_KEY",
                "chat": {
                    "model": "OPENAI_CHAT_MODEL",
                    "version": "OPENAI_CHAT_VERSION"
                }
            },
            "azureOpenai": {
                "apiKey": "AZURE_OPENAI_API_KEY",
                "chat": {
                    "apiBase": "AZURE_OPENAI_CHAT_API_BASE",
                    "deploymentId": "AZURE_OPENAI_CHAT_DEPLOYMENT_ID",
                    "apiVersion": "AZURE_OPENAI_CHAT_API_VERSION"
                }
            }
        }
        self._update_config_with_env(config, env_vars)
        return config
