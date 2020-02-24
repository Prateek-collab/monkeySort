import random,time

def is_sorted(L):
                for i in range(len(L)-1):
                                if L[i]<L[i+1]:
                                                return False
                return True

def monkey_sort(L):
                random.shuffle(L)

                if is_sorted(L):
                                print(L)
                else:
                                print(L)
                                time.sleep(0.2)
                                monkey_sort(L)

monkey_sort([23,45,12,13,36])
