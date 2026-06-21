# session.py

session = {

    # throughout the recipe stay same
    "preferences": {
        "diet": [],          # ["vegetarian", "vegan"]
        "dislikes": []       # ["mushrooms", "olives"]
    },

    # recipe session
    "recipe": {

        # recipe info
        "name": None,
        "start_time": None,
        "expected_end_time": None,

        # card/page is currently being displayed
        "current_step": 0,

        # list of all cards/pages
        "cards": [

            # Example card
            # {
            #     "step_number": 0,
            #     "title": "Mix Ingredients",
            #     "instruction":
            #         "Mix flour, sugar, and cocoa powder.",
            #
            #     # Whether to display timer UI
            #     "is_timer_card": False,
            #
            #     # Duration for this step
            #     "duration_seconds": 120,
            #
            #     # Filled in when user reaches this card
            #     "step_start_time": None,
            #     "expected_step_end_time": None
            # }

        ]
    },

    # active timers
    "timers": [

        # Example:
        # {
        #     "name": "Bake Cookies",
        #     "end_time": 1719444000
        # }

    ],

    # mistakes made during cooking
    "mistakes": [

        # Example:
        # {
        #     "step_number": 2,
        #     "description": "Burned butter",
        #     "resolved": False
        # }

    ],

    # conversation history (optional, useful later)
    "history": [

        # Example:
        # {
        #     "role": "user",
        #     "content": "I burned the butter"
        # }

    ]
}