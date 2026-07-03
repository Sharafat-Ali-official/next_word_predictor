📚 Next Word Predictor

A simple Python program that predicts the next word based on a small text dataset.  
It learns patterns from sentences and suggests the most likely word to come next.

---

🎯 What It Does

You type a phrase, and the program guesses what word should come next.  
For example, if you type:

Enter a phrase: I love

The program might respond with:

Predicted next word: programming

It makes predictions by looking at patterns in the dataset – similar to how language models work, but much simpler!

---

📁 Project Structure

next_word_predictor/
dataset.txt       # Training data (sentences)
predictor.py      # Main Python program
README.md         # This file is markdown for project documentation

---

🚀 How to Run

1. Make sure Python is installed on your computer.  
   (Download from python.org if needed)

2. Open a terminal (Command Prompt on Windows, Terminal on Mac/Linux).

3. Navigate to the project folder:
   cd path/to/next-word-predictor

4. Run the program:
   python predictor.py

5. Start typing phrases and see the predictions!

   Type quit to exit.

---

📝 Dataset

The program learns from dataset.txt, which contains these sentences:

I love programming
I love AI
I love Python
Machine learning is fun
Machine learning is powerful
Deep learning is awesome
Deep learning is a subset of machine learning
Natural language processing is cool
Natural language processing uses machine learning

You can add your own sentences to the file – the program will learn from them too!

---

💡 Example Interaction

=== Next-Word Predictor (Beginner Edition) ===
Type 'quit' to exit.

Enter a phrase: I love
Predicted next word: programming

Enter a phrase: Machine learning
Predicted next word: is

Enter a phrase: Natural language processing
Predicted next word: is

Enter a phrase: quit

---

🧠 How It Works (Simple Explanation)

1. The program reads all sentences from dataset.txt.
2. It looks at every pair of words – for example, in "I love programming", it learns that:
   - "I" is often followed by "love"
   - "love" is followed by "programming"
3. It stores these patterns in a dictionary (like a phonebook).
4. When you type a phrase, it finds the last word, looks up what words usually follow it, and picks the most common one.

That's it – frequency-based prediction!

---

🔧 What I Learned

- How to read and process text files in Python.
- How to build and use dictionaries to store word patterns.
- How to predict based on frequency (a simple form of probability).
- That more data leads to better predictions – just like real language models!

---

🛠️ Requirements

- Python 3.12.1 (No extra libraries needed – uses only built-in modules: random, and collection library for counting)

---

📈 Future Improvements (Optional Ideas)

- Use two or three words as context for better predictions.
- Add case insensitivity (treat "I" and "i" as the same).
- Handle punctuation properly.
- Use a larger dataset for more accurate results.

---


---


> 💡 **Fun Fact:** This is how early language models worked – by counting patterns in text!