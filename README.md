**README.md (Project Root)**

```markdown
# Ancestry Explorer

A conversational AI agent application powered by your family history data and external knowledge. Explore your ancestry dynamically through chat.

## Features (MVP)

- User Authentication (Signup, Login)
- Subscription Management (via Stripe - Placeholder integration initially)
- GEDCOM File Upload and Parsing
- AI Chat Agent powered by LangChain and Gemini Flash
- Agent can answer questions about your family tree using your data.
- Agent can find and link to relevant information on Wikipedia.
- Agent can find and link to relevant highly-rated historical videos on YouTube.
- Agent can handle simple updates to your profile (e.g., adding haplogroups).
- Conversational Memory: Agent remembers previous parts of the conversation.

## Technologies Used

- **Backend:** Python (FastAPI), SQLite, SQLAlchemy, LangChain, Gemini Flash API, Stripe API
- **Frontend:** React (or Vue), npm/yarn, axios
- **Deployment (Initial):** Single Server, Uvicorn, potentially Nginx/Caddy

## Setup Instructions (Development)

Follow these steps to get the project running on your local machine.

1.  **Prerequisites:**
    *   Git
    *   Python 3.8+
    *   Node.js & npm (or yarn)
    *   API Keys for Gemini Flash and Stripe (get these from the respective developer dashboards)

2.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd ancestry_explorer
    ```

3.  **Backend Setup:**
    *   Navigate to the backend directory: `cd backend`
    *   Create and activate a Python virtual environment: `python -m venv venv` and `source venv/bin/activate` (Linux/macOS) or `.\venv\Scripts\activate` (Windows)
    *   Install backend dependencies: `pip install -r requirements.txt`
    *   Create a `.env` file: Copy the contents from `.env.example` (you'll need to create this file yourself with placeholder values initially) and replace with your actual API keys and secrets. **Ensure `.env` is in your project's `.gitignore`!**
    *   Initialize the database: You might need a script or a command to create the SQLite tables. Check the `backend/database/` directory for instructions or a runnable script (e.g., `python init_db.py` if you create one).

4.  **Frontend Setup:**
    *   Navigate to the frontend directory: `cd ../frontend`
    *   Install frontend dependencies: `npm install` (or `yarn install`)

5.  **Running the Application:**
    *   **Start Backend:** With the backend virtual environment active, run `uvicorn main:app --reload` from the `backend` directory. The API should be available at `http://127.0.0.1:8000`.
    *   **Start Frontend:** From the `frontend` directory, run `npm start` (or `yarn start`). The React app should open in your browser, usually at `http://localhost:3000`.

## Project Structure

(Include the detailed folder/file structure description from the planning phase here)

## Development Plan

Refer to the `DEVELOPMENT_PLAN.md` file for the detailed step-by-step build and testing plan.

## Contributing

(Placeholder for contribution guidelines)

## License

(Choose and add a license)
```

---