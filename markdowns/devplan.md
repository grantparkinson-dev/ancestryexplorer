**DEVELOPMENT_PLAN.md (Project Root)**

```markdown
# Ancestry Explorer: Detailed Development Plan

This document outlines the step-by-step plan for building the Ancestry Explorer application, focusing on incremental development and testing using FastAPI and React.

**Core Principle:** Build and test the simplest possible implementation of each component before moving to the next.

**Phased Approach:**

*   **Phase 1: Foundation and Minimum Viable Product (MVP)** - Establish the core backend, database, agent, and frontend chat interface.
*   **Phase 2: Adding Key Agentic Features** - Implement data updates, prompt suggestions, and basic progress tracking.
*   **Phase 3: Refinement and Enhancements** - Add charting, improve reliability, optimize performance, and enhance UI/UX.
*   **(Future Phases):** Yearbook integration, more data sources, advanced visualizations, mobile apps, scaling.

---

## Phase 1: Foundation and Minimum Viable Product (MVP)

**Goal:** A working web application where a user can sign up, subscribe (placeholder), upload GEDCOM, and chat with an AI agent to get basic facts and external context (Wikipedia/YouTube links) about individuals in their tree.

**Step-by-Step Build & Test Plan:**

1.  **Step 1: Basic Backend Server**
    *   **Goal:** FastAPI server runs and responds to a root request.
    *   **Tasks:**
        *   Create `backend/main.py` with a basic FastAPI app.
        *   Add `@app.get("/")` endpoint returning `{"message": "Hello Ancestry Explorer Backend!"}`.
    *   **Test:** Run `uvicorn main:app --reload` in backend venv. Access `http://127.0.0.1:8000/` in browser/curl. Verify response.
    *   **Verification:** Server is running, basic endpoint works.

2.  **Step 2: Database Connection and Schema**
    *   **Goal:** SQLAlchemy configured, models defined, SQLite file created, can perform basic CRUD via functions.
    *   **Tasks:**
        *   Create `backend/database/connection.py`, `models.py`, `crud.py`.
        *   Define User, Individual models in `models.py` using SQLAlchemy.
        *   Implement connection and session functions in `connection.py`.
        *   Implement table creation function in `crud.py`.
        *   Implement simple `create_user` and `get_user` functions in `crud.py`.
        *   Add database initialization call in `backend/main.py` (or run separately).
    *   **Test:** Run backend/init script. Check for `data/genealogy.db`. Use SQLite browser to inspect tables. Write and run a script calling `crud.py` functions to add/get a test user.
    *   **Verification:** Database file exists, tables created, basic CRUD functions work outside FastAPI.

3.  **Step 3: GEDCOM Parsing (Basic)**
    *   **Goal:** A Python function can read a GEDCOM file and extract core individual/family data.
    *   **Tasks:**
        *   Create `backend/services/gedcom_parser.py`.
        *   Write `parse_gedcom_file(file_path)` function extracting INDI/FAM, names, BIRT/DEAT events.
    *   **Test:** Create a test `.ged` file. Write script to call parser function and print output. Verify extracted data looks correct.
    *   **Verification:** Parser function correctly extracts key data points from GEDCOM.

4.  **Step 4: GEDCOM Upload API Endpoint**
    *   **Goal:** Frontend can upload a GEDCOM, backend parses and saves it to the database linked to a user.
    *   **Tasks:**
        *   Implement basic user authentication placeholder (e.g., hardcoded user ID for now, or simple token check).
        *   Create `backend/api/gedcom.py` with `/api/upload_gedcom` POST endpoint.
        *   Endpoint receives file, calls `gedcom_parser.py`, and calls `crud.py` functions to save data associated with the current user.
    *   **Test:** Run backend. Use Postman/curl to send test GEDCOM to the endpoint (include user context placeholder). Check backend logs. Open `genealogy.db` and verify data for test user.
    *   **Verification:** File upload endpoint works, parsing is triggered, data is saved correctly to the database.

5.  **Step 5: First Genealogy Database Tool (Read)**
    *   **Goal:** A LangChain `Tool` is created that uses your database CRUD functions to retrieve person data, testable outside the agent.
    *   **Tasks:**
        *   In `backend/tools/genealogy_tools.py`, write `get_individual_details_from_db(person_name, user_id)` function calling `crud.py` and formatting results.
        *   Create LangChain `Tool` instance wrapping this function with description `name="get_person_facts"`.
    *   **Test:** Write script to initialize the Tool (providing a test `user_id`). Call `tool.run("Test Person Name")`. Verify output is correctly formatted data from the database.
    *   **Verification:** Custom database retrieval function works and is correctly wrapped as a LangChain Tool.

6.  **Step 6: LangChain Agent with One Tool**
    *   **Goal:** LangChain Agent Executor is set up and uses the `get_person_facts` tool based on a chat message.
    *   **Tasks:**
        *   Get Gemini API key, add to `.env`.
        *   Create `backend/agent/prompts/system_prompt.txt` with basic agent instructions and tool description.
        *   Create `backend/agent/agent_factory.py` with `create_genealogy_agent(user_id)` function.
        *   Inside `create_genealogy_agent`: Initialize LLM, load prompt, create `get_person_facts` Tool (with user context), set up `ConversationBufferMemory`, create and return `AgentExecutor`.
        *   Modify `backend/api/chat.py` `/api/chat` POST endpoint: Get user ID (placeholder), create agent instance, call `agent.run(user_message)`.
    *   **Test:** Run backend server. Send message "Tell me about [Name of person in DB]" to `/api/chat`. Observe backend logs for agent thought process. Verify agent calls the tool and generates a response based on tool output.
    *   **Verification:** Agent is initialized, receives messages, uses the database tool, and generates a response.

7.  **Step 7: Add External Knowledge Tools (Wikipedia/YouTube)**
    *   **Goal:** Agent can search Wikipedia and YouTube for historical context.
    *   **Tasks:**
        *   In `backend/tools/external_tools.py`, write `search_wikipedia_api(query)` and `search_youtube_api(query)` functions using `requests`. Wrap them as LangChain `Tool`s (`name="search_wikipedia"`, `name="search_historical_youtube"`).
        *   Modify `backend/agent/agent_factory.py` to include these new tools.
        *   Update `backend/agent/prompts/system_prompt.txt` to describe these tools and when to use them.
    *   **Test:** Run backend server. Send messages like "Tell me about [Person Name] and the history of [Place]" or "Find me a video about [Historical Event]". Observe logs to see agent using multiple tools. Verify response includes info/links from external sources.
    *   **Verification:** External search tool functions work and are integrated into the agent's toolset and prompt. Agent uses them dynamically.

8.  **Step 8: Basic Data Update Tool**
    *   **Goal:** Agent can perform simple data updates (e.g., haplogroups) via a tool.
    *   **Tasks:**
        *   In `backend/database/crud.py`, add `update_user_haplogroups(user_id, paternal, maternal)` function.
        *   In `backend/tools/update_tools.py`, write `handle_haplogroup_update(paternal_haplogroup, maternal_haplogroup, user_id)` function calling `crud.py`. Wrap as LangChain `Tool` (`name="update_genetic_info"`), describing input parameters.
        *   Modify `agent_factory.py` to include the update tool.
        *   Update `system_prompt.txt` to describe the update tool and its use, including the expected parameter format (this is key for LLM parsing).
    *   **Test:** Run backend. Send messages like "Update my haplogroups, paternal is R-S476 and maternal is V." Observe logs for agent using `update_genetic_info` tool and extracted parameters. Check database for update.
    *   **Verification:** Update tool function works, is integrated, agent attempts to use it (reliability depends on prompt/model parsing).

9.  **Step 9: Frontend Connection to Chat API**
    *   **Goal:** React frontend chat UI sends messages to backend and displays responses.
    *   **Tasks:**
        *   Create basic React app structure in `frontend/src`.
        *   Implement `ChatWindow` component with input, send button, message display area.
        *   Create `frontend/src/api/backendApi.js` with `sendMessage(message)` using `axios` to call backend `/api/chat`.
        *   In `ChatWindow`, use state to hold messages, call `sendMessage` on button click, update state with user and agent messages.
    *   **Test:** Run backend and frontend dev servers. Open app in browser. Send message in chat. Verify message appears locally, backend receives it, and agent response appears in chat.
    *   **Verification:** Frontend chat UI sends/receives messages via the backend API.

10. **Step 10: Basic Frontend User Flow (Login/Upload)**
    *   **Goal:** Implement frontend forms and backend endpoints for user auth and GEDCOM upload.
    *   **Tasks:**
        *   Implement backend endpoints in `backend/api/auth.py` for signup/login (basic user creation/lookup in DB).
        *   Implement frontend components (`LoginPage`, `SignupPage`) with forms.
        *   Implement `backendApi.js` functions for login/signup/upload.
        *   Implement frontend routing (`react-router-dom`).
        *   Update GEDCOM upload endpoint in `backend/api/gedcom.py` to require authentication and link to logged-in user.
    *   **Test:** Test user signup and login. Test GEDCOM upload through the frontend form. Verify data saved correctly for the logged-in user.
    *   **Verification:** User authentication and file upload flows are functional end-to-end through the UI.
