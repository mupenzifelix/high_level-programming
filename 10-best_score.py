#!/usr/bin/python3


def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not a_dictionary:
        return None

    # Sort by value and get the last item (highest value)
    return sorted(a_dictionary.items(), key=lambda item: item[1])[-1][0]
