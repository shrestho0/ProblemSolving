# import operator
# def person_lister(f):
#     def inner(people):

#         all_names = {}
#         to_show = []
#         for person in people:
#             if person[-1].upper() == 'M':
#                 person.insert(0, 'Mr.')
#             elif person[-1].upper() == 'F':
#                 person.insert(0, 'Ms.')

#             all_names[person[-2]] = ' '.join(person[:-2])
            
            
#         for x in sorted(all_names):
#             to_show.append(all_names[x])

#         return to_show


#     return inner

# @person_lister
# def name_format(person):
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

# if __name__ == '__main__':
#     people = [input().split() for i in range(int(input()))]
#     print(*name_format(people), sep='\n')



def get_age(x):
    return int(x[2])

def person_lister(f):

    def get_age(x):
        return int(x[2])
        
    def inner(people):
        return map(f,sorted(people, key=get_age))
    return inner