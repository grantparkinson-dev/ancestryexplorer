Roger and Grant, opting for FastAPI and React is an excellent choice! FastAPI provides high performance and developer-friendly features for the backend API, while React offers a widely-used and flexible approach for building the interactive frontend. This is a robust and maintainable stack for your project.

Let's address the mobile app publishing question first, then dive into the detailed setup instructions and development plan.

**Publishing as an App on Apple or Android (with this stack)**

It's wise to consider the future, and understanding the path to mobile is important without letting it derail your current focus on the web application.

Your current stack (FastAPI, React, SQLite for the backend; React for the frontend rendered in a browser) is fundamentally designed for a **web application**. This means users will access your service through a web browser on their computers or mobile devices.

To have a native app experience on Apple (iOS) or Android, you have a few primary paths, none of which involve directly converting your current web stack into a native app:

1.  **Building Native Clients:** You would need to develop entirely separate applications using native mobile development languages and frameworks (Swift/UIKit/SwiftUI for iOS, Kotlin/Java/Jetpack Compose for Android). These native apps would then communicate with your existing **FastAPI backend API**. This is the most labor-intensive but offers the best performance and deepest integration with device features.
2.  **Cross-Platform Development:** Use frameworks like **React Native** (since you're already using React) or Flutter. These allow you to write code once (mostly) and deploy to both iOS and Android. Like native apps, these cross-platform apps would communicate with your **FastAPI backend API**. React Native would leverage your existing React knowledge but still requires learning mobile-specific components and APIs.
3.  **Hybrid/Wrapper Apps:** Use tools like **Capacitor** (by the Ionic team) or Cordova to wrap your existing React web application within a native container. This essentially runs your web app in a fullscreen web view on the device. It's the quickest way to get *an icon* on the home screen, but the performance and access to native device features are limited compared to native or true cross-platform approaches. It's still fundamentally a web app running inside a shell.

**In summary: Your current stack builds a web application.** Publishing a true native app requires a separate development effort using native or cross-platform mobile technologies that would connect to your existing FastAPI backend API. The simplest future step *might* be a hybrid wrapper app, but don't confuse it with a native experience.

This confirms that your current plan to build a web application is distinct from mobile app development, and you can proceed with confidence on the web path knowing what a potential mobile future would entail.

---

**Project: Ancestry Explorer - Development Plan (FastAPI & React)**

This plan outlines the steps to set up your development environment from scratch and build the core components incrementally, following the principle of getting the simplest piece working before moving to the next.

**Technologies in Use:**

*   **Backend:** Python 3.x, FastAPI, Uvicorn, SQLAlchemy (for SQLite ORM), python-dotenv, requests, google-generativeai (or openai if preferred for Gemini API access), python-stripe.
*   **Frontend:** Node.js, npm or yarn, React, react-dom, axios (for API calls).
*   **Database:** SQLite (via SQLAlchemy).
*   **AI:** LangChain, Gemini Flash API.
*   **Payments:** Stripe API.

**Development Environment Setup (From Scratch):**

This assumes a standard development machine (Windows, macOS, or Linux).

1.  **Install Git:** If you don't have Git installed, download and install it from [https://git-scm.com/](https://git-scm.com/).
2.  **Install Python 3.x:** Download and install the latest version of Python 3.x from [https://www.python.org/downloads/](https://www.python.org/downloads/). Make sure to check the option to add Python to your PATH during installation on Windows.
3.  **Install Node.js and npm/yarn:** Download and install Node.js (which includes npm) from [https://nodejs.org/](https://nodejs.org/). We recommend installing an LTS (Long-Term Support) version. You can optionally install yarn (`npm install -g yarn`).
4.  **Clone the Project Repository:** Create a directory for your project. Navigate into this directory in your terminal and clone your Git repository (once you create it).
    ```bash
    mkdir ancestry_explorer
    cd ancestry_explorer
    git init # Or git clone <your_repo_url>
    ```
5.  **Set up Backend Virtual Environment:** Navigate into the `backend` directory. Create a Python virtual environment to isolate project dependencies.
    ```bash
    cd backend
    python -m venv venv
    ```
6.  **Activate Backend Virtual Environment:**
    *   On macOS/Linux: `source venv/bin/activate`
    *   On Windows: `.\venv\Scripts\activate`
    (You'll need to activate this environment every time you work on the backend).
7.  **Create Backend Requirements File:** Create `backend/requirements.txt` and add the core dependencies:
    ```
    fastapi
    uvicorn[standard]
    sqlalchemy
    python-dotenv
    requests
    google-generativeai # Or openai
    stripe
    langchain
    ```
8.  **Install Backend Dependencies:** With the virtual environment active, install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
9.  **Create Frontend Project:** Navigate back to the root `ancestry_explorer` directory and create the frontend project using Create React App or Vite (a faster alternative often used with React). Using Vite for React:
    ```bash
    cd .. # Go back to ancestry_explorer root
    npm create vite@latest frontend --template react
    cd frontend
    npm install # Or yarn install
    ```
10. **Create Backend `.env` File:** In the `backend` directory, create a file named `.env`. This will store your sensitive API keys and secrets. Add placeholder values for now. **Crucially, add `.env` to your `.gitignore` file in the project root.**
    ```
    # backend/.env
    GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
    STRIPE_SECRET_KEY="YOUR_STRIPE_SECRET_KEY"
    DATABASE_URL="sqlite:///../data/genealogy.db" # Path relative to backend/
    SECRET_KEY="SOME_RANDOM_SECRET_KEY" # For session management etc.
    ```
11. **Create Project `.gitignore`:** In the root `ancestry_explorer` directory, create a `.gitignore` file to specify files and folders that Git should ignore.
    ```
    # .gitignore
    venv/
    __pycache__/
    *.pyc
    .env
    data/genealogy.db
    node_modules/
    build/ # For frontend build output
    dist/ # For frontend build output (Vite)
    ```

**Incremental Installation and Testing Plan (Leading to MVP):**

This plan breaks down the Phase 1 tasks into smaller, testable steps.

**Step 1: Basic Backend Server**

*   **Goal:** Get a simple FastAPI server running that responds to a basic request.
*   **Install:** Already done in environment setup.
*   **Code:**
    *   In `backend/main.py`: Create a basic `FastAPI` app instance and define a simple root endpoint (`@app.get("/")`) that returns a "Hello World" or similar message.
*   **Test:** Activate the backend virtual environment (`cd backend && source venv/bin/activate`), run the server (`uvicorn main:app --reload`), and access `http://127.0.0.1:8000/` in your browser or using `curl`. Verify the "Hello World" response.

**Step 2: Database Connection and Schema**

*   **Goal:** Set up SQLAlchemy, define initial database models, and create the SQLite database file.
*   **Install:** SQLAlchemy already installed.
*   **Code:**
    *   In `backend/database/connection.py`: Write code to configure and create the SQLAlchemy engine and session, connecting to the `DATABASE_URL` from your `.env`. Add a function to get a database session.
    *   In `backend/database/models.py`: Define simple SQLAlchemy models for a `User` and perhaps a basic `Individual` (just ID and name for now).
    *   In `backend/database/crud.py`: Write a function to create the database tables based on your models. Write a simple function to add a test user.
    *   Modify `backend/main.py` to call the database table creation function when the app starts (or run it once manually).
*   **Test:** Run the backend server. Check if the `data/genealogy.db` file is created. Use a SQLite browser tool (like DB Browser for SQLite) to open the file and verify that the tables exist. Write and run a small Python script (outside the web server) that uses your `crud.py` functions to add and retrieve a test user directly to verify database interaction.

**Step 3: GEDCOM Parsing (Basic)**

*   **Goal:** Implement basic GEDCOM file reading and parsing.
*   **Install:** No additional libraries needed for basic line-by-line parsing. More advanced parsers exist if needed later.
*   **Code:**
    *   In `backend/services/gedcom_parser.py`: Write a Python function that takes a GEDCOM file path or content as input, reads it line by line, and extracts basic information like INDI and FAM records, names, and key events (BIRT, DEAT). Return a simple structured representation (like a dictionary or list of dictionaries) of the parsed data.
*   **Test:** Create a simple test GEDCOM file (you can use your provided sample data). Write a small Python script that calls your `gedcom_parser.py` function with this test file and prints the parsed output to verify it correctly extracts individuals and families.

**Step 4: GEDCOM Upload API Endpoint**

*   **Goal:** Create an API endpoint that receives a GEDCOM file, parses it, and saves the data to the database for a user.
*   **Install:** No additional installation if using FastAPI's file upload capabilities.
*   **Code:**
    *   In `backend/api/gedcom.py`: Define the `/api/upload_gedcom` endpoint (POST method). This endpoint will receive the file.
    *   Inside the endpoint function: Get the current authenticated user's ID (implement basic auth/session placeholder for now). Read the uploaded file's content. Call the `backend/services/gedcom_parser.py` function to parse the content. Call functions in `backend/database/crud.py` to save the parsed data, linking it to the user ID. Return a success message.
*   **Test:** Run the backend server. Use a tool like Postman, curl, or write a simple script to send a POST request with your test GEDCOM file to the `/api/upload_gedcom` endpoint. Check the backend logs for errors. Open the SQLite database with a browser and verify that the parsed data for the user has been correctly inserted into the `Individual` and `Family` tables.

**Step 5: First Genealogy Database Tool (Read)**

*   **Goal:** Create a LangChain Tool that can retrieve data about a person from the database, and test calling it directly (without the agent yet).
*   **Install:** LangChain already installed.
*   **Code:**
    *   In `backend/tools/genealogy_tools.py`: Define a Python function, say `get_individual_details_from_db(person_name)`. This function will take a person's name, query your `crud.py` functions to find them in the SQLite database for the current user (you'll need to pass user context here, potentially via a global or context variable in your backend for simplicity at this stage), and format the retrieved data (name, birth/death dates, parents, spouses, children IDs) into a clear string that an LLM can understand.
    *   In the same file, create a LangChain `Tool` instance: `genealogy_tool = Tool(name="get_person_facts", func=get_individual_details_from_db, description="Useful for getting core facts and relationships for a person in the user's family tree by their name.")`.
*   **Test:** Write a small Python script in the backend directory. In this script, initialize the LangChain Tool. Call the tool's `run()` method with a test person's name that you know is in your SQLite database. Print the output of the tool to verify it retrieves and formats the data correctly.

**Step 6: LangChain Agent with One Tool**

*   **Goal:** Set up the basic LangChain Agent Executor and get it to successfully use the genealogy database tool based on a user query.
*   **Install:** LangChain, LLM library installed. Need API key in `.env`.
*   **Code:**
    *   In `backend/agent/prompts/system_prompt.txt`: Write the initial system prompt (based on the conceptual prompt provided earlier), focusing on the agent's role and describing the single available tool (`get_person_facts`).
    *   In `backend/agent/agent_factory.py`: Write a function, say `create_genealogy_agent(user_id)`. This function will:
        *   Load the LLM (using `google-generativeai` or `openai` library, configured with the API key from `.env`).
        *   Load the system prompt from the file.
        *   Create an instance of your `get_person_facts` Tool (passing the `user_id` or user context so the tool knows which user's database to query).
        *   Initialize conversational memory (e.g., `ConversationBufferMemory`).
        *   Create and return a `LangChain AgentExecutor` instance, providing the LLM, the list containing only your `get_person_facts` tool, the system prompt, and the memory.
    *   Modify the `/api/chat` endpoint in `backend/api/chat.py`: Instead of just returning a static message, get the user ID, call `agent_factory.create_genealogy_agent(user_id)`, and then call `agent.run(user_message)`. Return the agent's response.
*   **Test:** Run the backend server. Using your browser or a tool, send a chat message to `/api/chat` like "Tell me about [Name of person in your database]". Observe the backend logs – you should see the agent's thought process, including its decision to use the `get_person_facts` tool, the tool's output, and the LLM's final generated response based on that output. Verify the final response is relevant to the person requested.

**Step 7: Add External Knowledge Tools (Wikipedia/YouTube)**

*   **Goal:** Implement and integrate the Wikipedia and YouTube search tools into the agent.
*   **Install:** `requests` for making HTTP requests to external APIs.
*   **Code:**
    *   In `backend/tools/external_tools.py`: Write Python functions `search_wikipedia_api(query)` and `search_youtube_api(query)`. These will use the `requests` library to call the respective APIs and return relevant information (e.g., Wikipedia summary/link, YouTube video titles/links). *Note: YouTube API requires API keys and can be more complex; start simple.*
    *   Wrap these functions as LangChain `Tool` instances in `backend/tools/external_tools.py` with clear descriptions (e.g., "Searches Wikipedia for information.", "Finds relevant historical videos on YouTube.").
    *   Modify `backend/agent/agent_factory.py` to include these new tools in the list provided to the `AgentExecutor`.
    *   Update the `backend/agent/prompts/system_prompt.txt` to describe these new tools and when the agent should consider using them (e.g., "Use `search_wikipedia` for general facts about places or events.", "Use `search_historical_youtube` to find videos that provide historical context.").
*   **Test:** Run the backend server. Send a chat message to `/api/chat` that would require these tools, like "Tell me about [Person Name] and the history of [Place they lived]". Observe the logs to see the agent potentially using multiple tools. Verify the agent's response includes information from both the database and the external sources, with links.

**Step 8: Basic Data Update Tool**

*   **Goal:** Implement a simple tool for the agent to update data.
*   **Install:** No new installs if using SQLAlchemy for updates.
*   **Code:**
    *   In `backend/database/crud.py`: Add a function like `update_user_haplogroups(user_id, paternal=None, maternal=None)` that safely updates the haplogroup fields for the specified user in the database.
    *   In `backend/tools/update_tools.py`: Create a Python function `handle_haplogroup_update(paternal_haplogroup, maternal_haplogroup)` that calls the `crud.py` update function for the current user. Wrap this as a LangChain `Tool` with a description like "Use this tool ONLY when the user explicitly provides their paternal and maternal haplogroup codes to update their profile. Input should be structured, like 'paternal=R-S476, maternal=V'."
    *   Modify `backend/agent/agent_factory.py` to include this `update_genetic_info` tool in the agent's tool list.
    *   Update the `backend/agent/prompts/system_prompt.txt` to instruct the agent on how and when to use this tool, emphasizing caution and parameter parsing (this is a key challenge for the LLM).
*   **Test:** Run the backend server. Send a message like "Update my haplogroups. My paternal is R-S476 and my maternal is V." Observe the logs to see if the agent attempts to use the `update_genetic_info` tool and how it tries to pass parameters. Check the SQLite database to see if the update occurred. (Expect this step to require prompt tuning for reliable parsing).

**Step 9: Frontend Connection to Chat API**

*   **Goal:** Connect the basic React frontend chat interface to your working backend chat API.
*   **Install:** `axios` recommended for easier API calls in React.
*   **Code:**
    *   In `frontend/src/api/backendApi.js`: Write an asynchronous function `sendMessage(message)` that uses `axios` to send a POST request to `http://localhost:8000/api/chat` (you'll configure proxying later for production) with the message body. This function should return the response data.
    *   In `frontend/src/components/ChatWindow.js`: Implement state to hold the messages. In the function triggered by the send button, call `backendApi.sendMessage()`, wait for the response, and update the message state to display both the user's message and the agent's response. Handle displaying links correctly.
*   **Test:** Run both the backend server (`cd backend && source venv/bin/activate && uvicorn main:app --reload`) and the frontend development server (`cd frontend && npm start`). Open your browser to the frontend URL (usually `http://localhost:3000`). Type a message in the chat and send it. Verify that the message appears in the chat window, the backend receives it (check logs), the agent processes it, and the agent's response appears back in the chat window, including clickable links from external tool results.

**Step 10: Basic Frontend User Flow (Login/Upload)**

*   **Goal:** Implement the basic user authentication and GEDCOM upload in the frontend.
*   **Code:**
    *   In `frontend/src/pages/LoginPage.js` and `frontend/src/pages/SignupPage.js`: Create simple forms for username/password. Implement functions in `backendApi.js` to send login/signup requests to backend auth endpoints.
    *   In `frontend/src/pages/GedcomUploadPage.js`: Create a file input form. Implement a function in `backendApi.js` to send the selected file to the `/api/upload_gedcom` endpoint.
    *   Implement basic routing in the frontend (`react-router-dom` is common) to navigate between these pages and the chat page, based on user authentication status (stored in frontend state or local storage for simplicity initially).
    *   Modify backend auth endpoints in `backend/api/auth.py` to handle user creation and login (password hashing is essential!).
*   **Test:** Test the signup, login, and GEDCOM upload flows. Verify user accounts are created in the database and uploaded GEDCOM data is correctly associated with the logged-in user. Ensure access to the chat page is restricted to authenticated users.

**Next Steps (Beyond MVP):**

After successfully completing Phase 1 (MVP), you will have a functional application. Phase 2 and 3 tasks (suggested prompts, learning plan, more complex updates, charting, etc.) can then be implemented incrementally, following the same pattern: implement backend logic/tool -> integrate into agent -> update frontend UI.

---



---

This plan provides a clear, actionable path for you and Grant to build the Ancestry Explorer, starting simple and layering functionality. Good luck with the codebase creation!

