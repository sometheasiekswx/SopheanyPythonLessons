l = [2,3,4,2,2,2]
item_to_stop_at=4
for item in l:
    
    if item == item_to_stop_at:
        break
    print(item)

if __name__ == '__main__':
    N = int(input())
    
    list_value = []
    
    for i in range(0, N, 1):
        command = input() # "insert 0 5" "print" 'insert 1 2' 'remove 7'
        commands = command.split(' ') # ['insert', '0', '5'], ]['print'] ['insert', '1', '2'] ['remove', '7']0
        
        command_0 = commands[0] # "insert" "print" 'insert' 'remove'
        
        if command_0 == 'insert':
            i = int(commands[1])
            e = int(commands[2])
            list_value.insert(i,e)
            
        elif command_0 == 'print':
            print(list_value)
            
        elif command_0 == 'remove':
            e = int(commands[1])
            if e in list_value:
                list_value.remove(e)  
                 
        elif command_0 == 'append':
            e = int(commands[1])
            list_value.append(e)
            
        elif command_0 == 'sort':
            list_value.sort()
            
        elif command_0 == 'pop':
            list_value.pop()
            
        elif command_0 == 'reverse':
            list_value.reverse()
            
# Tuple

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    print(hash(tuple(integer_list)))

# Split and join

    def split_and_join(line):
    # write your code here
        string = line.split(' ')
        string_2 = '-'.join(string)
        return string_2
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)