# 187. Repeated DNA Sequence

"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

    For example, "ACGAATTCCG" is a DNA sequence.

When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, 

return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. 

You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

 

Constraints:

    1 <= s.length <= 105
    s[i] is either 'A', 'C', 'G', or 'T'.


"""
s = "AAAAAAAAAAA"

def get_repeats(seq):

    res = set()
    seen = set()
    if len(seq) < 10:
        return []
    else:
        for i in range(len(seq)-9):
            chunk = seq[i:i+10]        
            if chunk in seen:
                res.add(chunk)
            else:
                seen.add(chunk)
        
        return list(res)
            
            
       
z = get_repeats(s)
print(z)

" O(n) time it takes N time to index and slice the array of length N"
"O(n) space complexity" 
