import requests as r


def load_candidates(file_json):
    """
    Load candidates from a JSON file.
    param file_json:
    :return: list with dictionaries of candidates
    """
    response = r.get(file_json)
    data = response.json()
    return data


def get_by_pk(data, pk):
    """
    Get pk.
    param data: list with dictionaries with candidates
    param pk: candidate pk
    :return: candidate
    """
    for candidate in data:
        if candidate['pk'] == pk:
            return candidate


def get_by_skill(data, skill):
    """
    Get skill.
    param data: list with dictionaries of candidates
    param skill: candidate skill
    :return: list of dictionaries with candidates with general skills
    """
    candidates_ = []
    for candidate in data:
        for candidate_skill in candidate['skills'].lower().split(', '):
            if skill == candidate_skill:
                candidates_.append(candidate)
    return candidates_
