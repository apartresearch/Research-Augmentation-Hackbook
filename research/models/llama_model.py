from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


class LlamaModel:
    def __init__(self, model_name="meta-llama/Llama-2-7b-chat-hf"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            load_in_8bit=True,
            torch_dtype=torch.float16,
            device_map="auto",
        )

    def summarize(self, text, max_length=150):
        prompt = f"Please summarize the following text in about {max_length} words:\n\n{text}\n\nSummary:"

        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_length,
                num_return_sequences=1,
                temperature=0.7,
                top_p=0.9,
            )

        summary = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Extract the summary part from the generated text
        summary = summary.split("Summary:")[1].strip()

        return summary
