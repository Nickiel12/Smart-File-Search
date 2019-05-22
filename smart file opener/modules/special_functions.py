
class LinearStringGenerator():

    def __init__(self, type_of_generator:int, generator_list:list):
        self.input_list = generator_list


    def linear_combinations(self, input_list):
        start = 0
        stop = 1
        total = len(input_list) + 1
        
        while True:
            yield self.input_list[start:stop]
            
            stop += 1
            if stop == total:
                start += 1
                stop = start + 1
            
            if start + 1 == stop == total:
                break