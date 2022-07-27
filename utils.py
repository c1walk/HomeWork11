import json

__data = []


def load_candidates_from_json(path):
    global __data
    with open(path, 'r', encoding='UTF-8') as file:
        __data = json.load(file)
    return __data


def get_candidate(candidate_id):
    for candidate in __data:
        if candidate["id"] == candidate_id:
            return {
                'name': candidate['name'],
                'position': candidate['position'],
                'picture': candidate['picture'],
                'skills': candidate['skills'],
            }
        return {'not_found': 'Ушел на обед'}


def get_candidates_by_name(candidates_name):
    return [candidate for candidate in __data if candidates_name.lower() in candidate['name'].lower()]


def get_candidates_by_skill(skill_name):
    pass

