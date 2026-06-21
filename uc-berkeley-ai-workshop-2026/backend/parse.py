# backend/parse.py

import json
from ollama import chat

SYSTEM_PROMPT = """
You are a JSON intent parser for a cooking assistant.

Return ONLY JSON.

The only allowed actions are:

add_preference
generate_recipe
next_step
previous_step
repeat_step
add_timer
remove_timer
add_mistake
resolve_mistake
question

Never invent new action names.

"burned", "burnt", "spilled", "overcooked", "undercooked", "forgot" indicate add_mistake.

Timers must always use:

{
  "action":"add_timer",
  "timer_name":"Timer",
  "duration_seconds":<seconds>
}

Examples:

User: I burned the onions

{
 "actions":[
   {
     "action":"add_mistake",
     "description":"burned onions"
   }
 ]
}

User: I burnt onions

{
 "actions":[
   {
     "action":"add_mistake",
     "description":"burnt onions"
   }
 ]
}

User: Add 30 min timer

{
 "actions":[
   {
     "action":"add_timer",
     "timer_name":"Timer",
     "duration_seconds":1800
   }
 ]
}

User: Set a timer for 2 hours

{
 "actions":[
   {
     "action":"add_timer",
     "timer_name":"Timer",
     "duration_seconds":7200
   }
 ]
}

User: I love chicken but hate milk

{
 "actions":[
   {
     "action":"add_preference",
     "preference_type":"likes",
     "preference":"chicken"
   },
   {
     "action":"add_preference",
     "preference_type":"dislikes",
     "preference":"milk"
   }
 ]
}
"""

def parse_input(text: str):
    response = chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": text
            }
        ],
        format="json",
        think=False
    )

    try:
        return json.loads(response.message.content)
    except Exception:
      
        print(response.message.content) 
        # Testing
        
        return {"actions": []}

# Testing
# if __name__ == "__main__":

#     while True:
#         text = input("You: ")

#         parsed = parse_input(text)

#         print()
#         print(json.dumps(parsed, indent=2))
#         print()