def solution(numbers):
    #create a set so it doesnt have copies of numbers and then back (python is great)
    cleared_list = list(set(numbers))
    return len(cleared_list)