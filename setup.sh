

# Create main directories
mkdir -p chutek-model_v1/{data/{raw,processed},models/{trained_model},notebooks,scripts,config}

# Create sample files inside those directories
touch chutek-model_v1/data/raw/{doc1.pdf,doc2.docx,scraped_data.html}
touch chutek-model_v1/data/processed/{train_data.txt,val_data.txt,test_data.txt}

touch chutek-model_v1/models/{gpt2_model.py,fine_tune_gpt2.py}
touch chutek-model_v1/models/trained_model/{model_checkpoint}

touch chutek-model_v1/notebooks/{data_exploration.ipynb,fine_tuning.ipynb,generate_text.ipynb}

touch chutek-model_v1/scripts/{preprocess_data.py,train.py,evaluate.py,generate_text.py}

touch chutek-model_v1/config/model_config.json

touch chutek-model_v1/requirements.txt
touch chutek-model_v1/README.md

echo "Project structure created successfully!"
