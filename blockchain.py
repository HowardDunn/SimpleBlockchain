import hashlib
import sys


class Block():

    def __init__(self):
        self.prev_block = None
        self.data = [] # you could call this transactions if you want


    def add_transaction(self,data):
        self.data.append(data)

    def get_hash(self):
        return hashlib.sha256(str(self.data).encode('utf-8')).hexdigest()

    def link(self,prev_block):
        self.prev_block = prev_block.get_hash()



class Blockchain():


    def __init__(self):

        self.blocks = [Block()] # empty genesis block

    def add_block(self,block):

        last_block = self.blocks[-1]
        block.link(last_block)
        self.blocks.append(block)



    def is_valid(self):


        for i,block in enumerate(self.blocks):

            if i == 0:

                continue # genesis block

            prev_block = self.blocks[i-1]
            if block.prev_block != prev_block.get_hash():
                return False

        return True



    def size(self):
        return sys.getsizeof(self)



    def print_chain(self):

        for i,block in enumerate(self.blocks):

            print()
            print("Block", i+1, ": ")
            print("Previous Block Hash: ", block.prev_block)

            print()
            for j,transaction in enumerate(block.data):

                print("Transaction ", j+1, ": ",transaction)

            if i == 0:

                print("Genesis Block")

    def rehash(self):

        for i, block in enumerate(self.blocks):

            if i == 0:
                continue  # genesis block

            prev_block = self.blocks[i - 1]
            block.prev_block = prev_block.get_hash()
    def num_blocks(self):


        return len(self.blocks)






