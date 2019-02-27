class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here

        if not str or offset == None:
            return 

        offset = offset % (len(str))

        self.reverse(str, 0, len(str) - offset - 1)
        self.reverse(str, len(str) - offset, len(str) - 1)
        self.reverse(str, 0, len(str) - 1)

    def reverse(self, str, start, end):

        while start < end:
            temp = str[start]
            str[start] = str[end]
            str[end] = temp 

            start = start + 1
            end = end - 1
        
            