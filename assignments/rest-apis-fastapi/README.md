# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build a REST API using the FastAPI framework. You'll create a web service that handles HTTP requests, processes data, and returns responses using Python. By the end of this assignment, you'll understand how APIs work and be able to build a functional backend service.

## 📝 Tasks

### 🛠️ Create Your First FastAPI Application

#### Description
Create a basic FastAPI application with a simple endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance
- Create a GET endpoint at the root path (`/`) that returns a JSON response
- Return a message in JSON format: `{"message": "Welcome to the FastAPI Server!", "status": "running"}`
- Run the server using `uvicorn` and verify it works by visiting the endpoint in your browser or using a tool like `curl`
- Example:
  ```bash
  uvicorn starter-code:app --reload
  # Visit http://localhost:8000/ and see the JSON response
  ```

### 🛠️ Build Multiple Endpoints with Different HTTP Methods

#### Description
Expand your API to handle different types of requests. Create a simple note-taking service with multiple endpoints.

#### Requirements
Completed program should:

- Create a GET endpoint at `/notes` that returns a list of sample notes (each note should have an id, title, and content)
- Create a POST endpoint at `/notes` that accepts a new note (with title and content) and returns it with an id
- Create a GET endpoint at `/notes/{note_id}` that returns a specific note by id
- All endpoints should return valid JSON responses
- Example:
  ```bash
  # GET /notes
  [{"id": 1, "title": "My Note", "content": "Hello World"}]
  
  # POST /notes with body {"title": "New Note", "content": "Content here"}
  {"id": 2, "title": "New Note", "content": "Content here"}
  ```

### 🛠️ Add Data Validation with Pydantic Models

#### Description
Use Pydantic to define and validate request/response data structures. This ensures your API only accepts correctly formatted data.

#### Requirements
Completed program should:

- Create a Pydantic model called `Note` with fields: id (int), title (str), and content (str)
- Update your POST endpoint to accept a Note model in the request body (without the id)
- Use Pydantic models for all request and response validation
- Return proper error responses (400 Bad Request) when data doesn't match the model
- Example:
  ```bash
  # Invalid POST request - missing required field
  curl -X POST http://localhost:8000/notes -H "Content-Type: application/json" -d '{"title": "No content"}'
  # Returns: 422 Unprocessable Entity with error details
  ```

### 🛠️ ⭐ Stretch Goal: Error Handling and Status Codes

#### Description
Implement proper HTTP status codes and error handling for edge cases.

#### Requirements
Completed program should:

- Return 404 Not Found when accessing a note that doesn't exist
- Return 201 Created when successfully creating a new note (instead of 200 OK)
- Include helpful error messages in responses
- Example:
  ```bash
  # GET non-existent note
  curl http://localhost:8000/notes/999
  # Returns: 404 with message {"detail": "Note with id 999 not found"}
  ```
