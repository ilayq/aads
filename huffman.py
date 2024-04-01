from collections import deque


class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def push(self, value):
        self.size += 1
        self.heap.append(value)
        pos = len(self.heap) - 1
        while value > self.heap[(pos - 1) // 2] and (pos - 1) // 2 >= 0:
            self.heap[(pos - 1) // 2], self.heap[pos] = self.heap[pos], self.heap[(pos - 1) // 2]
            pos = (pos - 1) // 2
            if pos == 0:
                break

    def pop(self):
        self.size -= 1
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        res = self.heap.pop()
        pos = 0
        while (2 * pos + 1 < len(self.heap) and \
                self.heap[pos] < self.heap[2 * pos + 1]) or \
                (2 * pos + 2 < len(self.heap) and self.heap[pos] < self.heap[2 * pos + 2]):
            maxson = 2 * pos + 1
            if 2 * pos + 2 < len(self.heap):
                if self.heap[2 * pos + 1] < self.heap[2 * pos + 2]:
                    maxson  = 2 * pos + 2
            self.heap[pos], self.heap[maxson] = self.heap[maxson], self.heap[pos]
            pos = maxson
        return res

    def top(self):
        return self.heap[0]

    def __len__(self):
        return self.size
    
    def __str__(self):
        return str(self.heap)


class Node:
    def __init__(self, val: int = 1, content: str = None, l=None, r=None):
        self.val = val
        self.content = content
        self.l = l
        self.r = r

    def __lt__(self, obj):
        return self.val < obj.val

    def __gt__(self, obj):
        return self.val >  obj.val



def encode(s):
    a = list(set(s))
    weights = dict()
    for char in s:
        if char not in weights:
            weights[char] = 0
        weights[char] += 1
    a.sort(key=lambda x: weights[x], reverse=True)
    weights = sorted(list(weights.values()), reverse=True)
    print(a, weights)
    n = len(a)
    h = Heap()

    if n <= 1:
        print(s.replace(s[0], '0'))
        return s.replace(s[0], '0')
    
    for i in range(n):
        a[i] = Node(content=a[i], val=-weights[i])
        h.push(a[i])

    while len(h) > 1:
        r, l = h.pop(), h.pop()
        new_val = l.val + r.val
        new_content = l.content+ r.content
        new_node = Node(val=new_val, content=new_content, r=r, l=l)
        h.push(new_node)

    q = deque()
    q.append((h.top(), ''))
    codes = {}
    while q:
        v, code = q.popleft()
        if len(v.content) == 1:
            codes[v.content] = code 
        if v.l:
            q.append((v.l, code + '0'))
        if v.r:
            q.append((v.r, code + '1'))

    for char in codes:
        s = s.replace(char, codes[char])
    print(codes)
    print(s)
    return s


if __name__ == '__main__':
    encode('aa')
