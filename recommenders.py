"""
Here lives our movie recommenders functions
"""
import random
from utils import Movies


def random_recommender(query={"Toy Story": 5}, k=3):
    """Toy random recommender

    Args:
        query (dict, optional): User query. Defaults to {"Toy Story": 5}.
        k (int, optional): _description_. Defaults to 3.

    Returns:
        _type_: _description_
    """
    random.shuffle(Movies)
    topk = Movies[:k]
    return topk


if __name__ == "__main__":
    top3 = random_recommender()
    print(top3)
