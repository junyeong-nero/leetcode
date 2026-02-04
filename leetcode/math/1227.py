# This question can be thought of more as a mathematical brainteaser than a computational problem.

# Let the first person be assigned seat 1, and the last person seat n.

#     By the time the last person arrives, all other seats (outside of 1 and n), will be taken
#         Remember, everyone from the second to second-last person will "take their own seat if it is still available" --> thus there's no way for any of the seats from 2 to n−1 to not be taken (as if they were still free, then the person assigned to that seat should've been able to take it)
#     Thus, the last person will have either seat 1 or n to take
#         By symmetry, the two probabilities are equal --> the first person picked a seat at random, and after this, the seat chosen was either (A) a seat from 2 to n−1, or (B) chosen at random --> thus seat 1 and n must be equally likely to be taken
#         Put another way, at no point in the question was there any reason that one seat would be more likely to be taken that the other (out of 1 and n)

# Thus, the probability must be 0.5, excluding the case where there is only 1 person.


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1
        return 0.5
        
