import random

variables = "Foo Bar Baz Bing".split()
scores = random.sample(range(1, 11), len(variables))

print("*" * 30)
print("\n")
print("With 'varable' left aligned")
for varable, score in zip(variables, scores):
    print(f"{varable:<10} | {score}")

print("*" * 30)
print("\n")
print("With 'varable' right aligned")
for varable, score in zip(variables, scores):
    print(f"{varable:>15} | {score}")

print("*" * 30)
print("\n")
print("With 'varable' center aligned")
for varable, score in zip(variables, scores):
    print(f"{varable:^5} | {score}")
