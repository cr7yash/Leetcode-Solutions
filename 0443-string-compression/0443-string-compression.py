class Solution:
    def compress(self, chars: List[str]) -> int:
        
        # chars = ["a","a","b","b","c","c","c"]
        # s = ""
        # aa is consecutive
        # if group length is 1 then a
        # otherwise it should be char followed by length, so a2
        # store it in the input arr
        # chars = ["a","2","b","2","c","3"]

        # return the length of input array which is 6

        current = 0  # The Pen (Write)
        next = 0     # The Scout (Read)

        # 1. Drive the loop with the Scout
        while next < len(chars):
            current_char = chars[next]
            count = 0

            # 2. Scout runs ahead to count. Pen stays completely still!
            while next < len(chars) and chars[next] == current_char:
                next += 1
                count += 1   # We increment count, NOT current!

            # 3. Scout is done. Now the Pen writes.
            chars[current] = current_char
            current += 1

            if count > 1:
                for digit in str(count):
                    chars[current] = digit
                    current += 1
                    
        return current
            









