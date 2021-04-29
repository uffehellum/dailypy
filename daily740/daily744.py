import unittest


# Implement an LFU (Least Frequently Used) cache.
# It should be able to be initialized with a cache size n, and contain the following methods:
#
# set(key, value): sets key to value.
#   If there are already n items in the cache and we are adding a new item,
#   then it should also remove the least frequently used item.
#   If there is a tie, then the least recently used key should be removed.
#
# get(key): gets the value at key.
#   If no such key exists, return null.
#
# Each operation should run in O(1) time.

class TestDaily744(unittest.TestCase):

    def test_base(self):
        c = LeastFrequentlyUsedCache(2)
        c.set("a", 1)
        c.set("b", 2)

        self.assertEqual(1, c.get("a"))
        self.assertEqual(2, c.get("b"))
        self.assertIsNone(c.get("c"))
        c.set("c", 3)
        self.assertIsNone(c.get("a"))
        self.assertEqual(2, c.get("b"))
        self.assertEqual(3, c.get("c"))


class LeastFrequentlyUsedCache:
    def __init__(self, maxCount):
        self.max_count = maxCount
        self.cache = dict()
        self.queue = LeastFrequentUseQueue()

    def __str__(self):
        return str(self.cache)

    def set(self, key, value):
        if key in self.cache:
            old = self.cache[key]
            self.queue.remove(old)
        else:
            if len(self.cache) == self.max_count:
                old = self.queue.remove_first()
                del(self.cache[old.key])
        new = CacheEntry(key, value)
        self.cache[key] = new
        self.queue.add(new)

    def get(self, key):
        if not key in self.cache:
            return None
        entry = self.cache[key]
        self.queue.access(entry)
        return entry.value


class CacheEntry:
    def __init__(self, key, value):
        self.next = None
        self.prev = None
        self.usagecount = 0
        self.key = key
        self.value = value


class UsageQueue:
    """double linked list of entries with same usage count, oldest first"""
    def __init__(self, usagecount: int):
        self.usagecount = usagecount
        self.firstentry = None
        self.lastentry = None
        self.nextqueue = None
        self.prevqueue = None

    def add(self, entry: CacheEntry):
        if self.firstentry is None:
            self.firstentry = entry
            self.lastentry = entry
        else:
            entry.prev = self.lastentry
            self.lastentry.next = entry
            self.lastentry = entry

    def remove(self, entry: CacheEntry):
        if entry.prev is None:
            self.firstentry = entry.next
            if self.firstentry:
                self.firstentry.prev = None
        else:
            entry.prev.next = entry.next
            if entry.next:
                entry.next.prev = entry.prev

    def remove_first(self):
        if self.firstentry is None:
            raise Exception('There are no entries with %s usages' % self.usagecount)
        r = self.firstentry
        self.firstentry = r.next
        if self.firstentry:
            self.firstentry.prev = None
        else:
            self.lastentry = None
        r.next = None
        return r


class LeastFrequentUseQueue:
    """double linked list of queues"""

    def __init__(self):
        self.firstqueue = None
        self.lastqueue = None
        self.queues = dict()

    def add(self, entry):
        """create a new value that has been added to the cache"""
        if entry.usagecount != 0:
            raise Exception("New entry does not have usage count zero as expected", entry)
        if entry.usagecount in self.queues:
            q = self.queues[entry.usagecount]
            q.add(entry)
            return
        q = UsageQueue(entry.usagecount)
        q.add(entry)
        self.queues[q.usagecount] = q
        if self.firstqueue is None:
            self.lastqueue = q
            self.firstqueue = q
        else:
            q.nextqueue = self.firstqueue
            self.firstqueue.prevqueue = q
            self.firstqueue = q

    def remove(self, entry: CacheEntry):
        """remove a value that has been removed from the cache"""
        q = self.queues[entry.usagecount]
        q.remove(entry)
        self._remove_queue_if_empty(q)

    def _remove_queue_if_empty(self, q: UsageQueue):
        if q.firstentry is None:
            del self.queues[q.usagecount]
            if q.prevqueue is None:
                self.firstqueue = q.nextqueue
                if q.nextqueue:
                    q.nextqueue.prevqueue = None
            else:
                q.prevqueue.nextqueue = q.nextqueue
                if q.nextqueue:
                    q.nextqueue.prevqueue = q.prevqueue

    def access(self, entry: CacheEntry):
        """a value has been read so increase access count"""
        q = self.queues[entry.usagecount]
        entry.usagecount += 1
        if entry.usagecount in self.queues:
            qnew = self.queues[entry.usagecount]
        else:
            qnew = UsageQueue(entry.usagecount)
            self.queues[qnew.usagecount] = qnew
            qnew.nextqueue = q.nextqueue
            q.nextqueue = qnew
            qnew.prevqueue = q
            if qnew.nextqueue:
                qnew.nextqueue.prevqueue = qnew
        qnew.add(entry)
        self._remove_queue_if_empty(q)

    def remove_first(self):
        """cache is full, so remove the least frequently used entry and return it"""
        if self.firstqueue is None:
            return None
        q = self.firstqueue
        entry = q.remove_first()
        self._remove_queue_if_empty(q)
        return entry
