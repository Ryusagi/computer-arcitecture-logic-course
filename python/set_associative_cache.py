def cache_check(set, value):
   for val in set:
      if val==value:
         return 1
   return 0

def cache_insert(set, value):
    for i in range(len(set)):
        if set[i]==-1:
            set[i]=value
            return
    set[0] = value
    

def main():
   cache_size = int(input('add cache size\n'));
   set_size = int(input('add set size (number of ways)\n'));
   command = input('add the program to check in the format <number number number...>\n');
   cache = [[-1] * set_size for _ in range(cache_size)]
   command_list = command.split()
   print('===========================')
   print(f'Cache size: {cache_size} Set size: {set_size}')
   print('Output:\n')
   hits = 0
   for num in command_list:
      block_val = int(num)
      set_index = block_val % cache_size
      set = cache[set_index]
      hit = cache_check(set, block_val)
      if (hit==0):
       cache_insert(set, block_val)
      hits += hit
      print(f'Block {num} -> set index {set_index} (Cache hit {hit}) cache: {cache}')

   print(f'Cache hits: {hits} Cache misses: {len(command_list) - hits}')

if __name__ == "__main__":
    main()