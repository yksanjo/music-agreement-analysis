import os
import openai
import logging
from dotenv import load_dotenv
from typing import Dict

# Load API key from environment variables or a .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Set up OpenAI API key
openai.api_key = api_key

# Setup logging
logging.basicConfig(level=logging.INFO)

class AISimulator:
    def __init__(self):
        self.negotiation_scenario: Dict[str, str] = {
            'offer': 'Record Label offers $100,000',
            'bargaining_power': 'Musician has a strong fan base and multiple offers from other labels',
        }
        self.music_executive_persona = {
            "role": "Experienced music industry executive",
            "skills": [
                "Excellent talent-spotting and nurturing abilities",
                "Comprehensive understanding of the music industry",
                "Successful record of negotiating contracts for artists",
                "Keen sense for the latest trends and opportunities in the music business"
            ],
            "traits": [
                "Adaptable to the changing dynamics of the music industry",
                "Proven success in propelling artists' careers",
                "Strives for excellence in all aspects of the music industry"
            ],
            "description": "I am an experienced executive in the music industry, with a track record of identifying and nurturing talent. My comprehensive understanding of the industry dynamics has enabled me to successfully negotiate numerous contracts, aligning artists with opportunities that propel their careers. My ability to identify and leverage the latest trends has helped me navigate the ever-changing landscape of the music business, ensuring success for the artists and businesses I represent."
        }

    def start_game(self):
        logging.info("Hello! I am your AI music executive simulator. Let me start off by saying I love your music and I'm interested in doing a record deal with you.")
        logging.info("Tell me about your journey through music so far.")

        while True:
            # Get player's response through user input
            player_response = input("Enter your response: ")

            if player_response.lower() in ['exit', 'quit']:
                logging.info("Exiting the game...")
                break
            else:
                # Generate AI response using OpenAI API
                try:
                    ai_response = self.generate_ai_response(player_response)
                    logging.info("AI Response: %s", ai_response)
                except Exception as e:
                    logging.error("An error occurred while generating AI response: %s", e)

    def generate_ai_response(self, player_response: str) -> str:
        message = {
            "role": "user",
            "content": f"As a {self.music_executive_persona['role']}, with skills like {', '.join(self.music_executive_persona['skills'])}, and traits like {', '.join(self.music_executive_persona['traits'])}, I can say: {self.music_executive_persona['description']}. Player says: {player_response}",
        }
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[message]
            )
            ai_response = response.choices[0].message.content
            return ai_response
        except Exception as e:
            logging.error("An error occurred while generating AI response: %s", e)
            raise e

# Start the game
game = AISimulator()

# Start the negotiation
game.start_game()

