# Part of Low-Key Anki from MIA.
# https://massimmersionapproach.com/table-of-contents/anki/low-key-anki/low-key-anki-summary-and-installation/
#
# They also credit https://eshapard.github.io/.

# from aqt.utils import showInfo
from aqt.gui_hooks import (
    # reviewer_will_answer_card,
    reviewer_did_answer_card,
    reviewer_did_show_question,
    reviewer_did_show_answer,
)
from anki.hooks import schedv2_did_answer_review_card


# Probably don't need to use all these hooks, but it can't hurt.


# 250%
DEFAULT_EASE_FACTOR = 2500


def reset_ease_on_show(card):
    """
    Action. Reset the ease factor to the default when a card's question or
    answer is shown.

    :param card: (Card) Card object.
    """
    card.factor = DEFAULT_EASE_FACTOR

reviewer_did_show_question.append(reset_ease_on_show)
reviewer_did_show_answer.append(reset_ease_on_show)


def reset_ease_on_answer(reviewer, card, ease):
    """
    Action. Reset the ease factor to the default when a card has been answered.

    Not sure if this hook runs after Anki has changed the card's factor while
    rescheduling.

    :param reviewer: (aqt.reviewer.Reviewer) Reviewer object.
    :param card: (card) Card object.
    :param ease: (int) Ease 1 to 4, representing the buttons again to easy.
    """
    card.factor = DEFAULT_EASE_FACTOR

reviewer_did_answer_card.append(reset_ease_on_answer)


def v2_reset_ease_on_answer(card, ease, early):
    """
    Action. Reset the ease factor to the default when a card has been answered
    and the new scheduler is used.

    :param card: (Card) Card object.
    :param ease: (int) Ease 1 to 4, representing the buttons again to easy.
    :param early: (bool) If the card is reviewed early (using a filtered deck).
    """
    card.factor = DEFAULT_EASE_FACTOR

schedv2_did_answer_review_card.append(v2_reset_ease_on_answer)


# def force_good_button(ease_tuple, reviewer, card):
#     """
#     Filter. Pretend the good button is always pushed to keep the ease factor
#     from changing.
#
#     :param ease_tuple: (bool, int) A boolean expressing whether the reviewer
#     should continue with rating the card, and an integer expressing the ease at
#     which the card should be rated, where ease is between 1 and 4 representing
#     the four answer buttons (1 being again and 4 being easy).
#     :param reviewer: aqt.reviewer.Reviewer.
#     :param card: Card object.
#     :returns: The ease tuple.
#     """
#     return (ease_tuple[0], 3)
#
# reviewer_will_answer_card.append(force_good_button)
