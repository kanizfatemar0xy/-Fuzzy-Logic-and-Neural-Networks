"""Educational password meter using fuzzy memberships; NOT a security guarantee.

This function never logs, stores, transmits, or returns the secret itself.
Use dummy/test passwords only. It is not a substitute for modern breach-aware meters.
"""
from dataclasses import dataclass
from getpass import getpass

@dataclass(frozen=True)
class PasswordRating:
    score: int
    label: str
    weak_membership: float
    medium_membership: float
    strong_membership: float


def _triangle(x: float, left: float, peak: float, right: float) -> float:
    if not left <= peak <= right:
        raise ValueError('invalid triangle')
    if x == peak:
        return 1.0
    if x <= left or x >= right:
        return 0.0
    return (x - left) / (peak - left) if x < peak else (right - x) / (right - peak)


def rate_password(secret: str) -> PasswordRating:
    """Rate a test string; output a bounded score and fuzzy strength classes.

    This is a teaching heuristic, not an estimate of guessability or compromise.
    """
    if not isinstance(secret, str):
        raise TypeError('secret must be a string')
    if not secret:
        return PasswordRating(0, 'Weak', 1.0, 0.0, 0.0)

    length_score = min(len(secret) / 18.0, 1.0) * 60.0
    groups = (
        any(c.islower() for c in secret),
        any(c.isupper() for c in secret),
        any(c.isdigit() for c in secret),
        any(not c.isalnum() and not c.isspace() for c in secret),
        any(c.isalpha() and not c.islower() and not c.isupper() for c in secret),
    )
    diversity_score = sum(groups) / 5.0 * 30.0
    unique_ratio = len(set(secret)) / len(secret)
    variety_score = unique_ratio * 10.0
    raw = max(0.0, min(100.0, length_score + diversity_score + variety_score))
    score = int(round(raw))

    weak = 1.0 if score <= 20 else max(0.0, (50.0 - score) / 30.0)
    medium = _triangle(score, 20, 50, 80)
    strong = 1.0 if score >= 80 else max(0.0, (score - 50.0) / 30.0)
    memberships = {'Weak': weak, 'Medium': medium, 'Strong': strong}
    label = max(memberships, key=memberships.get)
    return PasswordRating(score, label, weak, medium, strong)


if __name__ == '__main__':
    print('Educational demonstration only. Never enter a password used on a real account.')
    example = getpass('Enter a dummy test string (input hidden): ')
    rating = rate_password(example)
    print(f'Demonstration rating: {rating.label} ({rating.score}/100)')
