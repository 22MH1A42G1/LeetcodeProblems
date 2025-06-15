class Solution(object):
    def maxDiff(self, num):
        str_num = str(num)

        # For max: replace the first digit that is not '9' with '9'
        for ch in str_num:
            if ch != '9':
                max_str = str_num.replace(ch, '9')
                break
        else:
            max_str = str_num  # all digits are '9'

        # For min: 
        if str_num[0] != '1':
            min_str = str_num.replace(str_num[0], '1')
        else:
            found = False
            for ch in str_num[1:]:
                if ch != '0' and ch != '1':
                    min_str = str_num.replace(ch, '0')
                    found = True
                    break
            if not found:
                min_str = str_num

        return int(max_str) - int(min_str)