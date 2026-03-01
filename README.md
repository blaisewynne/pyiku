# Pyiku - A Python library that detects Haiku

## Overview
### `pyiku` is a library that detects haiku (haikus) in strings.
### Utilise the `Pyiku.is_haiku` function to detect if a string is a haiku.

## Usage
```
Pyiku.is_haiku("This is a library, made for the public to use, made just for you")
# Should return True
```

## FAQ
#### Q: How does it count syllables?
#### A: It iterates over each letter, checks if it's currently on a vowel, checks if it's not at the end of the word, if it isn't, then it checks if the next or previous letter is a vowel or a consonant. It doesn't count 'e's at the end of a sentence or 'y's that follow a vowel.

#### Q: What is the practical use for this?
#### A: See image below:
<img width="476" height="589" alt="image" src="https://github.com/user-attachments/assets/bcd4e785-50b5-47a3-9372-d4e5cc23abdb" />