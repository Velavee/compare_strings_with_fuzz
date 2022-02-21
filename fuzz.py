from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from pyxdameraulevenshtein import damerau_levenshtein_distance

def remove_puncuation(sentence):
    puncuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in puncuation:
        sentence = sentence.replace(char, "")

    return sentence

def check_answer(correct_ans, user_ans):
    correct_ans = remove_puncuation(correct_ans)
    user_ans = remove_puncuation(user_ans)

    # Check basic Levenshtein Distance
    score = fuzz.ratio(correct_ans, user_ans)
    if score >= 98:
        return True

    # Transpositions are counted as two edits in Levenshtein Distance. Use Damerau-Levenshtein
    # distance to check if difference is a single transposition
    if score >= 96:
        transposition_score = damerau_levenshtein_distance(correct_ans, user_ans)
        if transposition_score <= 1:
            return True
    
    # Check if string contains the same words in different orders
    any_order_score = fuzz.token_sort_ratio(correct_ans, user_ans)
    if any_order_score >= 99:
        return True

    return False