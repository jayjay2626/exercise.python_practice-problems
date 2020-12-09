# Created by Leon Hunter at 12:10 PM 12/08/2020
class Lister(object):
    def get_integer_list(self, start, stop, step):
        ''' TODO - Implement solution
        Given 3 integers,
            `start`, `stop`, and `step`
        return a list of all integers
            between `start`,
            incrementing by `step`,
            up to and including `stop`
        '''
        if step == 0:
            step = 1
        result = list(range(start, stop+1, step))

        return result

    def get_even_list(self, start, stop, step):
        ''' TODO - Implement solution
        Given 3 integers,
            `start`, `stop`, and `step`
        return a list of all integers
            between `start`,
            incrementing by `step`,
            up to and including `stop`
            and are divisible by 2
        '''
        if step == 0:
            step = 1

        temp_list = list(range(start, stop+1, step))
        even_list = list()
        for integer in temp_list:
            if integer % 2 == 0:
                even_list.append(integer)

        return even_list

    def get_odd_list(self, start, stop, step):
        ''' TODO - Implement solution
        Given 3 integers,
            `start`, `stop`, and `step`
        return a list of all integers
            between `start`,
            incrementing by `step`,
            up to and including `stop`
            and are not divisible by 2
        '''
        if step == 0:
            step = 1

        temp_list = list(range(start, stop+1, step))

        odd_list = list()
        even_list = list()

        for value in temp_list:
            if value % 2 == 0:
                even_list.append(value)
            else:
                odd_list.append(value)

        return odd_list
