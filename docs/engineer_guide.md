# Engineer's Guide

As an engineer on this project, your role is to develop the infrastructure to serve the summarization model and create a user interface.

## Tasks

1. **Backend Development**
   - Implement a Flask or FastAPI backend in `src/backend/app.py`.
   - Create an endpoint for paper upload and summarization requests.
   - Integrate the summarization model from `research/models/fine_tuned_model.py`.

2. **Frontend Development**
   - Create a simple web interface in `src/frontend/index.html` and `src/frontend/script.js`.
   - Implement functionality for uploading papers and displaying summaries.

3. **System Architecture**
   - Ensure the system can handle multiple users and papers simultaneously.
   - Implement proper error handling and logging.

4. **Testing**
   - Write unit tests for the API and summarizer in the `tests/` directory.
   - Implement integration tests to ensure end-to-end functionality.

5. **Deployment**
   - Containerize the application using Docker.
   - Set up a CI/CD pipeline for automated testing and deployment.

## Collaboration with Researchers

- Regularly communicate with the research team about model requirements and performance.
- Provide feedback on model latency and resource usage in a production setting.
- Assist in implementing evaluation metrics in the deployed system.