Combine entire code into a single line - join using \n
Use regular expressions to match comments
* // to match single line comments
1. .* matches every thing except newline char
* \* matches the block comment and line comment
1. .|\n matching any character including newline
2. the *? is a greedy match
​
Once the substitution using regex is compeleted, split the code using \n and
filter out empty lines.