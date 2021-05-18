import math

def run():
    
    my_dict = {i: round(math.sqrt(i),2) for i in range (1, 1001)}

    print(my_dict)


if __name__ == '__main__':
    run()


     # natural_dicts = {}
    # for i in range (1, 101):
    #     if i% 3 != 0
    #         natural_dicts[i] = i ** 3
    
    # print(natural_dicts)


    # my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0 }

    # print(my_dict)