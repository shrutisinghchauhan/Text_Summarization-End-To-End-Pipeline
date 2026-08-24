from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path)

        gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}

        inputs = tokenizer(
            text,
            max_length=1024,
            truncation=True,
            padding="longest",
            return_tensors="pt",
        )

        summary_ids = model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            **gen_kwargs,
        )

        summary = tokenizer.decode(
            summary_ids[0],
            skip_special_tokens=True,
            clean_up_tokenization_spaces=True,
        )

        print("Dialogue:")
        print(text)
        print("\nModel Summary:")
        print(summary)

        return summary