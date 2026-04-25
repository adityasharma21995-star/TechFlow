from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def ask_ai(question):
    try:
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            return "ERROR: API key missing"

        client = OpenAI(api_key=api_key)

        prompt = f"""
You are a senior procurement consultant.

Understand the user's question and respond ONLY to that category.

DO NOT give all sections.
DO NOT add extra categories.
Be precise and relevant.

---

POSSIBLE CATEGORIES:

1. Risks
2. Financial Risks
3. Legal Risks
4. Negotiation Levers
5. Sourcing Strategy
6. Cost / TCO

Identify which category the user is asking about and answer ONLY that.

---

CONTRACT:

- Subscription: $180K
- Implementation: $15K 
- Uplift: 10% (next year onwards, calculated only on Subscription fee progressively)
- SLA: 99.5%
- Payment: Net 15 upfront
- Professional Services: Uncapped
- Support: No 24/7
- Liability: 12 months cap
- Arbitration: Vendor-favorable
- Data protection: Weak

---

OUTPUT RULES:

- Bullet points only
- Max 5 bullets
- 1 line per bullet
- No explanation
- No repetition
- No headings like "Here are..."

---

QUESTION: {question}
"""

        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt,
            max_output_tokens=200
        )

        return response.output_text.strip()

    except Exception as e:
        return f"ERROR: {str(e)}"