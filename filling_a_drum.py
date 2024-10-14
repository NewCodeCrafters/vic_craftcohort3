# Create a simple App that fills an empty drum to 25 litres. The drum will be filled at 5 litres incrase every 1 second until it fills up

import time 

drum = 0

while drum < 25:
    start_time = time.time
    print(f"Drum contains {drum} litres")
    drum = drum + 5
    time.sleep(1)
end_time = time.time()
print(f"Drum is full. Volume: {drum}./nTime of completion{end_time}")
