from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from backend import ask_ai

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>TechFlow AI</title>

        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">

        <style>
            body {
                margin: 0;
                font-family: 'Inter', sans-serif;
                background: linear-gradient(135deg, #eef2ff, #f8fafc);
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }

            .container {
                background: white;
                padding: 40px;
                border-radius: 16px;
                width: 500px;
                text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            }

            h1 {
                margin-bottom: 10px;
                font-weight: 600;
                font-size: 28px;
            }

            p {
                color: #6b7280;
                margin-bottom: 25px;
                font-size: 15px;
            }

            input {
                width: 100%;
                padding: 14px;
                border-radius: 10px;
                border: 1px solid #d1d5db;
                font-size: 15px;
                margin-bottom: 20px;
                outline: none;
            }

            input:focus {
                border-color: #6366f1;
                box-shadow: 0 0 0 2px rgba(99,102,241,0.2);
            }

            button {
                width: 100%;
                padding: 14px;
                background: #6366f1;
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 16px;
                font-weight: 500;
                cursor: pointer;
                transition: 0.2s;
            }

            button:hover {
                background: #4f46e5;
            }

            .tag {
                display: inline-block;
                background: #eef2ff;
                color: #4f46e5;
                padding: 5px 10px;
                border-radius: 6px;
                font-size: 12px;
                margin-bottom: 15px;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <div class="tag">AI Powered Sourcing Tool</div>

            <h1>TechFlow Order Form</h1>

            <p>Analyze contract risks, costs, and negotiation levers instantly</p>

            <form action="/ask" method="post">
                <input 
                    name="question" 
                    placeholder="Ask about risks, pricing, negotiation..." 
                    required
                >

                <button>Analyze</button>
            </form>

        </div>

    </body>
    </html>
    """

@app.post("/ask", response_class=HTMLResponse)
def ask(question: str = Form(...)):
    response = ask_ai(question)

    formatted = response.replace("\n", "<br>")

    return f"""
    <html>
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Inter&display=swap" rel="stylesheet">
        <style>
            body {{
                font-family: 'Inter', sans-serif;
                background:#f5f7fa;
                padding:40px;
            }}
        </style>
    </head>

    <body>
        <div style="background:white; padding:30px; border-radius:10px; max-width:800px; margin:auto;">
            <h2>AI Analysis</h2>
            <p><b>Question:</b> {question}</p>
            <hr>
            <div style="font-size:18px; line-height:1.8;">
                {formatted}
            </div>
            <br>
            <a href="/">← Back</a>
        </div>
    </body>
    </html>
    """