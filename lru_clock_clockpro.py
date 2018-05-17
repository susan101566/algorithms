import random

DEBUG = 0
numDistinctPages = 1000

def fakePageTable(numPages):
    result = {}
    for i in xrange(numPages):
        pageBytes = 'pagecontent' + str(i)
        result[str(i)] = pageBytes
    return result

class Memory:
    entries = fakePageTable(numDistinctPages)

    @staticmethod
    def get(pageId):
        return Memory.entries.get(str(pageId), None)

##################### LRUCache
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return '[{0}: {1}]'.format(self.key, self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        start = self.head
        result = []
        while start != None:
            result.append(str(start))
            start = start.next
        result.append("(None)")    
        return '->'.join(result)  

    def moveToFront(self, node):
        # Already the head
        if node == self.head:
            return

        # Empty
        if self.head == None and self.tail == None:
            self.head = node
            self.tail = node
            node.prev = None
            node.next = None
            return

        if node == self.tail:
            self.tail = self.tail.prev

        # Assume node is one in the linked list
        if node.prev != None:
            node.prev.next = node.next
        if node.next != None:
            node.next.prev = node.prev
        node.next = self.head
        self.head.prev = node
        self.head = node

    def removeLast(self):
        node = self.tail
        if self.tail.prev:
            self.tail.prev.next = None
        self.tail = self.tail.prev
        node.prev = None
        node.next = None
        return node

class LRUCache:
    def __init__(self, size):
        self.maxSize = size
        self.hitCount = 0
        self.missCount = 0
        self.name = 'LRU'

        self.recencyList = LinkedList()
        self.mapping = {} # pageId -> Node

    def access(self, pageId):
        if pageId in self.mapping: # cache hit
            self.hitCount += 1
            self.recencyList.moveToFront(self.mapping[pageId])
        else: # cache miss
            self.missCount += 1
            # full, evict last one
            if len(self.mapping) == self.maxSize:
                node = self.recencyList.removeLast()
                del self.mapping[node.key]
            value = Memory.get(pageId)
            node = Node(pageId, value)
            self.recencyList.moveToFront(node)
            self.mapping[pageId] = node
        return self.mapping[pageId].value

##################### CLOCK

class Clock:
    def __init__(self, size):
        self.maxSize = size
        self.hitCount = 0
        self.missCount = 0
        self.name = 'Clock'

        self.referenceBits = [0] * size
        self.pageIdsInBuffer = [None] * size
        self.clockHand = 0
        self.mapping = {} # pageId -> (value, index)

    def access(self, pageId):
        if pageId in self.mapping: # cache hit
            self.hitCount += 1
        else:
            self.missCount += 1
            while self.referenceBits[self.clockHand] == 1:
                self.referenceBits[self.clockHand] = 0
                self.clockHand = (self.clockHand + 1) % self.maxSize

            # Actually evict in the cache
            oldPageId = self.pageIdsInBuffer[self.clockHand]
            if oldPageId:
                del self.mapping[oldPageId]

            value = Memory.get(pageId)
            entry = (value, self.clockHand)
            self.mapping[pageId] = entry
            self.pageIdsInBuffer[self.clockHand] = pageId
        # set reference bit
        self.referenceBits[self.mapping[pageId][1]] = 1
        return self.mapping[pageId][0]

##################### CLOCKPRO

class ClockPro:
    def __init__(self, size):
        self.maxSize = size
        self.hitCount = 0
        self.missCount = 0
        self.name = 'Clock-Pro'

        # maxSize = hotCount + coldCount
        self.hotCount = size / 3
        self.coldCount = size - self.hotCount
        self.testCount = size

        # [[pageId, referenceBit]..]
        self.hotPages = [[None, 0]] * self.hotCount
        self.coldPages = [[None, 0]] * self.coldCount
        self.testPages = [None] * self.testCount

        self.hotHand = 0 # [0, self.hotCount)
        self.coldHand = 0 # [0, self.coldCount)
        self.testHand = 0 # [0, self.testCount)

        # Resident pages. Note on index for mapping: 
        # [0, self.hotCount) -> in hotPages
        # [self.hotCount, self.maxSize) -> in coldPages
        self.mapping = {} # pageId -> [value, index]
        self.testMapping = {} # pageId -> index into testPages

    def debugState(self, msg):
        if not DEBUG:
            return
        print '***' * 10
        print msg
        print 'hotHand: {0}, coldHand: {1}, testHand: {2}'.format(self.hotHand, self.coldHand, self.testHand)
        print 'hotPages' + str(self.hotPages)
        print 'coldPages' + str(self.coldPages)
        print 'testPages' + str(self.testPages)
        print 'mapping'
        for k, v in self.mapping.iteritems():
            print str(k) + ': ' + str(v)
        print 'testMapping'
        for k, v in self.testMapping.iteritems():
            print str(k) + ': ' + str(v)
        print '***' * 10

    # Run until hotHand points at a hotPage whose refBit is 0
    def findHotIndex(self):
        while self.hotPages[self.hotHand][1] == 1:
            self.hotPages[self.hotHand][1] = 0
            self.hotHand = (self.hotHand + 1) % self.hotCount

    # Run until coldHand points at a coldPage whose refBit is 0, promoting to hot
    # the ones whose refbit is 1 when the coldHand sweeps over them
    def runColdHand(self):
        while self.coldPages[self.coldHand][1] == 1:
            # For every coldPage with refBit = 1, promote to hotPage
            self.findHotIndex() # Find a spot for it
            coldPageId, _ = self.coldPages[self.coldHand]
            assert coldPageId != None
            hotPageId, _ = self.hotPages[self.hotHand]

            # The demoted hot page goes to coldPages
            if hotPageId: # make sure dictionary points to the right index
                self.coldPages[self.coldHand] = [hotPageId, 0]
                self.mapping[hotPageId] = [self.mapping[hotPageId][0], self.coldHand + self.hotCount]
            else:
                self.coldPages[self.coldHand] = [None, 0]

            # The promoted cold page goes to hotPages
            self.hotPages[self.hotHand] = [coldPageId, 0]
            self.mapping[coldPageId] = [self.mapping[coldPageId][0], self.hotHand]
            self.hotHand = (self.hotHand + 1) % self.hotCount
            self.coldHand = (self.coldHand + 1) % self.coldCount

    def addToColdPage(self, pageId, value):
        self.runColdHand()
        coldPageId = self.coldPages[self.coldHand][0]

        # Empty slot, add to it straight away
        if coldPageId == None:
            self.coldPages[self.coldHand] = [pageId, 0]
            self.mapping[pageId] = [value, self.coldHand + self.hotCount]
            self.coldHand = (self.coldHand + 1) % self.coldCount
            return

        # Actually evict the entry
        del self.mapping[coldPageId]
        
        # Add to test pages
        self.addToTestPage(coldPageId)

        # Add pageId to the slot
        self.coldPages[self.coldHand] = [pageId, 0]
        self.mapping[pageId] = [value, self.coldHand + self.hotCount]
        self.coldHand = (self.coldHand + 1) % self.coldCount

    def addToTestPage(self, coldPageId):
        assert coldPageId not in self.testMapping
        # Get rid of wherever the test hand is pointing at
        if len(self.testMapping) == self.testCount:
            testPageId = self.testPages[self.testHand]
            assert testPageId != None
            del self.testMapping[testPageId]
            self.testMapping[coldPageId] = self.testHand
            self.testPages[self.testHand] = coldPageId
            self.testHand = (self.testHand + 1) % self.testCount
            return

        # There must be an empty slot, find it
        index = -1
        for i in xrange(self.testCount):
            if self.testPages[(self.testHand + i) % self.testCount] == None:
                index = (self.testHand + i) % self.testCount
                break
        assert index >= 0
        self.testMapping[coldPageId] = index
        self.testPages[index] = coldPageId

    def addToHotPage(self, pageId, value):
        self.findHotIndex()
        hotPageId = self.hotPages[self.hotHand][0]
        if hotPageId == None:
            self.hotPages[self.hotHand] = [pageId, 0]
            self.mapping[pageId] = [value, self.hotHand]
            return

        hotPageValue = self.mapping[hotPageId][0]
        # Demote to coldPage
        self.hotPages[self.hotHand] = [None, 0]
        del self.mapping[hotPageId]
        self.addToColdPage(hotPageId, hotPageValue)
        self.addToHotPage(pageId, value)

   def access(self, pageId):
        # cache hit, set reference bit, return value (no fancy swapping logic)
        if pageId in self.mapping:
            self.hitCount += 1
            value, index = self.mapping[pageId]
            # set reference bit (the page could be in hotPages or coldPages)
            pageBuffer = self.hotPages if index < self.hotCount else self.coldPages
            pageIndex = index if index < self.hotCount else index - self.hotCount
            pageBuffer[pageIndex][1] = 1
            self.debugState('hit')
            return value

        self.missCount += 1
        value = Memory.get(pageId)

        # cache miss
        # In test period?
        if pageId in self.testMapping:
            testIndex = self.testMapping[pageId]
            del self.testMapping[pageId]
            self.testPages[testIndex] = None
            self.addToHotPage(pageId, value)
            self.debugState('miss in test')
            return
 
        # Warm up? This section is optional, but Clock-Pro is particularly bad 
        # when there's nothing hot at the beginning because we'd only be using 
        # a percentage of the actual cache
        if len(self.mapping) < self.hotCount:
            self.addToHotPage(pageId, value)
            self.debugState('miss warmup in hot')
            return
        if len(self.mapping) < self.maxSize:
            self.addToColdPage(pageId, value)
            self.debugState('miss warm up in cold')
            return
      
        self.addToColdPage(pageId, value)
        self.debugState('miss in cold')
        return value

#####################

def testRandom(cache):
    for _ in xrange(100000):
        num = int(random.random() * numDistinctPages)
        cache.access(num)
    print cache.name
    print 'Cache hit: {0}'.format(cache.hitCount)
    print 'Cache miss: {0}'.format(cache.missCount)

m = 100
clockpro = ClockPro(m)
clock = Clock(m)
lru = LRUCache(m)

testRandom(clockpro)
testRandom(clock)
testRandom(lru)

