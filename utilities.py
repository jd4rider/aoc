class Utilities:
    def __init__(self, x):
        #concatenate the first and last occuring numbers
        self.num = int(self.find_first_num_occurance(self.fix_string_numbers(x)) 
                       + self.find_first_num_occurance(self.fix_string_numbers(x)[::-1]))

    #replace the second character of string numbers with actual number
    def fix_string_numbers(self, x):
        num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        for idx, i in enumerate(num_list):
            if i in x:
                x = x.replace(i, i.replace(i[1], str(idx)))
        return x

    #return the first occuring digit from string
    def find_first_num_occurance(self, x):
        for c in x:
            if c.isdigit():
                return str(c)


    