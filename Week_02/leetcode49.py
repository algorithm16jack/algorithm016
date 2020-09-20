class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #dict = {}
        dict = collections.defaultdict(list)
        for item in strs:
            tuple_item = sorted(item)
            tuple_item = tuple(tuple_item)
            dict[tuple_item].append(item)

        return dict.values()

        ## official
        #ans = collections.defaultdict(list)
        #for s in strs:
        #    ans[tuple(sorted(s))].append(s)
        #return ans.values()
