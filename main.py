from mem0 import MemoryClient
from dotenv import load_dotenv
import os

load_dotenv()


# Initialize the client
client = MemoryClient(api_key=os.getenv("MEM0_API_KEY"))

'''
# Add memory
messages = [
    {"role": "user", "content": "Hi, I'm Alex. I'm a vegetarian and I'm allergic to nuts."},
    {"role": "assistant", "content": "Hello Alex! I've noted that you're a vegetarian and have a nut allergy. I'll keep this in mind for any food-related recommendations or discussions."}
]
res = client.add(messages, user_id="alex")
print(res)
print('\n')


# Retrieve memory
query = "What can I cook for dinner tonight?"
res = client.search(query, user_id="alex")
print(res)
'''

'''
# Long-term memory for a user

messages = [
    {"role": "user", "content": "Hi, I'm Alex. I'm a vegetarian and I'm allergic to nuts."},
    {"role": "assistant", "content": "Hello Alex! I've noted that you're a vegetarian and have a nut allergy. I'll keep this in mind for any food-related recommendations or discussions."}
]

# The default output_format is v1.0
r = client.add(messages, user_id="alex", output_format="v1.0")
print(r)

print('\n')

# To use the latest output_format, set the output_format parameter to "v1.1"
r = client.add(messages, user_id="alex", output_format="v1.1", metadata={"food": "vegan"})
print(r)


'''


'''
# Short-term memory for a user session

messages = [
    {"role": "user", "content": "I'm planning a trip to Japan next month."},
    {"role": "assistant", "content": "That's exciting, Alex! A trip to Japan next month sounds wonderful. Would you like some recommendations for vegetarian-friendly restaurants in Japan?"},
    {"role": "user", "content": "Yes, please! Especially in Tokyo."},
    {"role": "assistant", "content": "Great! I'll remember that you're interested in vegetarian restaurants in Tokyo for your upcoming trip. I'll prepare a list for you in our next interaction."}
]

# The default output_format is v1.0
r = client.add(messages, user_id="alex123", run_id="trip-planning-2024", output_format="v1.0")
print(r)

print('\n')

# To use the latest output_format, set the output_format parameter to "v1.1"
r = client.add(messages, user_id="alex123", run_id="trip-planning-2024", output_format="v1.1")
print(r)

'''


'''
# Long-term memory for agents
messages = [
    {"role": "system", "content": "You are an AI tutor with a personality. Give yourself a name for the user."},
    {"role": "assistant", "content": "Understood. I'm an AI tutor with a personality. My name is Alice."}
]

# The default output_format is v1.0
r = client.add(messages, agent_id="ai-tutor", output_format="v1.0")
print(r)

print('\n')


# To use the latest output_format, set the output_format parameter to "v1.1"
client.add(messages, agent_id="ai-tutor", output_format="v1.1")
print(r)

'''

'''# General Memory Search

query = "What should I cook for dinner today?"

# The default output_format is v1.0
r = client.search(query, user_id="alex", output_format="v1.0")
print(r)

print('\n')

# To use the latest output_format, set the output_format parameter to "v1.1"
r = client.search(query, user_id="alex", output_format="v1.1")
print(r)

'''

'''
query = "What do you know about me?"
filters = {
   "AND":[
      {
         "user_id":"alex"
      },
      {
         "agent_id":{
            "in":[
               "travel-assistant",
               "customer-support",
                "ai-tutor"
            ]
         }
      }
   ]
}
r = client.search(query, version="v2", filters=filters)

print(r)
'''

# r = client.users()
# print(r)


# # Add some message to create history
# messages = [{"role": "user", "content": "I recently tried chicken and I loved it. I'm thinking of trying more non-vegetarian dishes.."}]
# client.add(messages, user_id="alex")

# # Add second message to update history
# messages.append({'role': 'user', 'content': 'I turned vegetarian now.'})
# client.add(messages, user_id="alex")


memory_id = "871d5574-9ee8-407d-9cba-1043185072eb"
history = client.history(memory_id)
print(history)