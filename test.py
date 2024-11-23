# # Define test function
# from hash_table import HashSet, HashMap
# def test_hash_tables():
#     print("Testing HashSet with Chaining")
#     hash_set_chain = HashSet("Chain", (31, 10))
#     hash_set_chain.insert("hello")
#     hash_set_chain.insert("world")
#     print("Inserted hello and world")
#     print("Find hello:", hash_set_chain.find("hello"))
#     print("Find world:", hash_set_chain.find("world"))
#     print("Find test:", hash_set_chain.find("test"))
#     print("Current table:", hash_set_chain)

#     print("\nTesting HashSet with Linear Probing")
#     hash_set_linear = HashSet("Linear", (31, 10))
#     hash_set_linear.insert("hello")
#     hash_set_linear.insert("world")
#     print("Inserted hello and world")
#     print("Find hello:", hash_set_linear.find("hello"))
#     print("Find world:", hash_set_linear.find("world"))
#     print("Find test:", hash_set_linear.find("test"))
#     print("Current table:", hash_set_linear)

#     print("\nTesting HashSet with Double Hashing")
#     hash_set_double = HashSet("Double", (31, 37, 10, 10))
#     hash_set_double.insert("hello")
#     hash_set_double.insert("world")
#     print("Inserted hello and world")
#     print("Find hello:", hash_set_double.find("hello"))
#     print("Find world:", hash_set_double.find("world"))
#     print("Find test:", hash_set_double.find("test"))
#     print("Current table:", hash_set_double)

#     print("\nTesting HashMap with Chaining")
#     hash_map_chain = HashMap("Chain", (31, 4))
#     hash_map_chain.insert(("hello", "world"))
#     hash_map_chain.insert(("foo", "bar"))
#     print("Inserted ('hello', 'world') and ('foo', 'bar')")
#     print("Find 'hello':", hash_map_chain.find("hello"))
#     print("Find 'foo':", hash_map_chain.find("foo"))
#     print("Find 'test':", hash_map_chain.find("test"))
#     print("Current table:", hash_map_chain)

#     print("\nTesting HashMap with Linear Probing")
#     hash_map_linear = HashMap("Linear", (31, 4))
#     hash_map_linear.insert(("hello", "world"))
#     hash_map_linear.insert(("foo", "bar"))
#     print("Inserted ('hello', 'world') and ('foo', 'bar')")
#     print("Find 'hello':", hash_map_linear.find("hello"))
#     print("Find 'foo':", hash_map_linear.find("foo"))
#     print("Find 'test':", hash_map_linear.find("test"))
#     print("Current table:", hash_map_linear)

#     print("\nTesting HashMap with Double Hashing")
#     hash_map_double = HashMap("Double", (31, 37, 10, 4))
#     hash_map_double.insert(("hello", "world"))
#     hash_map_double.insert(("foo", "bar"))
#     print("Inserted ('hello', 'world') and ('foo', 'bar')")
#     print("Find 'hello':", hash_map_double.find("hello"))
#     print("Find 'foo':", hash_map_double.find("foo"))
#     print("Find 'test':", hash_map_double.find("test"))
#     print("Current table:", hash_map_double)

# # Run the test function
# test_hash_tables()



from library import MuskLibrary, JGBLibrary
from dynamic_hash_table import DynamicHashSet
from prime_generator import set_primes, get_next_size
import sys
import re

def read_data(file_name):
    with open(file_name, "r") as file:
        number_of_books = int(file.readline().strip())
        book_titles = []
        texts = []
        for _ in range(number_of_books):
            book_titles.append(file.readline().strip())
            texts.append(file.readline().strip().split())
    return book_titles, texts

def DynamicHashSetTest(words):
    print("DynamicHashSet")
    set_primes([47, 23, 11])
    dhs = DynamicHashSet("Chain", (10, get_next_size()))
    try:
        for word in words:
            # print(word,words)
            dhs.insert(word)
            # print(a)
            print(f"Word: {word:<12} \tLoad: {dhs.get_load():<.12f}")
            if dhs.get_load() > 0.5:
                # print('abcd')
                print("DYNAMIC HASH TABLE NOT IMPLEMENTED")
                break
        else:
            # print('yo')
            print(dhs)
    except Exception as e:
        if str(e) == "Table is full":
            print("DYNAMIC HASH TABLE NOT IMPLEMENTED")

    print("-" * 350)


book_titles, texts = read_data("input.txt")
DynamicHashSetTest(texts[1])