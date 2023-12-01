#!/usr/bin/python3
"""
This module contain one funtion that prints a text with 2 new lines
    after each of these characters: ., ? and :

>>> text_indentation("Red. Dri? nice: to meet, you;haha.")
Red.
<BLANKLINE>
Dri?
<BLANKLINE>
nice:
<BLANKLINE>
to meet, you;haha.
<BLANKLINE>
>>> text_indentation("salamu alikum folks")
salamu alikum folks
>>> text_indentation()

"""


def text_indentation(text=""):
    """Return None, rints a text with 2 new lines after each
        of these characters: ., ? and :

    >>> text_indentation("Red. Dri? nice: to meet, you;haha.")
    Red.
    <BLANKLINE>
    Dri?
    <BLANKLINE>
    nice:
    <BLANKLINE>
    to meet, you;haha.
    <BLANKLINE>
    >>> text_indentation("salamu alikum folks")
    salamu alikum folks
    >>> text_indentation(22)
    Traceback (most recent call last):
    TypeError: text must be a string
    >>> text_indentation(("red", "dd"))
    Traceback (most recent call last):
    TypeError: text must be a string
    >>> text_indentation(["red", "dd"])
    Traceback (most recent call last):
    TypeError: text must be a string

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lst = [".", "?", ":"]

    for dlm in lst:
        text = text.replace(dlm, dlm + "\n")

    text_list = text.split("\n")
    for i in range(len(text_list)):
        text_list[i] = text_list[i] + "\n\n"
    text_list[i] = text_list[i][:-2]
    for ele in text_list:
        print(ele.strip(" "), end="")
    text_list[-1] = text_list[-1].rstrip("\n")


if __name__ == "__main__":
    import doctest
    flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS | doctest.FAIL_FAST
    flag = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    doctest.testmod(optionflags=flag)
