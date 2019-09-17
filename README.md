# Python-Based-Compiler
Python Application that uses a library called PLY to parse and then compile code. It uses lexographical symbols and a tree hierarchy in order to break down the read text file. Then it looks for symbols and then turns into a tree. The tree is then read from the leaves and then the result is determined in the root.
# Example Input/Output
Input:
<br/>
{{}{}{print(['abc', 'def', ['ghi', 'jkl', ['mno', 'pqrs', ['tuv', 'wxyz']]]][2][2][2][1][0] in 'the quick brown fox jumps over the lazy dog.' or ['abc', 'def', ['ghi', 'jkl', ['mno', 'pqrs', ['tuv', 'wxyz']]]][2][2][2][1] in 'the quick brown fox jumps over the lazy dog.' and [[[[[["substring"]]]]]][0][0][0][0][0][0] in "There is no sub-string in this string");}}
<br/>
Output: <br />
False
