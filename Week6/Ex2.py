class FibonacciHeapNode:
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance
        self.marked = False
        self.parent = None
        self.child = None
        self.degree = 0
        self.next = self
        self.prev = self

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.nodes = {}

    def insert(self, node, distance):
        new_node = FibonacciHeapNode(node, distance)
        self.nodes[node] = new_node
        if self.min_node:
            new_node.next = self.min_node.next
            new_node.prev = self.min_node
            self.min_node.next = new_node
            new_node.next.prev = new_node
            if distance < self.min_node.distance:
                self.min_node = new_node
        else:
            self.min_node = new_node

    def extract_min(self):
        min_node = self.min_node
        if min_node:
            if min_node.child:
                child = min_node.child
                while True:
                    if child.child:  # Kiểm tra child có con không
                        next_child = child.child
                        child.parent = None
                        child.marked = False
                        self._add_to_root_list(child)
                        child = next_child
                        if child == min_node.child:
                            break
                    else:
                        self._add_to_root_list(child)  # Thêm vào danh sách root nếu không có con
                        break
            min_node.parent = None
            if min_node == min_node.next:
                self.min_node = None
            else:
                self.min_node = min_node.next
                self._consolidate()
            del self.nodes[min_node.node]  # Xóa nút khỏi self.nodes
        return min_node
    def decrease_key(self, node, new_distance):
        if node not in self.nodes:
            return
        fib_node = self.nodes[node]
        if new_distance < fib_node.distance:
            fib_node.distance = new_distance
            parent = fib_node.parent
            if parent and new_distance < parent.distance:
                self._cut(fib_node, parent)
                self._cascading_cut(parent)
            if new_distance < self.min_node.distance:
                self.min_node = fib_node

    def _add_to_root_list(self, node):
        if self.min_node:
            node.next = self.min_node.next
            node.prev = self.min_node
            self.min_node.next = node
            node.next.prev = node
        else:
            node.next = node
            node.prev = node
        self.min_node = node

    def _consolidate(self):
        max_degree = int((2 * len(self.nodes)) ** 0.5)
        table = [None] * (max_degree + 1)
        nodes = list(self.nodes.values())

        for node in nodes:
            degree = node.degree
            while table[degree]:
                other = table[degree]
                if node.distance > other.distance:
                    node, other = other, node
                self._link(other, node)
                table[degree] = None
                degree += 1
            table[degree] = node

        self.min_node = None
        for node in table:
            if node:
                if self.min_node:
                    node.next = self.min_node.next
                    node.prev = self.min_node
                    self.min_node.next = node
                    node.next.prev = node
                    if node.distance < self.min_node.distance:
                        self.min_node = node
                else:
                    node.next = node
                    node.prev = node
                    self.min_node = node

    def _link(self, child, parent):
        child.prev.next = child.next
        child.next.prev = child.prev
        child.parent = parent
        if not parent.child:
            parent.child = child
            child.next = child
            child.prev = child
        else:
            child.prev = parent.child
            child.next = parent.child.next
            parent.child.next = child
            child.next.prev = child
        parent.degree += 1
        child.marked = False

    def _cut(self, child, parent):
        child.prev.next = child.next
        child.next.prev = child.prev
        parent.child = child.next if child == child.next else child
        parent.degree -= 1
        self._add_to_root_list(child)
        child.parent = None
        child.marked = False

    def _cascading_cut(self, node):
        parent = node.parent
        if parent:
            if not node.marked:
                node.marked = True
            else:
                self._cut(node, parent)
                self._cascading_cut(parent)
def dijkstra(n, edges, s, t):
    graph = {}
    for u, v, w in edges:
        if u not in graph:
            graph[u] = {}
        graph[u][v] = w

    distances = {}
    previous = {}
    heap = FibonacciHeap()

    for node in graph:
        distances[node] = float('inf')
        previous[node] = None
        heap.insert(node, distances[node])

    distances[s] = 0
    heap.decrease_key(s, 0)

    while heap.min_node and heap.min_node.node != t:
        u = heap.extract_min().node
        if u in graph:
            for v, weight in graph[u].items():
                alt = distances[u] + weight
                if alt < distances[v]:
                    distances[v] = alt
                    previous[v] = u
                    heap.decrease_key(v, alt)

    if t not in previous:
        return -1

    path = []
    while t:
        path.insert(0, t)
        t = previous[t]

    return distances[path[0]]

# Đọc dữ liệu vào
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

# Tìm đường đi ngắn nhất
result = dijkstra(n, edges, s, t)
print(result)
