# key is the url
# value is the local path
# size is the size of the file
import requests
import os
class doublyLinkedList:
    def __init__(self, key, value, size):
        self.key = key
        self.value = value
        self.size = size
        self.start = None
        self.end = None

# return [url, local_path, size]
class Lru_cache:
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.current_size = 0
        self.hm = {}

        self.left = doublyLinkedList(0,0,0)
        self.right = doublyLinkedList(0,0,0)

        self.left.end = self.right
        self.right.start = self.left
    def get(self, key):
        if key in self.hm:
            node = self.hm[key]
            self.remove(node)
            self.push(node)
            return [node.key, node.value, node.size]
        return ""
    def remove(self, node):
        end = node.end
        start = node.start

        end.start = start
        start.end = end

    def push(self, node):
        last = self.right.start

        node.start = last
        node.end = self.right

        self.right.start = node
        last.end = node

    def insert(self, key):
        size, value = self.downloadImageToLocal(key)
        self.current_size += size

        while (self.current_size > self.cache_size):
            least_used = self.left.end
            least_used_size = least_used.size
            least_used_key = least_used.key
            least_used_value = least_used.value
            self.remove(least_used)
            print(self.hm)
            del self.hm[least_used_key]
            self.deleteLocalImage(least_used_value)

            self.current_size -= least_used_size
        newnode = doublyLinkedList(key,value,size)
        self.hm[key] = newnode
        self.push(newnode)
        return [newnode.key, newnode.value, newnode.size]

    def downloadImageToLocal(self, url):
        r = requests.get(url, headers= {"user-agent": "curl/7.84.0",
            "accept": "*/*"})
        size = len(r.content)
        local_path = "./local_cache/"+url.split("/")[-1]
        print(r.status_code, r)
        
        with open(local_path, "wb") as wf:
            wf.write(r.content)
        print(url + " file downloaded at " + local_path)
        return size, local_path
    def deleteLocalImage(self, local_path):
        os.remove(local_path)
        print(local_path + " File deleted")


