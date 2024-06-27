# Longest Common Sequence

## Overview
This script is designed to compare two sequences of elements or strings provided by the user and determine their longest common sequence (LCS). It outputs this sequence to the user.

## How It Works
The script initialises a 2D list *'F'* to store the length of the LCS between subsequences *'A'* and *'B'*. It iterates over each character in *'A'* and *B*, updating *'F'* based on whether characters match or not. After building *'F'*, it traces back to construct LCS by following the maximum values in *'F'*.

## Usage
1. Clone the repository: git clone https://github.com/LisaOz/longestCommonSequence.git
2. Navigate to the project directory: cd longestCommonSequence
3. Run the script: python main.py
4. Follow the prompts:
   - Enter the fist sequence.
   - Enther the second sequence.
   - The script will output the longest common sequence found.

## Dependencies
- Python 3.x

## Licence
This project is licensed under the MIT License. See the [MIT License](https://opensource.org/licenses/MIT) for details.




