# GeoHealth: Efficient Hospital Search and Management System

## Objective
The **GeoHealth** project is a comprehensive hospital management system designed to efficiently manage and search hospital data using advanced data structures like **R-Tree**, **Trie**, **Heap**, and **Stack**. It supports features such as location-based hospital searches, prefix-based search queries, priority-based hospital ratings, and search history tracking, providing a user-friendly and efficient solution for emergency and non-emergency scenarios.

---

## Features
1. **Hospital Management:**
   - Add, delete, and retrieve hospital information.
   - Prioritize high-rated hospitals for emergencies.

2. **Location-Based Searches:**
   - Utilize **R-Tree** for efficient spatial indexing of hospital locations.
   - Perform range and nearest neighbor queries.

3. **Name-Based Searches:**
   - Use **Trie** for prefix-based search, enabling autocomplete and efficient retrieval of hospital names and addresses.

4. **Hospital Ratings:**
   - Maintain hospital ratings with a **MaxHeap** to quickly access the highest-rated hospital.

5. **Search History:**
   - Track user searches using a **Stack** to provide quick access to recent searches.

---

## Data Structures and Their Applications
1. **R-Tree**: 
   - Efficiently indexes spatial data for location-based hospital searches.
   - Operations: 
     - Insertion: **O(log n)**  
     - Deletion: **O(log n)**  
     - Search: **O(log n + k)** (nearest neighbors)

2. **MaxHeap**:
   - Maintains and prioritizes hospitals based on ratings.
   - Operations: 
     - Insertion: **O(log n)**  
     - Maximum Retrieval: **O(1)**

3. **Trie**:
   - Facilitates fast prefix-based lookups for hospital names and addresses.
   - Operations: 
     - Insertion/Search/Deletion: **O(m)** (where *m* is the length of the key)

4. **Stack**:
   - Tracks user search history for quick reference.
   - Operations: 
     - Push/Pop/Peek: **O(1)**  
     - View History: **O(n)**

---

## R-Tree Structure Example
```
Root (Internal Node) [Bounding Box: (40.7242, -74.0049) - (40.758896, -73.9176)]
|-- Internal Node 1 [Bounding Box: (40.7242, -74.0049) - (40.7373, -73.9352)]
|   |-- Leaf Node 1
|   |   |-- City Hospital (40.73061, -73.935242)
|   |   |-- St. Peter's Hospital (40.7306, -73.9352)
|   |-- Leaf Node 2
|       |-- Metro (40.730610, -73.935242)
|       |-- Sunshine Medical Clinic (40.730610, -73.935242)
|-- Internal Node 2 [Bounding Box: (40.7357, -74.0031) - (40.758896, -73.9744)]
|   |-- Leaf Node 3
|   |   |-- Northside Hospital (40.7357, -73.9918)
|   |   |-- Westside Hospital (40.7373, -74.0031)
```

---

## Challenges
1. **Sensor Accuracy**: Handling inconsistencies in geographical data with optimized algorithms.
2. **Efficient Retrieval**: Balancing memory usage and speed for large datasets.
3. **User Experience**: Designing intuitive and fast systems for real-world applications.

---

## Future Enhancements
- Add support for real-time updates and notifications.
- Integrate GPS for outdoor navigation.
- Implement machine learning algorithms for predictive analytics and smarter decision-making.

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/GeoHealth.git
   ```
2. Navigate to the project folder:
   ```bash
   cd GeoHealth
   ```
3. Compile and run the code:
   ```bash
   g++ main.cpp -o geohealth
   ./geohealth
   ```

---
