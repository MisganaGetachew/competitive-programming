class Solution:
    def reverse(self, x: int) -> int:

        negative = False
        if x < 0:
          stringInt = str(x) 
          stringIntNew = stringInt[1:]
          negative = True
        else:
            stringIntNew = str(x)
        reversed = int(stringIntNew[::-1])
        positiveRange = (2 ** 31 ) - 1 
        negativeRange = -1 * (2 ** 31)
        if reversed > 0 and reversed > positiveRange:
            return 0
        elif reversed < 0 and reversed < negativeRange:
            return 0
        else:
            if negative:
                return -reversed
            else:
                return reversed


