def func():
    string_input = raw_input()
    input_list = string_input.split()
    print sorted(input_list, key=len)
    
func();
