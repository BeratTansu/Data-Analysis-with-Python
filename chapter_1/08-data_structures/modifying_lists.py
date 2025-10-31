#%% modifying_lists.py
# Examples about modifying lists (index assignment, slice assignment, mutating methods)
# Run each cell (#%%) independently to see isolated outputs.

#%% 1) Index assignment (assign to a single element)
print("=== 1) Index assignment ===")
L = [11, 13, 22, 32]
print("before:", L)
L[2] = 10   # changes third element (index 2)
print("after L[2]=10 ->", L)
print()

#%% 2) Slice assignment (replace subsequence with another list)
print("=== 2) Slice assignment ===")
L = [11, 13, 22, 32]
print("before:", L)
L[1:3] = [4]   # replace elements at indices 1 and 2 with a single-element list [4]
print("after L[1:3] = [4] ->", L)
print()

#%% 3) Deleting elements by index or slice
print("=== 3) Deleting elements ===")
L = [0, 1, 2, 3, 4, 5]
print("before:", L)
del L[2]       # remove element at index 2
print("after del L[2] ->", L)
del L[1:3]     # remove a slice (indices 1 and 2)
print("after del L[1:3] ->", L)
print()

#%% 4) append, extend, insert
print("=== 4) append, extend, insert ===")
L = [1, 2, 3]
L.append(4)             # add single element at end
print("after append(4) ->", L)
L.extend([5, 6])        # extend by iterable: adds 5 and 6
print("after extend([5,6]) ->", L)
L.insert(0, 0)          # insert value 0 at index 0
print("after insert(0,0) ->", L)
print()

#%% 5) remove, pop, clear
print("=== 5) remove, pop, clear ===")
L = ['a', 'b', 'c', 'b']
print("before:", L)
L.remove('b')   # removes first occurrence of 'b'
print("after remove('b') ->", L)
p = L.pop()     # removes and returns last element
print("pop() returned", p, "and list is now", L)
p0 = L.pop(0)   # pop at index 0
print("pop(0) returned", p0, "and list is now", L)
L.clear()       # remove all elements
print("after clear() ->", L)
print()

#%% 6) reverse and sort (in-place) vs reversed/sorted (non-mutating)
print("=== 6) reverse & sort vs reversed & sorted ===")
L = [3, 1, 4, 2]
print("original:", L)
L.reverse()   # in-place reversal
print("after L.reverse() ->", L)
L.sort()      # in-place sort ascending
print("after L.sort() ->", L)
# non-mutating variants
L2 = [3, 1, 4, 2]
print("sorted(L2) ->", sorted(L2))   # returns new sorted list, L2 unchanged
print("reversed(L2) ->", list(reversed(L2)))  # reversed returns iterator, so list() to see it
print("L2 after calling sorted/reversed ->", L2)
print()

#%% 7) sort with key and reverse=True
print("=== 7) sort with key and reverse ===")
words = ["apple", "Banana", "cherry", "date"]
print("original words:", words)
# sort case-insensitive:
words_sorted = sorted(words, key=str.lower)
print("sorted(words, key=str.lower):", words_sorted)
# sort by length descending in-place:
words.sort(key=len, reverse=True)
print("words.sort(key=len, reverse=True) ->", words)
print()

#%% 8) Aliasing and mutation: modifying one reference affects others
print("=== 8) Aliasing and mutation ===")
orig = [ [1,2], [3,4] ]
alias = orig
copy_shallow = orig.copy()    # shallow copy of top-level list
print("orig:", orig)
alias[0].append(99)
print("after alias[0].append(99): orig ->", orig, "copy_shallow ->", copy_shallow)
# modifying top-level element via assignment
alias[0] = ["changed"]
print("after alias[0] = ['changed']: orig ->", orig, "copy_shallow ->", copy_shallow)
print()

#%% 9) Copying lists: shallow vs deepcopy
print("=== 9) shallow vs deep copy ===")
import copy
nested = [[0], [1]]
shallow = nested.copy()
deep = copy.deepcopy(nested)
nested[0].append(7)
print("after nested[0].append(7): nested ->", nested)
print("shallow ->", shallow)  # inner list shared
print("deep ->", deep)        # independent
print()

#%% 10) Common pitfalls and tips (mutable default arg example)
print("=== 10) Pitfalls: mutable default argument ===")
def bad_accumulator(x, lst=[]):
    lst.append(x)
    return lst

def good_accumulator(x, lst=None):
    if lst is None:
        lst = []
    lst.append(x)
    return lst

print("bad_accumulator(1) ->", bad_accumulator(1))
print("bad_accumulator(2) ->", bad_accumulator(2), "(same list reused -> pitfall)")
print("good_accumulator(1) ->", good_accumulator(1))
print("good_accumulator(2) ->", good_accumulator(2), "(new list each call)")
print()

#%% 11) Exercises
print("=== 11) Exercises (try these) ===")
# EX1: Given L = [10, 20, 30, 40, 50], replace the middle three elements with [99].
L = [10,20,30,40,50]
L[1:4] = [99]
print(L)
# EX2: Show how to remove all occurrences of value 'x' from a list using a while loop and then using list comprehension.
L = [1,2,3,2,4,2]
x = 2
L_filtered = [v for v in L if v != x]
print(L_filtered)

# EX3: Given nested = [[1],[2],[3]], demonstrate shallow copy problem and fix it with deepcopy.
print("Try EX1-EX3 by editing this file or testing in REPL.")
print()

#%% 12) Main reminder
def main():
    print("This module shows list modification techniques. Run cells individually to experiment.")

if __name__ == "__main__":
    main()