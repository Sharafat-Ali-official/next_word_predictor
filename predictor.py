import random
import os  # NEW: For handling file paths

# ---------- YOUR DATASET FILE PATH ----------
# This tells Python exactly where to find dataset.txt
DATASET_PATH = r"C:\Users\USER69\Desktop\AI_LLM\next_word_predictor\dataset.txt"

# ---------- Helper functions ----------
def read_dataset(filename):
    """Open the file and read all sentences into a list."""
    file = open(filename, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()

    sentences = []
    for line in lines:
        clean_line = line.strip()
        if clean_line != "":
            sentences.append(clean_line)
    
    return sentences

def build_dictionary(sentences):
    """
    For every sentence, look at each pair of words.
    Store: current word -> list of words that came after it.
    """
    transitions = {}

    for sentence in sentences:
        words = sentence.split()
        
        for i in range(len(words) - 1):
            current = words[i]
            next_word = words[i+1]
            
            if current not in transitions:
                transitions[current] = []
            
            transitions[current].append(next_word)
    
    return transitions

def get_most_frequent(word_list):
    """
    Given a list of words, find the one that appears the most.
    Example: ["AI","AI","Python"] -> "AI"
    """
    counts = {}
    for w in word_list:
        if w not in counts:
            counts[w] = 0
        counts[w] = counts[w] + 1
    
    best_word = None
    highest_count = 0
    
    for word, count in counts.items():
        if count > highest_count:
            highest_count = count
            best_word = word
    
    return best_word

def predict_next_word(transitions, user_phrase, random_mode=False):
    """
    Take the last word from user input, look it up in the dictionary,
    and return the most likely next word.
    """
    words = user_phrase.strip().split()
    
    if len(words) == 0:
        return None
    
    last_word = words[-1]
    
    if last_word not in transitions:
        return None
    
    candidates = transitions[last_word]
    
    if random_mode:
        return random.choice(candidates)
    else:
        return get_most_frequent(candidates)

def learn_new_sentence(transitions, sentence):
    """
    Take a brand new sentence, split it, and update the dictionary
    with all the word pairs found in it.
    """
    words = sentence.split()
    for i in range(len(words) - 1):
        current = words[i]
        next_word = words[i+1]
        
        if current not in transitions:
            transitions[current] = []
        transitions[current].append(next_word)

def save_dataset(filename, sentences_list):
    """Write all sentences back to the file, one per line."""
    file = open(filename, 'w', encoding='utf-8')
    for s in sentences_list:
        file.write(s + '\n')
    file.close()

def main():
    print("=== Next-Word Predictor (Beginner Edition) ===")
    print("Type 'quit' to exit.\n")
    
    # Use the full path to dataset.txt
    sentences = read_dataset(DATASET_PATH)
    transitions = build_dictionary(sentences)
    
    while True:
        user_input = input("Enter a phrase: ")
        
        if user_input.lower() == "quit":
            break
        
        prediction = predict_next_word(transitions, user_input, random_mode=False)
        
        if prediction is None:
            print("Sorry, I don't have enough data to predict.")
            
            add_choice = input("Do you want to add this phrase as a new sentence? (y/n): ")
            if add_choice.lower() == "y":
                sentences.append(user_input)
                learn_new_sentence(transitions, user_input)
                save_dataset(DATASET_PATH, sentences)  # Save to the full path
                print("Added! Now I can learn from it.\n")
            continue
        
        print(f"Predicted next word: {prediction}")
        
        correct = input("Was that prediction correct? (y/n): ")
        
        if correct.lower() == "y":
            print("Great!\n")
        else:
            correct_word = input("What should have been the next word? ")
            
            last_word = user_input.strip().split()[-1]
            
            if last_word not in transitions:
                transitions[last_word] = []
            transitions[last_word].append(correct_word)
            
            full_sentence = user_input + " " + correct_word
            sentences.append(full_sentence)
            save_dataset(DATASET_PATH, sentences)  # Save to the full path
            print("Thanks! I've updated my knowledge.\n")
        
        add_new = input("Would you like to add a brand new sentence for training? (y/n): ")
        if add_new.lower() == "y":
            new_sentence = input("Type the new sentence: ")
            sentences.append(new_sentence)
            learn_new_sentence(transitions, new_sentence)
            save_dataset(DATASET_PATH, sentences)  # Save to the full path
            print("Added to dataset and memory!\n")

if __name__ == "__main__":
    main()
