from p1 import *
class MaxHeap:
    def __init__(self):
        self.heap = []  # Initialize an empty list to store hospitals

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, hospital):
        self.heap.append(hospital)
        self.heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty():
            return None
        
        max_hospital = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return max_hospital

    def max_hospital(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index]['rating'] > self.heap[parent_index]['rating']:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if (left_child_index < len(self.heap) and
                self.heap[left_child_index]['rating'] > self.heap[largest]['rating']):
            largest = left_child_index

        if (right_child_index < len(self.heap) and
                self.heap[right_child_index]['rating'] > self.heap[largest]['rating']):
            largest = right_child_index

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)

    def display_hospitals(self):
        if self.is_empty():
            print("Max Heap is empty.")
            return
        print("Max Heap (from highest to lowest rating):")
        for hospital in self.heap:
            print(f"Hospital: {hospital['name']}, Rating: {hospital['rating']}")
        print("")  # For better readability

