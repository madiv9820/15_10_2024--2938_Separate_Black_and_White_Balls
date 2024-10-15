# 2938. Separate Black and White Balls

__Type:__ Medium <br>
__Topics:__ Two Pointers, String, Greedy <br>
__Companies:__ 1Kosmos <br>
__Leetcode Link:__ [Separate Black and White Balls](https://leetcode.com/problems/separate-black-and-white-balls/description/)
<hr>

There are `n` balls on a table, each ball has a color black or white. <br><br>
You are given a __0-indexed__ binary string `s` of length `n`, where `1` and `0` represent black and white balls, respectively. <br><br>
In each step, you can choose two adjacent balls and swap them. <br><br>
Return _the __minimum__ number of steps to group all the black balls to the right and all the white balls to the left._
<hr>

### Examples
    
- __Example 1:__ <br>
__Input:__ s = "101" <br>
__Output:__ 1 <br>
__Explanation:__ We can group all the black balls to the right in the following way:-<br> - Swap s[0] and s[1], s = "011". <br>
Initially, 1s are not grouped together, requiring at least 1 step to group them to the right.

- __Example 2:__ 
__Input:__ s = "100" <br>
__Output:__ 2 <br>
__Explanation:__ We can group all the black balls to the right in the following way: <br> - Swap s[0] and s[1], s = "010".<br>  - Swap s[1] and s[2], s = "001". <br>
It can be proven that the minimum number of steps needed is 2.

- __Example 3:__ 
__Input:__ s = "0111" <br>
__Output:__ 0 <br>
__Explanation:__ All the black balls are already grouped to the right.
<hr>

### Constraints:

- <code>1 <= n == s.length <= 10<sup>5</sup></code>
- `s[i]` is either `'0'` or `'1'`.
<hr>

### Hints:

- Every `1` in the string `s` should be swapped with every `0` on its right side.
- Iterate right to left and count the number of `0` that have already occurred, whenever you iterate on `1` add that counter to the answer.