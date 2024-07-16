# Problem: Heap Sort - https://practice.geeksforgeeks.org/problems/heap-sort/1

    def HeapSort(self, arr, n):
        #code here
        import heapq
        heap = arr.copy()
        heapq.heapify(heap)
        for i in range(n):
            arr[i] = heapq.heappop(heap)