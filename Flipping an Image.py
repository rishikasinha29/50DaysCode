from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        
        for i in range(n):
            # Step 1: Flip horizontally
            # This can be done by reversing the list in place
            image[i].reverse()
            
            # Step 2: Invert the image (0 becomes 1, and 1 becomes 0)
            for j in range(n):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
                # Alternatively, you can use: image[i][j] = 1 - image[i][j]
        
        return image

