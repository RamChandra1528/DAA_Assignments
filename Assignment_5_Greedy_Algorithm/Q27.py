from collections import deque

class Solution:
    def pageFaults(self, N, C, pages):
        # Create a queue to represent pages in memory and a set for quick look-up
        page_queue = deque()
        page_set = set()
        page_faults = 0
        
        for page in pages:
            # If the page is not in the set, it's a page fault
            if page not in page_set:
                # If memory is full, remove the oldest page
                if len(page_queue) >= C:
                    oldest_page = page_queue.popleft()
                    page_set.remove(oldest_page)
                
                # Add the new page to the set and the queue
                page_queue.append(page)
                page_set.add(page)
                page_faults += 1
        
        return page_faults


solution = Solution()
N = 9
C = 3
pages = [1, 2, 3, 1, 4, 2, 3, 4, 5]
print(solution.pageFaults(N, C, pages))  
