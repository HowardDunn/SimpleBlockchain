import blockchain
import random
import time
import statistics as s
import matplotlib.pyplot as plt

def test(num_blocks):
    blckchain = blockchain.Blockchain()

    rand2 = random.randint(1,10)

    for i in range(0,num_blocks):

        block = blockchain.Block()
        for j in range(rand2):
            rand3 = random.randint(1, 100)
            block.add_transaction(rand3)

        blckchain.add_block(block)



    blckchain.blocks[1].add_transaction(57)
    start_time = time.time()
    blckchain.rehash()
    time_taken = time.time() - start_time

    return time_taken

# 0.00476527214050293


avg_times = []
num_blocks = [10,100,1000,10000,100000,1000000]
print("starting")
for num_block in num_blocks:
    times = []
    for i in range(0,10):
        tim =  test(num_block)

        times.append(tim)

    print("Average time for ", num_block, " blocks:", s.mean(times))
    avg_times.append(s.mean(times))

print("end")

plt.plot(num_blocks, avg_times)

plt.xlabel('Number of Blocks')
plt.ylabel('Average Time Taken to Rehash')
plt.savefig("time_to_rehash_vs_num_blocks.png")
plt.show()

