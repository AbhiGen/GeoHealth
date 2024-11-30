import math

# Euclidean distance formula to calculate the distance between two lat/long points
def calculate_distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    # Calculate the differences
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Convert the differences from degrees to kilometers
    km_per_degree_latitude = 111
    km_per_degree_longitude = 111 * math.cos(math.radians(lat1))

    # Euclidean formula
    distance = math.sqrt((dlat * km_per_degree_latitude) ** 2 + (dlon * km_per_degree_longitude) ** 2)
    return distance

# R-Tree Node class
# [Code for R-Tree remains unchanged]

# R-Tree Node class
class RTreeNode:
    # leaf node holds the actual data points like lat lon and rat
    # internal node does not hold data points directly intead it holds child nodes and organizez them by bounding boxes . it manages the heierachy of r tree
    # we set leaf node as false initally 
    # children array behaves ddirenelty based on type of node 
        # if internal node - it holds references to other node child nodes creating heorachial stricture
        # if leaf node -hold actual data points 
        # initally node is emtpy so children array also empty
    # bounding box is a rectangular area defined by max and min coordinates . encloses all nodes children 
        # for leaf node - enclose all data points 
        # for internal node - enclose all bounding boxes of its child node 
        # intially node as there are no children for node 
    def __init__(self, is_leaf=False):
        self.is_leaf = is_leaf
        self.children = []
        self.bounding_box = None  # Min and max lat/long for the node
    
    def insert(self, hospital):
        # Insert hospital, adjust bounding box, and split if needed
        if self.is_leaf:
            self.children.append(hospital)
            self.adjust_bounding_box()
            if len(self.children) > 4:  # Max capacity reached, split the node
                return self.split()
        else:
            # Insert in the child node that has the minimum bounding box overlap
            best_child = self.choose_best_child(hospital)
            new_node = best_child.insert(hospital)
            if new_node:  # A split occurred
                self.children.append(new_node)
                self.adjust_bounding_box()
        return None

    def adjust_bounding_box(self):
        if not self.children:
            return

        # Determine if the children are hospitals or nodes
        if self.is_leaf:
            min_lat = min(child["latitude"] for child in self.children)
            max_lat = max(child["latitude"] for child in self.children)
            min_lon = min(child["longitude"] for child in self.children)
            max_lon = max(child["longitude"] for child in self.children)
        else:
            min_lat = min(child.bounding_box[0][0] for child in self.children)
            max_lat = max(child.bounding_box[1][0] for child in self.children)
            min_lon = min(child.bounding_box[0][1] for child in self.children)
            max_lon = max(child.bounding_box[1][1] for child in self.children)

        self.bounding_box = ((min_lat, min_lon), (max_lat, max_lon))

    def split(self):
        # Split the node into two new nodes
        mid_index = len(self.children) // 2
        new_node = RTreeNode(is_leaf=self.is_leaf)
        new_node.children = self.children[mid_index:]
        self.children = self.children[:mid_index]
        self.adjust_bounding_box()
        new_node.adjust_bounding_box()
        return new_node

    def choose_best_child(self, hospital):
        best_child = None
        min_distance = float('inf')  # Initialize to infinity so any real distance is smaller

        # Get the hospital's latitude and longitude
        hospital_lat = hospital["latitude"]
        hospital_lon = hospital["longitude"]

        # Iterate through each child and calculate the distance to find the best one
        for child in self.children:
            # Get the child's bounding box coordinates (assuming lower-left corner for comparison)
            child_lat = child.bounding_box[0][0]
            child_lon = child.bounding_box[0][1]

            # Calculate the distance between the hospital and the child's bounding box corner
            distance = calculate_distance((child_lat, child_lon), (hospital_lat, hospital_lon))

            # Find the child with the minimum distance
            if distance < min_distance:
                min_distance = distance
                best_child = child

        return best_child


# R-Tree class
class RTree:
    def __init__(self):
        self.root = RTreeNode(is_leaf=True)

    def insert_hospital(self, hospital):
        new_node = self.root.insert(hospital)
        if new_node:  # Root split, create a new root
            new_root = RTreeNode(is_leaf=False)
            new_root.children = [self.root, new_node]
            new_root.adjust_bounding_box()
            self.root = new_root
    
    def search_nearest(self, user_location, max_results=3, distance_range=None):
        nearest_hospitals = []
        self._nearest_search(self.root, user_location, nearest_hospitals, max_results, distance_range)
        return sorted(nearest_hospitals, key=lambda h: calculate_distance(user_location, (h['latitude'], h['longitude'])))

    def _nearest_search(self, node, user_location, nearest_hospitals, max_results, distance_range):
        if node.is_leaf:
            for hospital in node.children:
                dist = calculate_distance(user_location, (hospital['latitude'], hospital['longitude']))
                if distance_range is None or dist <= distance_range:
                    nearest_hospitals.append(hospital)
        else:
            for child in node.children:
                self._nearest_search(child, user_location, nearest_hospitals, max_results, distance_range)
