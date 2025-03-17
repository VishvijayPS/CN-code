import time
pkt=[3,6,2,1,4]
bucket_size=5
storage=0
leak_rate=2
j=0
for i in range(0,len(pkt)):
    time.sleep(0.5)
    i=pkt[i]
    if (i+storage<=bucket_size):
        storage+=i
        print(f"Packet of size {i} added. Bucket size: {storage}/{bucket_size}")
        if(storage<leak_rate):
            continue
        else:
            storage=storage-leak_rate
            print(f"Bucket size after time {j}:{storage}/{bucket_size}")
    else:
        print(f"Packet of size {i} dropped.")
    time.sleep(1/leak_rate)
    j=j+1