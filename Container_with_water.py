def max_area(heights):
    left, right = 0, len(heights) - 1
    current_max = 0
    
    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        current_area = width * height
        
        current_max = max(current_max, current_area)
        
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return current_max


if __name__ == "__main__":
    # Example test case
    heights = [1,8,6,2,5,4,8,3,7]
    result = max_area(heights)
    print(f"Max area: {result}")