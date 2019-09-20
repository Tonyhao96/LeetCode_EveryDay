#1122_Relative Sort Array
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        Dict={val:i for i, val in enumerate(arr2)}
        def sortmethod(val):
            index=Dict.get(val,-1)
            return (1, val) if index==-1 else (0, index)
        return sorted(arr1,key=sortmethod)