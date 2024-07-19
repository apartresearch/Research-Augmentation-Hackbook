from transformers import pipeline, AutoTokenizer
from research.models.summarizer_model import SummarizerModel
# from research.models.llama_model import LlamaModel

bart_tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
bart_summarizer = pipeline(
    "summarization", model="facebook/bart-large-cnn", tokenizer=bart_tokenizer
)

# llama_model = LlamaModel()


def chunk_text(text, max_chunk_size):
    chunks = []
    current_chunk = []
    current_size = 0
    for sentence in text.split("."):
        sentence = sentence.strip() + "."
        sentence_tokens = bart_tokenizer.tokenize(sentence)
        if current_size + len(sentence_tokens) <= max_chunk_size:
            current_chunk.append(sentence)
            current_size += len(sentence_tokens)
        else:
            if current_chunk:
                chunks.append(" ".join(current_chunk))
            current_chunk = [sentence]
            current_size = len(sentence_tokens)
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks


def summarize_paper(text, model_choice="bart"):
    if model_choice == "bart":
        # BART can handle up to 1024 tokens, but we'll use a smaller chunk size for safety
        max_chunk_size = 900
        chunks = chunk_text(text, max_chunk_size)

        summaries = []
        for chunk in chunks:
            summary = bart_summarizer(
                chunk, max_length=150, min_length=30, do_sample=False
            )
            summaries.append(summary[0]["summary_text"])

        # Combine the summaries
        final_summary = " ".join(summaries)

        # If the combined summary is still too long, summarize it again
        if len(bart_tokenizer.tokenize(final_summary)) > max_chunk_size:
            final_summary = bart_summarizer(
                final_summary, max_length=150, min_length=50, do_sample=False
            )[0]["summary_text"]

        return final_summary
    # elif model_choice == "llama":
    #     return llama_model.summarize(text)
    else:
        raise ValueError("Invalid model choice. Choose 'bart' or 'llama'.")
