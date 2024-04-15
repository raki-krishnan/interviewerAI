# InterviewerAI
Welcome to InterviewerAI, a project designed to help users improve their interviewing skills using artificial intelligence.

# Walkthrough video link
https://youtu.be/jbIMK_gJ4rA

## Inspiration
We realized that Gemini had a very accurate ability to recognize facial expressions, and wanted to explore innovative ways to apply this. As college students who often need to hone our interviewing skills, we wanted to explore a way to make this process easier to tackle and more enjoyable. While there are interview assistent applications out there, none of them are able to provide specific, tailored feedback based on both speech and facial expressions.

## What it does
Given a job title, company, and a question a user wants to answer, we allow the user to record a response. InterviewerAI will then parse the video frame by frame and separate the audio. We feed these components in individually and ask Gemini to provide feedback on them in the context of the given role, company, and question.

## How we built it
We used the Gemini API, JavaScript, and Flask to develop the backend and front-end on VSCode.

## Accomplishments that we're proud of
Using the Gemini API to develop a tool that legitimately gives accurate feedback to users. We think it's super cool that we can provide feedback involving visual aspects on top of just audio/speech.

## What we learned
Full-stack development, integrating the use of the Gemini API.

## What's next for InterviewerAI
Continue building, innovating, and optimizing!

## Built With
- Gemini
- JavaScript
- Python
- CSS
- VSCode


## Quickstart Guide

### Prerequisites

Before getting started, ensure you have the following installed on your system:

- [Node.js](https://nodejs.org/) (includes npm)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```bash
   cd InterviewerAI
   ```

3. Install dependencies using npm:

   ```bash
   npm install
   ```

### Usage

1. Start the development server:

   ```bash
   flask run --host=0.0.0.0 --port=4000
   ```

   This command will start the development server and open the application in your default web browser.

2. Follow the on-screen instructions to use the InterviewerAI application.

### Additional Scripts

- `npm run build`: Builds the production-optimized bundle of the application.
- `npm run test`: Runs the tests included in the project.

### Project Structure
- `/frontend/`: Contains the react.js code to build user interfaces.
- `/backend/`: Contains the flask and python code that serve the server and generate responses.
- `/src/`: Contains the source code of the application.
- `/public/`: Contains static assets and HTML template.
- `package.json`: Contains metadata and dependencies of the project.
