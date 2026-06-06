
# search in the boxes without recursion
# def look_for_key(main_box):
#     pile = main_box.male_a_pile_to_look_through()
#     while pile is not empty:
#         box = pile.grab_a_box()
#         for item in box:
#             if item.is_a_box():
#                 pile.append(item)
#             elif item.is_a_key():
#                 print("Found the key")


# search in the boxes with reursion
# def look_for_key(box):
#     for iten in box:
#         if item.is_a_box():
#             look_for_key(item) # recursion
#         elif item.is_a_key():
#             print("Found the key")


def countdown(i):
    print(i)
    if i <= 1: # базовый случай
        return
    else:
        countdown(i-1) # рекусрсивный случай

countdown(3)