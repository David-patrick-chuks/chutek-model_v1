# Chtek-V1 Text Generation Project

## Project Structure

This project fine-tunes a GPT-2 model to generate text based on various data sources (PDF, DOC, web scraping).

### Setup Instructions

1. Clone the repository and navigate to the project folder.
2. Create a virtual environment:
   ```bash
   python3 -m venv venv


3. Activate the environment:
bash
Copy code
source venv/bin/activate  # macOS/Linux
.\venv\Scripts\activate   # Windows

4. Install the required dependencies:
bash
Copy code
pip install -r requirements.txt


## Files and Scripts
preprocess_data.py: Converts PDFs and DOC files into text data for training.
gpt2_model.py: Defines the GPT-2 model.
fine_tune_gpt2.py: Fine-tunes the GPT-2 model on your custom dataset.
train.py: Main training script.
evaluate.py: Evaluates the model performance.
generate_text.py: Generates text based on a prompt using the fine-tuned model.