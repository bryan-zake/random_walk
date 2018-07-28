class RandomArgsParser():
    def parse_args(argv, str_arg):
        arg_value = 0
        args = [i for i,x in enumerate(argv) if str_arg in x]
        try:
            arg_value = int(argv[args[0] + 1])
        except:
            print("Invalid input to arguments, exiting program") 
            exit() 
        return arg_value

    def read_args(self, argv, array_size, dim_size):
        if len(argv) > 2:
            #determine array size or default to 100k
            if '-a' in argv:
                temp = self.parse_args(argv, '-a')
                if temp != 0:
                    array_size = temp
            #determine number of dimensions
            if '-d' in argv:
                temp = self.parse_args(argv, '-d')
                if temp > 0:
                    dim_size = temp
        else:
            print("Usage: -d=dimensions (2 or 3), -a=array size")
        return array_size, dim_size 
