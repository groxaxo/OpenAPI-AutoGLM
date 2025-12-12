# Using Custom OpenAI-Compatible Models

Phone Agent supports **any OpenAI-compatible API with vision capabilities**, allowing you to bring your own LLM models from various providers.

## Supported Providers

Any provider that implements the OpenAI Chat Completions API format with vision support can be used, including:

### Commercial Providers
- **OpenAI** - GPT-4 Vision, GPT-4o, GPT-4 Turbo with vision
- **Azure OpenAI Service** - Vision-enabled deployments
- **Anthropic** (via compatibility layers)
- **Google AI** (via compatibility layers)
- And many others...

### Self-Hosted Solutions
- **vLLM** - High-performance inference server
- **SGLang** - Fast serving framework
- **LiteLLM** - Unified API for multiple providers
- **text-generation-webui** - With OpenAI extension
- **LocalAI** - Local OpenAI-compatible server
- **Ollama** (with OpenAI-compatible mode)

## Requirements for Custom Models

Your model/endpoint must support:

1. ✅ **OpenAI Chat Completions API format** (`/v1/chat/completions`)
2. ✅ **Vision input** - Multimodal (text + images)
3. ✅ **Base64-encoded images** in message content
4. ✅ **Structured output** - Ability to follow instructions and output formatted responses

## Configuration Examples

### OpenAI GPT-4 Vision

```python
from phone_agent import PhoneAgent
from phone_agent.model import ModelConfig

model_config = ModelConfig(
    base_url="https://api.openai.com/v1",
    api_key="sk-your-openai-api-key",
    model_name="gpt-4o",  # or "gpt-4-vision-preview", "gpt-4-turbo"
    temperature=0.1,
)

agent = PhoneAgent(model_config=model_config)
```

**Command line:**
```bash
python main.py \
  --base-url https://api.openai.com/v1 \
  --model gpt-4o \
  --apikey sk-your-openai-api-key \
  "Open Chrome browser"
```

### Azure OpenAI

```python
model_config = ModelConfig(
    # Azure uses a different URL format
    base_url="https://YOUR_RESOURCE_NAME.openai.azure.com/openai/deployments/YOUR_DEPLOYMENT_NAME",
    api_key="your-azure-api-key",
    model_name="gpt-4-vision-preview",
    extra_body={"api-version": "2024-02-15-preview"},
)

agent = PhoneAgent(model_config=model_config)
```

**Command line:**
```bash
python main.py \
  --base-url https://YOUR_RESOURCE.openai.azure.com/openai/deployments/YOUR_DEPLOYMENT \
  --model gpt-4-vision-preview \
  --apikey your-azure-api-key \
  "Open Chrome browser"
```

### LiteLLM Proxy

LiteLLM allows you to use 100+ LLMs with an OpenAI-compatible interface.

```python
model_config = ModelConfig(
    base_url="http://localhost:4000",  # LiteLLM proxy URL
    api_key="your-litellm-key",
    model_name="claude-3-opus-20240229",  # or any model supported by LiteLLM
)

agent = PhoneAgent(model_config=model_config)
```

### text-generation-webui with OpenAI Extension

```python
model_config = ModelConfig(
    base_url="http://localhost:5000/v1",
    api_key="EMPTY",  # No auth required for local
    model_name="your-local-vision-model",
)

agent = PhoneAgent(model_config=model_config)
```

### LocalAI

```python
model_config = ModelConfig(
    base_url="http://localhost:8080/v1",
    api_key="EMPTY",
    model_name="llava",  # or other vision models
)

agent = PhoneAgent(model_config=model_config)
```

## Environment Variables

You can configure the model using environment variables:

```bash
export PHONE_AGENT_BASE_URL="https://api.openai.com/v1"
export PHONE_AGENT_MODEL="gpt-4o"
export PHONE_AGENT_API_KEY="sk-your-api-key"

# Then run without specifying arguments
python main.py "Open Chrome browser"
```

## Performance Considerations

### AutoGLM vs. General-Purpose Models

- **AutoGLM models** are specifically fine-tuned for:
  - Understanding mobile UI layouts
  - Screen element detection and localization
  - Action planning for phone automation tasks
  - Efficient multi-step task execution

- **General-purpose vision models** (like GPT-4V):
  - May work but could be less accurate
  - Might require more steps to complete tasks
  - May have higher API costs
  - Could struggle with UI element localization

### Recommendations

1. **For best results**: Use AutoGLM models when available
2. **For experimentation**: Try GPT-4 Vision or other providers
3. **For cost-effectiveness**: Consider self-hosted solutions
4. **For production**: Benchmark different models on your specific use cases

## Troubleshooting

### Model doesn't understand the task

**Problem**: The model outputs random text or doesn't follow the expected format.

**Solution**:
- Ensure your model supports vision input
- Check that the model can process base64-encoded images
- Try adjusting the temperature (lower = more deterministic)
- Verify the model understands the system prompt format

### API connection errors

**Problem**: Cannot connect to the API endpoint.

**Solution**:
- Verify the `base_url` is correct (should end with `/v1`)
- Check your API key is valid
- Ensure network connectivity to the endpoint
- For Azure, verify the URL format matches the deployment

### Images not being processed

**Problem**: Model responds but ignores the screenshots.

**Solution**:
- Confirm the model supports multimodal input (vision)
- Check the model's image size limits
- Verify the API endpoint supports image_url in message content

### Poor performance on phone tasks

**Problem**: Model completes tasks but inefficiently or incorrectly.

**Solution**:
- Consider using AutoGLM models optimized for phone automation
- Adjust the system prompt for your specific model
- Fine-tune temperature and other parameters
- Provide more specific task descriptions

## API Compatibility Testing

To test if your endpoint is compatible:

```python
from phone_agent.model import ModelClient, ModelConfig
from phone_agent.model.client import MessageBuilder

# Configure your endpoint
config = ModelConfig(
    base_url="your-endpoint-url",
    api_key="your-api-key",
    model_name="your-model-name",
)

# Create client
client = ModelClient(config)

# Test with a simple vision request
messages = [
    MessageBuilder.create_system_message("You are a helpful assistant."),
    MessageBuilder.create_user_message(
        text="What's in this image?",
        image_base64="iVBORw0KG..."  # Your base64 image
    ),
]

try:
    response = client.request(messages)
    print(f"Success! Model response: {response.raw_content}")
except Exception as e:
    print(f"Error: {e}")
```

## Advanced Configuration

### Custom Parameters

Use `extra_body` for provider-specific parameters:

```python
model_config = ModelConfig(
    base_url="https://api.example.com/v1",
    api_key="your-key",
    model_name="custom-vision-model",
    extra_body={
        "custom_param": "value",
        "another_param": 123,
    }
)
```

### Timeout and Retry

Configure request timeouts by modifying the OpenAI client:

```python
from phone_agent.model import ModelClient, ModelConfig
from openai import OpenAI

config = ModelConfig(
    base_url="https://api.example.com/v1",
    api_key="your-key",
    model_name="your-model",
)

client = ModelClient(config)
# Access the underlying OpenAI client for advanced configuration
client.client = OpenAI(
    base_url=config.base_url,
    api_key=config.api_key,
    timeout=60.0,  # 60 seconds timeout
    max_retries=3,
)
```

## Need Help?

- Check the [main documentation](../README_en.md) for general setup
- See [examples/openai_compatible_models.py](../examples/openai_compatible_models.py) for complete code examples
- Report issues on [GitHub Issues](https://github.com/zai-org/Open-AutoGLM/issues)

## Contributing

Have you successfully used Phone Agent with a new provider? Please consider:
- Sharing your configuration
- Contributing to the documentation
- Reporting compatibility issues
