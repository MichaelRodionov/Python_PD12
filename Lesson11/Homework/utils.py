import json


def load_candidates(json_file) -> list[dict]:
    """
    Load candidates from JSON file.
    param file_json:
    :return: list with dictionaries of candidates
    """
    with open(json_file) as file:
        data = json.load(file)
        return data


def get_candidates_by_name(data, candidate_name) -> list[dict]:
    """
    Get candidates by name.
    param data: list with dictionaries with candidates
    param candidate_name: candidate name
    :return: list with dictionaries of candidates
    """
    candidates_list = []
    for candidate in data:
        if candidate_name.lower() in candidate['name'].lower():
            candidates_list.append(candidate)
    return candidates_list


def get_by_pk(data, pk) -> dict:
    """
    Get candidate by pk.
    param data: list with dictionaries with candidates
    param pk: candidate pk
    :return: candidate
    """
    for candidate in data:
        if candidate['id'] == pk:
            return candidate


def get_by_skill(data, skill) -> list[dict]:
    """
    Get candidates by skill.
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
