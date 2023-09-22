# post_processing/post_processor.py
from fuzzywuzzy import fuzz

def compare_entities(truth_dict, prediction_dict, fuzzy_threshold=80):
    """
    Compare two dictionaries of entities using fuzzy string matching.

    Args:
        truth_dict (dict): Dictionary of true entities.
        prediction_dict (dict): Dictionary of predicted entities.
        fuzzy_threshold (int): Threshold for fuzzy matching (default is 80).

    Returns:
        Tuple: A tuple containing the number of correct, missed, and false positive entities.
    """
    correct_entities = 0
    missed_entities = 0
    false_positive_entities = 0

    for entity_type, truth_values in truth_dict.items():
        if entity_type in prediction_dict:
            predicted_values = prediction_dict[entity_type]
        else:
            predicted_values = []

        for truth_value in truth_values:
            truth_words = truth_value.lower().split()
            found = False

            for predicted_value in predicted_values:
                predicted_words = predicted_value.lower().split()
                word_similarity = max(fuzz.ratio(truth_word, predicted_word) for truth_word in truth_words for predicted_word in predicted_words)

                if word_similarity >= fuzzy_threshold:
                    correct_entities += 1
                    found = True
                    break

            if not found:
                missed_entities += 1

        for predicted_value in predicted_values:
            predicted_words = predicted_value.lower().split()
            found = False

            for truth_value in truth_values:
                truth_words = truth_value.lower().split()
                word_similarity = max(fuzz.ratio(truth_word, predicted_word) for truth_word in truth_words for predicted_word in predicted_words)

                if word_similarity >= fuzzy_threshold:
                    found = True
                    break

            if not found:
                false_positive_entities += 1

    return correct_entities, missed_entities, false_positive_entities
