#!/usr/bin/env python3
"""
Examples of using Phone Agent with OpenAI-compatible vision models.

This demonstrates how to use various OpenAI-compatible API providers
with vision capabilities, including OpenAI GPT-4 Vision, Azure OpenAI,
and other custom endpoints.
"""

from phone_agent import PhoneAgent
from phone_agent.agent import AgentConfig
from phone_agent.model import ModelConfig


def example_openai_gpt4_vision():
    """Example using OpenAI GPT-4 Vision (GPT-4o)"""
    print("\n" + "=" * 60)
    print("Example: Using OpenAI GPT-4 Vision (GPT-4o)")
    print("=" * 60)

    # Configure OpenAI GPT-4 Vision
    model_config = ModelConfig(
        base_url="https://api.openai.com/v1",
        api_key="sk-REPLACE_WITH_YOUR_ACTUAL_API_KEY",  # Replace with your actual OpenAI API key
        model_name="gpt-4o",  # or "gpt-4-vision-preview", "gpt-4-turbo"
        temperature=0.1,
        max_tokens=3000,
    )

    # Configure Agent
    agent_config = AgentConfig(
        max_steps=50,
        verbose=True,
        lang="en",  # Use English prompts
    )

    # Create Agent
    agent = PhoneAgent(
        model_config=model_config,
        agent_config=agent_config,
    )

    # Execute task
    result = agent.run("Open Chrome and search for weather forecast")
    print(f"Result: {result}")


def example_azure_openai():
    """Example using Azure OpenAI Service with GPT-4 Vision"""
    print("\n" + "=" * 60)
    print("Example: Using Azure OpenAI Service")
    print("=" * 60)

    # Configure Azure OpenAI
    # Note: Azure uses a different URL format
    # Format: https://{resource-name}.openai.azure.com/openai/deployments/{deployment-name}
    model_config = ModelConfig(
        base_url="https://YOUR_RESOURCE_NAME.openai.azure.com/openai/deployments/YOUR_DEPLOYMENT_NAME",
        api_key="REPLACE_WITH_YOUR_ACTUAL_AZURE_API_KEY",  # Replace with your actual Azure API key
        model_name="gpt-4-vision-preview",  # Your Azure deployment model
        temperature=0.1,
        max_tokens=3000,
        # Azure-specific parameters can be added via extra_body
        extra_body={"api-version": "2024-02-15-preview"},
    )

    agent_config = AgentConfig(
        max_steps=50,
        verbose=True,
        lang="en",
    )

    agent = PhoneAgent(
        model_config=model_config,
        agent_config=agent_config,
    )

    result = agent.run("Open Gmail and check for new emails")
    print(f"Result: {result}")


def example_custom_openai_compatible():
    """Example using custom OpenAI-compatible endpoint"""
    print("\n" + "=" * 60)
    print("Example: Using Custom OpenAI-Compatible Endpoint")
    print("=" * 60)

    # This works with any OpenAI-compatible API, such as:
    # - Local LLMs via LiteLLM
    # - text-generation-webui with OpenAI extension
    # - vLLM or SGLang deployments
    # - Other third-party providers

    model_config = ModelConfig(
        base_url="http://localhost:8000/v1",  # Your custom endpoint
        api_key="REPLACE_WITH_YOUR_CUSTOM_API_KEY",  # Or "EMPTY" if no auth required
        model_name="your-vision-model-name",
        temperature=0.1,
        max_tokens=3000,
    )

    agent_config = AgentConfig(
        max_steps=50,
        verbose=True,
        lang="en",
    )

    agent = PhoneAgent(
        model_config=model_config,
        agent_config=agent_config,
    )

    result = agent.run("Open Maps and find nearby restaurants")
    print(f"Result: {result}")


def example_with_environment_variables():
    """Example using environment variables for configuration"""
    import os

    print("\n" + "=" * 60)
    print("Example: Using Environment Variables")
    print("=" * 60)

    # Set environment variables before running
    # export PHONE_AGENT_BASE_URL="https://api.openai.com/v1"
    # export PHONE_AGENT_MODEL="gpt-4o"
    # export PHONE_AGENT_API_KEY="sk-REPLACE_WITH_YOUR_ACTUAL_API_KEY"

    # Or set them programmatically for this example
    os.environ["PHONE_AGENT_BASE_URL"] = "https://api.openai.com/v1"
    os.environ["PHONE_AGENT_MODEL"] = "gpt-4o"
    os.environ["PHONE_AGENT_API_KEY"] = "sk-REPLACE_WITH_YOUR_ACTUAL_API_KEY"

    # ModelConfig will automatically use environment variables if not specified
    model_config = ModelConfig(
        base_url=os.getenv("PHONE_AGENT_BASE_URL", "http://localhost:8000/v1"),
        api_key=os.getenv("PHONE_AGENT_API_KEY", "EMPTY"),
        model_name=os.getenv("PHONE_AGENT_MODEL", "autoglm-phone-9b"),
    )

    agent_config = AgentConfig(verbose=True, lang="en")

    agent = PhoneAgent(
        model_config=model_config,
        agent_config=agent_config,
    )

    result = agent.run("Open Chrome browser")
    print(f"Result: {result}")


def example_comparing_models():
    """Example comparing different models on the same task"""
    print("\n" + "=" * 60)
    print("Example: Comparing Different Models")
    print("=" * 60)

    task = "Open Chrome and search for Python tutorials"

    # Test with AutoGLM (optimized for phone automation)
    print("\n--- Testing with AutoGLM ---")
    autoglm_config = ModelConfig(
        base_url="http://localhost:8000/v1",
        model_name="autoglm-phone-9b",
    )
    autoglm_agent = PhoneAgent(
        model_config=autoglm_config,
        agent_config=AgentConfig(max_steps=50, lang="en"),
    )
    autoglm_result = autoglm_agent.run(task)
    print(f"AutoGLM Result: {autoglm_result}")

    # Test with OpenAI GPT-4 Vision (general-purpose vision model)
    print("\n--- Testing with GPT-4 Vision ---")
    gpt4v_config = ModelConfig(
        base_url="https://api.openai.com/v1",
        api_key="sk-REPLACE_WITH_YOUR_ACTUAL_API_KEY",
        model_name="gpt-4o",
    )
    gpt4v_agent = PhoneAgent(
        model_config=gpt4v_config,
        agent_config=AgentConfig(max_steps=50, lang="en"),
    )
    gpt4v_result = gpt4v_agent.run(task)
    print(f"GPT-4V Result: {gpt4v_result}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Examples of using OpenAI-compatible vision models"
    )
    parser.add_argument(
        "--example",
        type=str,
        choices=[
            "openai",
            "azure",
            "custom",
            "env",
            "compare",
            "all",
        ],
        default="openai",
        help="Which example to run",
    )
    args = parser.parse_args()

    print("\n" + "=" * 60)
    print("Phone Agent - OpenAI-Compatible Models Examples")
    print("=" * 60)
    print("\nNOTE: Remember to replace API keys with your actual keys!")
    print("=" * 60)

    if args.example == "openai" or args.example == "all":
        try:
            example_openai_gpt4_vision()
        except Exception as e:
            print(f"Error: {e}")

    if args.example == "azure" or args.example == "all":
        try:
            example_azure_openai()
        except Exception as e:
            print(f"Error: {e}")

    if args.example == "custom" or args.example == "all":
        try:
            example_custom_openai_compatible()
        except Exception as e:
            print(f"Error: {e}")

    if args.example == "env" or args.example == "all":
        try:
            example_with_environment_variables()
        except Exception as e:
            print(f"Error: {e}")

    if args.example == "compare":
        try:
            example_comparing_models()
        except Exception as e:
            print(f"Error: {e}")

    print("\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)
