#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#
class Solution:
    # hashmap
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 0: return "NaN"
        negative = (numerator > 0) ^ (denominator > 0)
        numerator, denominator = abs(numerator), abs(denominator)
        remainder_map = {}
        fraction_part = ''
        count = 0
        int_part = 0
        if numerator > denominator:
            int_part = numerator // denominator
            remainder = numerator % denominator
            numerator = remainder
        
        # NOTE: when the numerator < denominator, the numerator itself is a remainder
        remainder_map[numerator] = count
        count += 1

        recur_begin = 0
        recur_end = 0

        while numerator:
            numerator *= 10
            fraction = numerator // denominator
            remainder = numerator % denominator
            # print(fraction, remainder)
            # when remainder accured before, we get a recurred fraction
            if remainder in remainder_map:
                fraction_part += str(fraction)
                recur_begin = remainder_map[remainder]
                recur_end = count
                break
            else:
                fraction_part += str(fraction)
                remainder_map[remainder] = count
                count += 1
                numerator = remainder
        # print(remainder_map)
        # print("fraction part: ",fraction_part)
        # print("recur area", recur_begin, recur_end)
        if recur_end:
            res = str(int_part) + '.' + fraction_part[:recur_begin] + "(" + fraction_part[recur_begin:recur_end+1] + ")"
        elif fraction_part:
            res = str(int_part) + '.' + fraction_part
        else:
            res = str(int_part)
        if res == "0": return "0"
        return res if not negative else "-"+res

