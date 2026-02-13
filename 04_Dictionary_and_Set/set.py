"""
A set is:
- Unordered
- Unindexed
- Does not allow duplicate values
- Mutable (can add/remove items)

Sets are written using curly braces {}.
"""

# ---------------------------------
# 1. Creating a Set
# ---------------------------------

numbers = {1, 2, 3, 4, 4, 5}

print("Set values:", numbers)   # Duplicate 4 will be removed


# ---------------------------------
# 2. Adding Elements
# ---------------------------------

numbers.add(6)
print("After adding 6:", numbers)


# ---------------------------------
# 3. Removing Elements
# ---------------------------------

numbers.remove(3)     # Removes specific value
print("After removing 3:", numbers)

numbers.discard(10)   # No error if value not found
print("After discard 10:", numbers)


# ---------------------------------
# 4. Pop Element
# ---------------------------------

removed_value = numbers.pop()   # Removes random element
print("Removed value:", removed_value)
print("Set after pop:", numbers)


# ---------------------------------
# 5. Set Operations
# ---------------------------------

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
print("Union:", set1.union(set2))

# Intersection
print("Intersection:", set1.intersection(set2))

# Difference
print("Difference (set1 - set2):", set1.difference(set2))

# Symmetric Difference
print("Symmetric Difference:", set1.symmetric_difference(set2))


# ---------------------------------
# 6. Checking Membership
# ---------------------------------

print("Is 2 in set1?", 2 in set1)


# ---------------------------------
# 7. Clearing a Set
# ---------------------------------

temp_set = {10, 20, 30}
temp_set.clear()
print("After clear:", temp_set)


# ---------------------------------
# 8. Frozen Set (Immutable Set)
# ---------------------------------

frozen = frozenset([1, 2, 3])
print("Frozen set:", frozen)

# frozen.add(4)  # This will give error because frozen set is immutable
