class Solutions:                                  # Class name
  def sort(self, nums : list[int]) -> list[int]:  # Function name with input and output
    return sorted([i*i for i in nums])            # Return the sorted list of squared elements of the input list
                                                  # Time Complexity is O(nlogn) because of sorting
                                                  # Space Complexity is O(n) because of the list comprehension
nums = [1, 0, -4, 7, -10]                         # Input list
solution = Solutions()                            # Class object
print(solution.sort(nums))                        # [0, 1, 16, 49, 100]