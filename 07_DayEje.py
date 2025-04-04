#LEVEL 1#
it_companies = {'Google, Apple,Microsoft'}
it_companies.add ('Twitter')
it_companies.update(['Company1', 'Company2', 'Company3'])
it_companies.remove('Company1')  

#Level 2#
A.union(B)
A.intersection(B)
A.issubset(B)
A.isdisjoint(B)
A.update(B)
B.update(A)
A.symmetric_difference(B)
del A
del B

#LEVEL 3#
ages_set = set(ages)
print("List length:", len(ages))
print("Set length:", len(ages_set))
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print("Number of unique words:", len(unique_words))

