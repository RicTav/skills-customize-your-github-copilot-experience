"""
Starter code for Building REST APIs with FastAPI assignment.
Complete the tasks below to build your REST API.
"""

from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the FastAPI app
app = FastAPI()

# Task 1: Create a basic endpoint
# TODO: Create a GET endpoint at "/" that returns a welcome message
# Expected response: {"message": "Welcome to the FastAPI Server!", "status": "running"}


# Task 2 & 3: Create a note-taking service with Pydantic models
# TODO: Define a Pydantic model for Note (id, title, content)

class Note(BaseModel):
    """Model for a note. Remove the 'pass' and add your fields here."""
    pass


# TODO: Create a list to store notes in memory
# notes = [...]


# TODO: Create GET endpoint at "/notes" that returns all notes


# TODO: Create POST endpoint at "/notes" that accepts a new note and returns it with an id


# TODO: Create GET endpoint at "/notes/{note_id}" that returns a specific note by id


# Task 4 (Stretch): Add proper error handling
# TODO: Return 404 when note is not found
# TODO: Return 201 when creating a new note


# To run the server:
# pip install fastapi uvicorn
# uvicorn starter-code:app --reload
