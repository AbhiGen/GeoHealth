from p1 import *
from p2 import *
from p3 import *
from p5 import *

# Hospital Project class integrating R-Tree, Trie, and Heap
class HospitalProject:
    def __init__(self):
        self.rtree = RTree()
        self.trie_name = Trie()
        self.trie_address = Trie()
        self.hospitals = []

    def add_hospital(self, hospital):
        self.rtree.insert_hospital(hospital)
        self.trie_name.insert(hospital['name'], hospital)
        self.trie_address.insert(hospital['address'], hospital)
        self.hospitals.append(hospital)

    def find_hospital_by_name(self, partial_name):
        matched_hospitals = self.trie_name.search(partial_name)
        self.display_hospitals(matched_hospitals)
        return matched_hospitals

    def find_hospital_by_address(self, partial_address):
        matched_hospitals = self.trie_address.search(partial_address)
        self.display_hospitals(matched_hospitals)
        return matched_hospitals

    def display_hospitals(self, hospitals):
        # Make sure `hospitals` is a list and iterate through it
        if not hospitals:
            print("No hospitals found.")
            return
        
        # Display only the name and rating of each hospital
        for hospital in hospitals:
            print(f"Hospital: {hospital['name']}, Rating: {hospital['rating']}")

    def show_hospital_details(self, hospital):
        # Show detailed information of a single hospital
        print("\nHospital Details:")
        print(f"Name: {hospital['name']}")
        print(f"Address: {hospital['address']}")
        print(f"Rating: {hospital['rating']}")
        print(f"Latitude: {hospital['latitude']}")
        print(f"Longitude: {hospital['longitude']}")
        print(f"Contact: {hospital['contact']}")

    def find_nearest_hospitals(self, user_location, max_results=3):
        return self.rtree.search_nearest(user_location, max_results)
    
    def find_nearest_hospitals_within_range(self, user_location, range_km):
        # Search for hospitals within the specified range
        return self.rtree.search_nearest(user_location, max_results=3, distance_range=range_km)
    
     #Method to get the best hospitals within a given distance range using MaxHeap
    def best_hospitals_within_range(self, user_location, distance_range=1):
    # Find all hospitals within the given distance range.
        nearest_hospitals = self.rtree.search_nearest(user_location, distance_range=distance_range)
        if not nearest_hospitals:
            return "No hospitals found within the specified distance range."

    # Create a MaxHeap to store hospitals based on their ratings.
        max_heap = MaxHeap()
        for hospital in nearest_hospitals:
            max_heap.insert(hospital)
    
    # Extract hospitals with the highest rating from the MaxHeap.
        best_hospitals = []
        if not max_heap.is_empty():
            highest_rating = max_heap.heap[0]['rating']
            while not max_heap.is_empty() and max_heap.heap[0]['rating'] == highest_rating:
                best_hospitals.append(max_heap.extract_max())

        return best_hospitals
        
    


# Example data and project initialization
hospitals = [
    {"name": "City Hospital", "latitude": 40.73061, "longitude": -73.935242, "rating": 4.7, "address": "123 Main St, New York, NY", "contact": "555-1234"},
    {"name": "New City Hospital", "latitude": 40.73061, "longitude": -73.935242, "rating": 4.8, "address": "123 Main St, New York, NY", "contact": "555-1234"},
    {"name": "Green Valley Hospital", "latitude": 40.758896, "longitude": -73.985130, "rating": 4.5, "address": "456 Green Rd, New York, NY", "contact": "555-5678"},
    {"name": "Metro Health Center", "latitude": 40.730610, "longitude": -73.935242, "rating": 4.2, "address": "789 Metro Blvd, New York, NY", "contact": "555-6789"},
    {"name": "Sunshine Medical Clinic", "latitude": 40.730610, "longitude": -73.935242, "rating": 4.2, "address": "321 Sunshine Ave, New York, NY", "contact": "555-4321"},
    {"name": "General Hospital", "latitude": 40.7580, "longitude": -73.9855, "rating": 4.1, "address": "101 General St, New York, NY", "contact": "555-0011"},
    {"name": "St. Peter's Hospital", "latitude": 40.7306, "longitude": -73.9352, "rating": 4.4, "address": "202 St. Peter's Rd, New York, NY", "contact": "555-0022"},
    {"name": "Northside Hospital", "latitude": 40.7357, "longitude": -73.9918, "rating": 4.6, "address": "303 Northside Blvd, New York, NY", "contact": "555-0033"},
    {"name": "Eastside Medical Center", "latitude": 40.7312, "longitude": -73.9998, "rating": 4.3, "address": "404 Eastside Ave, New York, NY", "contact": "555-0044"},
    {"name": "Westside Hospital", "latitude": 40.7373, "longitude": -74.0031, "rating": 4.5, "address": "505 Westside Blvd, New York, NY", "contact": "555-0055"},
    {"name": "Lakeside Medical Clinic", "latitude": 40.7402, "longitude": -73.9823, "rating": 4.2, "address": "606 Lakeside Ave, New York, NY", "contact": "555-0066"},
    {"name": "Downtown Medical Center", "latitude": 40.7242, "longitude": -74.0049, "rating": 4.4, "address": "707 Downtown St, New York, NY", "contact": "555-0077"},
    {"name": "Southview Hospital", "latitude": 40.7367, "longitude": -73.9722, "rating": 4.1, "address": "808 Southview Blvd, New York, NY", "contact": "555-0088"},
    {"name": "East River Hospital", "latitude": 40.7394, "longitude": -73.9744, "rating": 4.6, "address": "909 East River Rd, New York, NY", "contact": "555-0099"},
    {"name": "Harbor Medical Center", "latitude": 40.7331, "longitude": -73.9580, "rating": 4.3, "address": "1010 Harbor Ave, New York, NY", "contact": "555-0100"},
    {"name": "Community Health Center", "latitude": 40.7408, "longitude": -73.9176, "rating": 4.5, "address": "1111 Community Blvd, New York, NY", "contact": "555-0111"},
]


# Initialize the project and add hospitals
project = HospitalProject()
for hospital in hospitals:
    project.add_hospital(hospital)

# Example usage
user_location = (40.730610, -73.935242)

# Find nearest hospitals within <1 km, <2 km, <5 km
print("\nNearest Hospitals within 1 km:")
nearest_hospitals_1km = project.find_nearest_hospitals_within_range(user_location, 1)
for hospital in nearest_hospitals_1km:
    print(f"{hospital['name']} - {hospital['rating']} stars")
print()

print("\nNearest Hospitals within 2 km:")
nearest_hospitals_2km = project.find_nearest_hospitals_within_range(user_location, 2)
for hospital in nearest_hospitals_2km:
    print(f"{hospital['name']} - {hospital['rating']} stars")
print()

print("\nNearest Hospitals within 5 km:")
nearest_hospitals_5km = project.find_nearest_hospitals_within_range(user_location, 5)
for hospital in nearest_hospitals_5km:
    print(f"{hospital['name']} - {hospital['rating']} stars")
print()

print("\nSearch results for hospitals with 'City' in their name:")
search_results = project.find_hospital_by_name("Green")

for hospital in search_results:
    print(f"Hospital: {hospital['name']}, Address: {hospital['address']}")
print()

print("Search results for hospitals with address ")
search_results1=project.find_hospital_by_address("465 Green Rd, New York, NY")

for hospital in search_results1:
    print(print(f"Hospital: {hospital['name']}, Address: {hospital['address']}"))

print()
print("All Hospital details ")
print(project.display_hospitals(hospitals))

print()
print("best hospitals in case of emergency")
print(project.best_hospitals_within_range(user_location))


print()

for hospital in hospitals:
    project.show_hospital_details(hospital)
"""
def get_search_history(self):
        # Return the entire search history
        return self.search_history

def display_search_history(self):
        if not self.search_history:
            print("No search history available.")
        else:
            print("Search History:")
            for entry in self.search_history:
                query_type = entry["type"]
                query = entry["query"]
                result_count = len(entry["results"])
                print(f"Search Type: {query_type.capitalize()}, Query: '{query}', Results: {result_count} hospital(s)")

search_history = project.get_search_history()
print(search_history)  # Prints the search history list

# Display the search history in a more readable format
project.display_search_history()    """                                                                                                                                                       