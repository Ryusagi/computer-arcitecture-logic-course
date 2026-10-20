def main():
   cache_size = int(input('add cache size\n'));
   command = input('add the program to check in the format <number number number...>\n');
   cache = [-1] * cache_size;
   command_list = command.split()
   print('===========================')
   print(f'Cache size: {cache_size}')
   print('Output:\n')
   hits = 0
   for num in command_list:
      block_val = int(num)
      line = block_val % cache_size
      hit = 0
      if (cache[line] == block_val):
         hit = 1
      hits += hit
      cache[line] = block_val
      print(f'Block {num} -> line {line} (Cache hit {hit})')

   print(f'Cache hits: {hits} Cache misses: {len(command_list) - hits}')

if __name__ == "__main__":
    main()