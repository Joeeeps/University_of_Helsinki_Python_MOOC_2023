# Write your solution here
string = input("Word: ")
LINE_WIDTH = 30

print(
    "*" * LINE_WIDTH,
    f"*{string:^{LINE_WIDTH-2}}*", #^ means centre
    "*" * LINE_WIDTH,
    sep='\n'
)
