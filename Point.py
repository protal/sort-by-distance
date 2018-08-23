class Point(object):
    def __init__(self, location):
        self.lat = location['lat']
        self.long = location['long']
    def sort_by_distance(self, positions):
        positions.sort(key = lambda p: ((p['location']['lat'] - self.lat)**2 + (p['location']['long'] - self.long)**2)**0.5)
        return positions
        # return sorted(positions, key=lambda e: ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5)