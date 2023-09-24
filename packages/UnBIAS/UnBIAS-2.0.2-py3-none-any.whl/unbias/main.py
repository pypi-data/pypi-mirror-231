from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoModelForTokenClassification, AutoModelForCausalLM, pipeline
import torch
import pandas as pd

class BiasPipeline:
    def __init__(self):
        self.classifier_model = AutoModelForSequenceClassification.from_pretrained("newsmediabias/UnBIAS-classifier")
        self.classifier_tokenizer = AutoTokenizer.from_pretrained("newsmediabias/UnBIAS-classifier")

        self.ner_model = AutoModelForTokenClassification.from_pretrained("newsmediabias/UnBIAS-Named-entity")
        self.ner_tokenizer = AutoTokenizer.from_pretrained("newsmediabias/UnBIAS-Named-entity")

        self.debiaser_model = AutoModelForCausalLM.from_pretrained("newsmediabias/UnBIAS-LLama2-Debiaser-Chat")
        self.debiaser_tokenizer = AutoTokenizer.from_pretrained("newsmediabias/UnBIAS-LLama2-Debiaser-Chat")

        self.classifier = pipeline("text-classification", model=self.classifier_model, tokenizer=self.classifier_tokenizer)
        self.ner = pipeline("ner", model=self.ner_model, tokenizer=self.ner_tokenizer)

    def debias_text(self, text):
        instruction = "Debias this text:"
        system_message = ("You are a text debiasing bot, you take as input a text and you output "
                          "its debiased version by rephrasing it to be free from any age, gender, "
                          "political, social or socio-economic biases, without any extra outputs")

        pipe = pipeline(
            task="text-generation",
            model=self.debiaser_model,
            tokenizer=self.debiaser_tokenizer,
            max_length=500
        )
        
        debiased_output = pipe(f"<s>[INST] <<SYS>>{system_message}<</SYS>> {instruction} {text} [/INST]")
        debiased_text = debiased_output[0]['generated_text'].split('\n')[3].strip('"')
        return debiased_text

    def pretty_print(self, texts, classification_results, ner_results, debiased_texts):
        for i, text in enumerate(texts):
            print(f"Text {i + 1}:")
            print("-" * 50)

            print("Original Text:")
            print(text)

            print("\nClassification:")
            print(f"Label: {classification_results[i]['label']}")
            print(f"Score: {classification_results[i]['score']:.4f}")

            print("\nBiased Entities:")
            biased_words = [entry['word'] for entry in ner_results[i] if entry['entity'] == 'Biased']
            if biased_words:
                print(", ".join(biased_words))
            else:
                print("No biased entities detected.")

            print("\nDebiased Text:")
            print(debiased_texts[i])

            print("=" * 50)
  
    def results_to_dataframe(self, texts, classification_results, ner_results, debiased_texts):
        data = {
            'Original Text': texts,
            'Classification Label': [result['label'] for result in classification_results],
            'Classification Score': [result['score'] for result in classification_results],
            'Biased Words': [[entry['word'] for entry in ner_result if entry['entity'] == 'Biased'] for ner_result in ner_results],
            'Debiased Text': debiased_texts
        }
        df = pd.DataFrame(data)
        return df
    
    def process(self, texts):
        classification_results = self.classifier(texts)
        ner_results = self.ner(texts)
        debiased_texts = [self.debias_text(text) for text in texts]
        
        return classification_results, ner_results, debiased_texts




# Optionally, you can include a main block to demonstrate usage or for testing
if __name__ == '__main__':
    pipeline_instance = BiasPipeline()
    texts = ["Women are too emotional and can not be good leaders "]
    classification_results, ner_results, debiased_texts = pipeline_instance.process(texts)
    pipeline_instance.pretty_print(texts, classification_results, ner_results, debiased_texts)

    # Convert results to a DataFrame
    df = pipeline_instance.results_to_dataframe(texts, classification_results, ner_results, debiased_texts)

    # Save the DataFrame to a CSV file
    df.to_csv("debiased_results.csv", index=False)