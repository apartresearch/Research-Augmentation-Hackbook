from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


class SummarizerModel:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def summarize(self, text, max_length=150, min_length=50):
        inputs = self.tokenizer.encode(
            "summarize: " + text, return_tensors="pt", max_length=1024, truncation=True
        )
        summary_ids = self.model.generate(
            inputs,
            max_length=max_length,
            min_length=min_length,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True,
        )
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
