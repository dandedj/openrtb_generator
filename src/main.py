
import json
from chatgpt.OpenRTBGenerator import OpenRTBGenerator
import os

if __name__ == "__main__":
    generator = OpenRTBGenerator()
    
    NUM_REQUESTS = 10
    NUM_RESPONSES = 10
    
    # Create directories if they don't exist
    if not os.path.exists("requests"):
        os.makedirs("requests")
    if not os.path.exists("responses"):
        os.makedirs("responses")

    # Clear out previous data
    for file in os.listdir("requests"):
        os.remove(os.path.join("requests", file))
    for file in os.listdir("responses"):
        os.remove(os.path.join("responses", file))

    # Generate request payloads and write to individual json files
    for i in range(NUM_REQUESTS):
        request_payload = generator.generate_bid_request()
        with open(f"requests/request_{i+1}.json", "w") as f:
            json.dump(request_payload, f, ensure_ascii=False)

    # Generate response payloads and write to individual json files
    for i in range(NUM_RESPONSES):
        response_payload = generator.generate_bid_response()
        with open(f"responses/response_{i+1}.json", "w") as f:
            json.dump(response_payload, f, ensure_ascii=False)
