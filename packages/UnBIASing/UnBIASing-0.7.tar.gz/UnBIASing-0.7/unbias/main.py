import pandas as pd
from transformers import (AutoTokenizer, AutoModelForSequenceClassification, AutoModelForTokenClassification,
                          AutoModelForSeq2SeqLM, T5Tokenizer, T5ForConditionalGeneration, pipeline)
import torch

class BiasPipeline:
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        # Load models and tokenizers
        self.classifier_tokenizer = AutoTokenizer.from_pretrained("newsmediabias/UnBIAS-classifier")
        self.classifier_model = AutoModelForSequenceClassification.from_pretrained("newsmediabias/UnBIAS-classifier").to(self.device)

        self.ner_tokenizer = AutoTokenizer.from_pretrained("newsmediabias/UnBIAS-Named-entity")
        self.ner_model = AutoModelForTokenClassification.from_pretrained("newsmediabias/UnBIAS-Named-entity").to(self.device)

        self.debiaser_tokenizer = AutoTokenizer.from_pretrained("newsmediabias/UnBIAS-Debiaser")
        self.debiaser_model = AutoModelForSeq2SeqLM.from_pretrained("newsmediabias/UnBIAS-Debiaser").to(self.device)

        self.t5_tokenizer = T5Tokenizer.from_pretrained("t5-base")
        self.t5_model = T5ForConditionalGeneration.from_pretrained("t5-base").to(self.device)

        # Initialize pipelines
        self.classifier_pipe = pipeline('sentiment-analysis', model=self.classifier_model, tokenizer=self.classifier_tokenizer, device=self.device.index)
        self.ner_pipe = pipeline('ner', model=self.ner_model, tokenizer=self.ner_tokenizer, device=self.device.index)

        # Initialize biased lexicon set
        self.biased_lexicon = set()

    def load_biased_lexicon(self, filepath):
        with open(filepath, 'r') as file:
            self.biased_lexicon = set(line.strip().lower() for line in file)

    def convert_to_positive(self, text):
        prompt = f"Rephrase the following statement in a positive and constructive manner,remove any toxic and bad language words and repharase to positive, including content inside quotes: '{text}'"
        input_ids = self.t5_tokenizer.encode(prompt, return_tensors="pt").to(self.device)
        output = self.t5_model.generate(input_ids, max_length=200, num_return_sequences=1,
                                        num_beams=5, early_stopping=True,
                                        temperature=0.7, top_k=50, top_p=0.95,
                                        no_repeat_ngram_size=2)
        generated_text = self.t5_tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_text


    def classifier(self, texts):
        return self.classifier_pipe(texts)

    def enhanced_ner(self, texts):
        ner_results = self.ner_pipe(texts)
        enhanced_results = []

        for idx, text in enumerate(texts):
            current_entities = []

            # Check if NER model identifies any biased words
            for entity in ner_results[idx]:
                word = entity['word'].lower()
                if entity['entity'] not in ["O", "Information"] and word in self.biased_lexicon and word in text.split():
                    current_entities.append(entity)

            # Additionally, check the lexicon for biased words/phrases
            for lexicon_item in self.biased_lexicon:
                if lexicon_item in text.lower().split() and lexicon_item not in [entity['word'].lower() for entity in current_entities]:
                    current_entities.append({'word': lexicon_item, 'entity': 'Biased', 'score': 1.0})

            enhanced_results.append(current_entities)

        return enhanced_results


    def ensemble_debias_text(self, text):
        t5_inputs = self.debiaser_tokenizer.encode_plus(text, return_tensors="pt", truncation=True, padding='max_length', max_length=150)
        t5_inputs = {key: value.to(self.device) for key, value in t5_inputs.items()}
        with torch.no_grad():
            t5_output = self.debiaser_model.generate(t5_inputs["input_ids"], attention_mask=t5_inputs["attention_mask"], max_length=150, pad_token_id=self.debiaser_tokenizer.eos_token_id)
        debiased_text = self.debiaser_tokenizer.decode(t5_output[0], skip_special_tokens=True)

        # Check sentiment of debiased text
        sentiment = self.classifier([debiased_text])[0]['label']
        if sentiment in ["Negative", "Highly Biased", "Slightly Biased"]:
            debiased_text = self.convert_to_positive(debiased_text)

        return debiased_text


    def debias_text(self, text):
        # Use the T5 model to debias
        t5_inputs = self.debiaser_tokenizer.encode_plus(text, return_tensors="pt", truncation=True, padding='max_length', max_length=150)
        t5_inputs = {key: value.to(self.device) for key, value in t5_inputs.items()}
        with torch.no_grad():
            t5_output = self.debiaser_model.generate(t5_inputs["input_ids"], attention_mask=t5_inputs["attention_mask"], max_length=150, pad_token_id=self.debiaser_tokenizer.eos_token_id)
        debiased_text = self.debiaser_tokenizer.decode(t5_output[0], skip_special_tokens=True)

        # Check sentiment of the debiased text
        sentiment = self.classifier([debiased_text])[0]['label']

        # If sentiment is negative, convert to positive
        if sentiment == "Negative":
            debiased_text = self.convert_to_positive(debiased_text)

        return debiased_text

    def process(self, texts):
        classification_results = self.classifier(texts)
        ner_results = self.enhanced_ner(texts)

        # Use debias_text function for debiasing
        debiaser_results = [self.debias_text(text) for text in texts]

        return {
            "classification": classification_results,
            "ner": ner_results,
            "debiased_text": debiaser_results
        }

 
if __name__ == "__main__":
    # Usage
    bias_pipeline = BiasPipeline()


