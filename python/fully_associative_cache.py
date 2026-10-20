def cache_check(cache, value):
   for val in cache:
      if val==value:
         return 1
   return 0

def cache_insert(cache, value):
    for i in range(len(cache)):
        if cache[i]==-1:
            cache[i]=value
            return
    set[0] = value
    

def main():
   cache_size = int(input('add cache size\n'));
   command = input('add the program to check in the format <number number number...>\n');
   cache = [-1] * cache_size
   command_list = command.split()
   print('===========================')
   print(f'Cache size: {cache_size}')
   print('Output:\n')
   hits = 0
   for num in command_list:
      block_val = int(num)
      hit = cache_check(cache, block_val)
      if (hit==0):
       cache_insert(cache, block_val)
      hits += hit
      print(f'Block {num} -> (Cache hit {hit}) cache: {cache}')

   print(f'Cache hits: {hits} Cache misses: {len(command_list) - hits}')

if __name__ == "__main__":
    main()