# josephus
Solving Josephus problem in binary operations

## Observation of results

| n        | 2^a + L       | f(n) = 2L + 1 |
|----------|:-------------:|:-------------:|
| 1 	     | 1 + 0 	       | 2 * 0 + 1 = 1 |
| 2 	     | 2 + 0 	       | 2 * 0 + 1 = 1 |
| 3 	     | 2 + 1 	       | 2 * 1 + 1 = 3 |
| 4 	     | 4 + 0 	       | 2 * 0 + 1 = 1 |
| 5 	     | 4 + 1 	       | 2 * 1 + 1 = 3 |
| 6 	     | 4 + 2 	       | 2 * 2 + 1 = 5 |
| 7 	     | 4 + 3 	       | 2 * 3 + 1 = 7 |
| 8 	     | 8 + 0 	       | 2 * 0 + 1 = 1 |
| 9 	     | 8 + 1 	       | 2 * 1 + 1 = 3 |
| 10 	     | 8 + 2 	       | 2 * 2 + 1 = 5 |
| 11 	     | 8 + 3 	       | 2 * 3 + 1 = 7 |
| 12 	     | 8 + 4 	       | 2 * 4 + 1 = 9 |

## Binary method

We need to get the biggest possible power of 2 in binary - basically
the most significant bit (MSB). In the original Josephus problem there
were n = 41 knights, in binary it is 101001.

MSB gives us largest power of 2 (j), so we can n XOR j getting 1001 (9),
(which basically is our L). Shift right (multiply by 2) gives 10010 (18).
Adding one, via OR 1, gives 10011 (19), which is the answer.
