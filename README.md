# Research Augmentation Hackbook
Welcome to the Research Augmentation Hackathon! This hackbook will guide you through creating, using, and improving an AI-powered tool for summarizing research papers. Our goal is to boost productivity in AI safety research by building open-source tools that can make transformative changes in how alignment research is done today. In this hackbook we aim to foster collaboration between AI researchers and engineers so that they better understand each other's challenges.

We'll go through:
- Setting up the project
- Creating a basic summarizer using BART and LLaMA2 models
- Improving the summarization quality
- Optimizing the system for production use
- Evaluating and comparing different summarization models

This hackbook is designed for both researchers focusing on building the next generation of AI, and engineers working on deploying and scaling AI systems.

## Getting Started
First, let's set up our project environment: 
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your API keys for accessing the LLaMA2 model


## Repository Overview

- `research/`: Contains the data, models, and evaluation metrics (to be implemented) for the summarization task.
- `src/`: Houses the backend API
- `templates/`: Houses the frontend html file.
- `docs/`: Contains guides for how researchers and engineers can contribute to this project.

## Creating Our Summarizer
In this section, we'll implement two summarization models: BART and LLaMA2. Each model has its strengths and challenges, and understanding both will give us insights into different approaches to summarization.

### BART Summarizer
BART is a denoising autoencoder for pretraining sequence-to-sequence models. It's particularly effective for text generation tasks like summarization due to its bidirectional encoder and auto-regressive decoder.

We have implemented a basic BART inference pipeline in `research/models/summarizer_model.py`

Key points about this implementation:

- We use the bart-large-cnn model, which is fine-tuned for summarization tasks.
- The chunk_text function splits long documents into manageable chunks, as BART has an input limit.
- We summarize each chunk separately and then combine the summaries.
- If the combined summary is still too long, we summarize it again to get a concise final summary.

This approach allows us to handle research papers of varying lengths while maintaining the context as much as possible. However, there is still a lot of room for improvement. We will discuss some of these in a later section.

### LLaMA2 Summarizer

LLaMA2 is a more recent and powerful language model that can be adapted for various tasks, including summarization. It has a larger context window and more diverse training data compared to BART.

We have implemented a basic BART inference pipeline in `research/models/llama_model.py`

Key points about this implementation:

- We're using the 7B parameter version of LLaMA2, which balances performance and resource requirements.
- The model is loaded in 8-bit quantization to reduce memory usage while maintaining performance.
- We use a prompt-based approach, instructing the model to generate a summary of a specific length.
- The temperature and top_p parameters control the randomness and diversity of the generated summary.
- Currently the LLaMa2 model is commented out to allow folks with less powerful systems to run this code.

LLaMA2's larger context window allows it to potentially capture more long-range dependencies in the text, which could be beneficial for summarizing complex research papers. However, there are concerns with safety and bias in LLMs like LLaMa2.

## Improving Summarization Quality [Exercise for Researchers]
Now that we have our basic summarizers, let's work on improving their quality. Here are some areas to explore:

- Fine-tuning: Adapt the models to scientific paper summarization by fine-tuning them on a dataset of scientific abstracts.
- Prompt Engineering: Experiment with different prompts for the LLaMA2 model to generate better summaries.
- Evaluation Metrics: Implement ROUGE scores and other relevant metrics to quantitatively assess summary quality.
- Hybrid Approaches: Combine extractive and abstractive summarization techniques for potentially better results.

## Optimizing for Production [Exercise for Engineers]
To make our summarizer production-ready, we need to focus on performance and scalability. Here are some tasks to tackle:

- API Development: Create a RESTful API using Flask or FastAPI to serve the summarization models.
- Caching: Implement a caching mechanism to store and quickly retrieve summaries for previously seen papers.
- Asynchronous Processing: Use message queues (e.g., Celery) for handling long-running summarization tasks.
- Containerization: Dockerize the application for easy deployment and scaling.
- Monitoring and Logging: Implement proper logging and monitoring to track system performance and errors.

## Next Steps and Challenges

- Multi-Lingual Support: Extend the summarizer to work with papers in multiple languages.
- Domain Adaptation: Fine-tune the models for specific scientific domains (e.g., medical, computer science).
- Long Document Handling: Improve the chunking strategy or explore models that can handle longer contexts.
- User Feedback Integration: Implement a mechanism to collect and incorporate user feedback for continuous improvement.
- Safety Considerations: Address potential biases, deceoption and other safety concerns in summarization