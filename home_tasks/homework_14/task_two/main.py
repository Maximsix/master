
from custom_iterator import CustomIterator

if __name__ == '__main__':
    some_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    some_lis2 = list(range(1, 101))
    custom_iterator2 = CustomIterator(sequence=some_lis2, start=0, stop=99, step=7)
    custom_iterator1 = CustomIterator(sequence=some_list1, start=3, stop=9)
    for item_of_list in [custom_iterator1, custom_iterator2]:
        print(sep='\n')
        for item in item_of_list:
            print(item, end=' ')