"""Game guess the number
The computer comes up with a number and guesses it itself.
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Random guess number.

    Args:
        number (int, optional): Hidden number. Defaults to 1.

    Returns:
        int: Number of attempts 
    """
    count = 0
    
    first = 0 
    last = 101 # Arguments for module np.random.randit outside of funktion
    
    while True:
        count += 1
        predict_number = (np.random.randint(first, last)) # possible number
        
        if number > predict_number:
            first = predict_number 
            
            # If the given number is grater, the beginning of the search 
            # range is shifted to the assumed.
        
        elif number < predict_number:
            last = predict_number  
            
            # The and of the searchin range shifted likewise, 
            # if given number less then alleged.   
        
        elif number == predict_number: 
            
            break  # exit from the loop if guessed right

    return count


def score_game(random_predict) -> int:
    """
    For how many attempts on average for 1000 approaches our algorithm guesses

    Args:
        random_predict ([type]): function of guessing

    Returns:
        int: average quantity of attempts
    """
    count_ls = []
    np.random.seed(1)  # fix seed for the reproductibility
    random_array = np.random.randint(1, 101, size=(1000))  
    
    # guessed list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses number on average for:{score} attempts.")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
