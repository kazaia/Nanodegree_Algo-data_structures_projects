"""
A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.
Use your knowledge of linked lists and hashing to create a blockchain implementation.
"""
import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
    @staticmethod 
    def create_genesis():
        return Block(datetime.now(), "0", datetime.now())


b1 = [Block.create_genesis()]
blocks_num = 5


print("Block #Genesis.")
print("Hash: %s" % b1[0].hash)

for i in range(1, blocks_num):
    b1.append(Block(b1[i-1].hash, "Block number %d" % i, datetime.now()))
    print("--------------")
    print("Block #%d:" % i)
    print("Hash: %s" % b1[-1].hash)


    
    

           
