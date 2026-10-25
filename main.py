
from nemoguardrails import RailsConfig, LLMRails

config = RailsConfig.from_path("config")
rails = LLMRails(config)

response = rails.generate(
    messages=[
        {
            "role": "user",
            "content": "Explain Python functions"
        }
    ]
)

print(response["content"])
