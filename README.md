# Natural Language Processing (NLP) Project

## Overview

This project implements two primary functionalities: **Text Summarization with Keyword Extraction** and **Sentiment Analysis**. The project leverages transformer models from the Hugging Face `transformers` library and employs TF-IDF for keyword extraction. The summarization and sentiment analysis components process textual data stored in `.txt` files.

## Project Structure

The project directory is organized as follows:

```
project-directory/
│
├── SE.py                  # Script for text summarization and keyword extraction
├── senti.py               # Script for sentiment analysis
├── txt files/             # Directory containing input text files
│   ├── activities.txt     # Text file containing activities data
│   ├── discussion.txt     # Text file containing discussion data
│   ├── office.txt         # Text file containing office-related data
│   ├── production.txt     # Text file containing production data
│   ├── report.txt         # Text file containing report data
│   └── sentences.txt      # Text file containing sentences for sentiment analysis
│
└── requirements.txt        # File listing required libraries
```

## Requirements

To run this project, ensure you have Python 3.7 or later installed. The following libraries are required:

- `transformers`: For implementing pre-trained models for text summarization and sentiment analysis.
- `torch`: Required for running models from the Hugging Face library.
- `sklearn`: For the TF-IDF vectorization used in keyword extraction.
- `os`: For directory and file management in Python.

You can install the required libraries using `pip`. Create a virtual environment (optional but recommended) and install the dependencies as follows:

```bash
pip install -r requirements.txt
```

### `requirements.txt`

```plaintext
torch
transformers
scikit-learn
```

## How to Use This Repository

1. **Clone the Repository**

   First, clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/AaftabAalam/NLP-project.git
   ```

2. **Navigate to the Project Directory**

   Change into the project directory:

   ```bash
   cd NLP-project
   ```

3. **Set Up the Environment**

   If you haven’t already, set up a virtual environment and install the required dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

4. **Prepare Your Text Files**

   Ensure that the text files you want to process are located in the `txt files/` directory. You can edit or add `.txt` files as needed.

5. **Run Text Summarization and Keyword Extraction**

   To summarize the text and extract keywords, run the `SE.py` script:

   ```bash
   python SE.py
   ```

   This will process all `.txt` files in the `txt files/` directory and print the summaries and keywords to the console.

6. **Run Sentiment Analysis**

   To analyze the sentiment of messages, run the `senti.py` script:

   ```bash
   python senti.py
   ```

   This will read the `sentences.txt` file and output the sentiment and emotion results for each message.

## Example Output

**SE.py Output:**

```
---------- Summary of file 1 activities.txt ----------
The summary text goes here.

---------- Top keywords for file 1 activities.txt ----------
keyword1, keyword2, keyword3, keyword4, ...
```

**senti.py Output:**

```
Message: This is a sample message.
Sentiment: POSITIVE (Score: 0.95)
Emotion: Joy (Score: 0.90)
--------------------------------------------------
```

## Notes

- Ensure the `.txt` files in the `txt files/` directory contain properly formatted text for best results.
- Adjust the parameters in the summarization model or TF-IDF vectorizer as needed based on your specific requirements or to optimize performance.

## Acknowledgments

This project utilizes the Hugging Face `transformers` library and its pre-trained models for natural language processing tasks, significantly simplifying the implementation of complex algorithms.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
