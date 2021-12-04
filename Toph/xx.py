



# L, M = map(int, input().split())
# haap_dict = {}

# for i in range(L+M):
#     Shuru, Shesh = map(int, input().split())
#     if Shuru not in haap_dict:
#         haap_dict[Shuru] = Shesh
#     else:
#         haap_dict[Shuru] = Shesh

# print(haap_dict)
# Jaber_start = False
# Mukhtar_start = False

# Jaber_Bhai = 0
# Mukhtar_Bhai = 0

# while True:
#     Jaber = int(input())
#     #code 
#     if Jaber == 1:
#         if Jaber_start:
#             Jaber_Bhai +=  1
#         else:
#             Jaber_start = True
            
#     if not Jaber_start:
#         continue
#     else:
#         if Jaber in haap_dict:
#             Jaber_Bhai = haap_dict.get(Jaber)
#         else:
#             Jaber_Bhai += Jaber
#     if Jaber_Bhai >= 100:
#         print("Jaber Bhai")
#         break

#     Mukhtar = int(input())
#     if Mukhtar == 1:
#         if Mukhtar_start:
#             Mukhtar_Bhai +=  1
#         else:
#             Mukhtar_start = True
            
#     if not Mukhtar_start:
#         continue
#     else:
#         if Mukhtar in haap_dict:
#             Mukhtar_Bhai = haap_dict.get(Mukhtar)
#         else:
#             Mukhtar_Bhai += Mukhtar
#     if Mukhtar >= 100:
#         print("Mukhtar Bhai")
#         break







snake ={}
ladder = {}

L, M = (int(x) for x in input().split())
for i in range(L):

    # Shuru, Shesh = (int(x) for x in input().split())
    # if Shuru not in ladder:
    #     ladder[Shuru] = Shesh

    if i == M-1:
        Shuru, Shesh = (int(x) for x in input().split())
        if Shuru not in snake:
            snake[Shuru] = Shesh
    else:
        Shuru, Shesh = (int(x) for x in input().split())
        if Shuru not in ladder:
            ladder[Shuru] = Shesh


for i in range(M):
    Shuru, Shesh = (int(x) for x in input().split())
    if Shuru not in snake:
        snake[Shuru] = Shesh
# print(ladder,snake)
dic = {
    "zaber":0,
    "muktar":0
}
counter = 1
for _ in range(10000000):
    guti = int(input())
    if guti == 1 or dic["zaber"] > 0:
        dic["zaber"] += guti
        if dic["zaber"] > 100: dic["zaber"] -= guti
        if dic["zaber"] in ladder.keys() :
            dic["zaber"] = ladder[dic["zaber"]]
        if dic["zaber"] in snake.keys() :
            dic["zaber"] = snake[dic["zaber"]]
    if dic["zaber"] >= 100:
        print("Jaber Tuhin is the winner.")
        break
    guti = int(input())
    if guti == 1 or dic["muktar"] > 0:
        dic["muktar"] += guti
        if dic["muktar"] > 100: dic["muktar"] -= guti
        if dic["muktar"] in ladder.keys() :
            dic["muktar"] = ladder[dic["muktar"]]
        if dic["muktar"] in snake.keys() :
            dic["muktar"] = snake[dic["muktar"]]
    if dic["muktar"] >= 100:
        print("Mukhter Hossain is the winner.")
        break
