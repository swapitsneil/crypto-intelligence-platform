from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_market_report(prompt):

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"ERROR: {str(e)}"


if __name__ == "__main__":

    prompt = """
    Market Health: Bullish

    Positive Coins: 60

    Negative Coins: 40

    Total Market Cap: 2.5 Trillion

    Total Volume: 100 Billion

    Generate a short market report.
    """

    print(
        generate_market_report(prompt)
    )