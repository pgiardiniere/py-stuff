# Given two strings: write a function to decide if one is perm of other.


# Determine whether s2 is a permutation of s1.
# We have O(n^2) time complexity. O(n) space complexity.
def is_permutation(s1, s2):
    if len(s2) > len(s1):
        return False

    for c in s2:
        if c not in s1:
            return False

    return True


# cheating by not implementing my own sorting algorithm, but it'll do.
def is_strict_permutation(s1, s2):
    if len(s2) != len(s1):
        return False

    if sorted(s1) == sorted(s2):
        return True


def is_hashed_strict_perm(s1, s2):
    if len(s2) != len(s1):
        return False

    d1, d2 = {}, {}
    for i, c in enumerate(s1):
        d1[hash(c)] = i

    for i, c in enumerate(s2):
        d2[hash(c)] = i

    # Still don't understand how to make these comparisons in a single pass
    # for key1, key2 in d1, d2:


if __name__ == '__main__':
    s1 = 'hello'
    s2 = 'leo'
    print(is_permutation(s1, s2))

    # Wait, is_permutation is just checking whether or not we have arrangement
    # strictly speaking, a permutation would be the same length.

    """
    Hint 1:
    Describe what it means for two strings to be permutations of each other.
    Now, look at that definition you provided.
    Can you check the strings against that definition?
    """

    # Yeah, as I thought. Playing with definition.

    """
    Hint 2:
    There is one solution that is O(N log N) time.
    Another solution uses more space, but is O(N) time.
    """

    # Okay, so the O(N log N) solution implies an in-place sort on string

    # And the O(N) solution implies use of a (two?) hashtable(s).
    # Actually, we could have 2 strings of equal length and hashtable,
    # but with different num instances of chars hashing to same thing.

    # If I'm using a strict hashtable and not a hashset, then it will work.

    s1 = 'hello'
    s2 = 'olleh'
    print(is_strict_permutation(s1, s2))

    """
    Hint 3:
    Could a hash table be useful?
    """
    # Yeah, already understood fam.

    """
    Hint 4:
    Two strings that are permutations should have the same characters,
    but in possibly different orders.
    Can you make the orders look the same?
    """
    # Pretty sure hashing would 'order' the stuff too.