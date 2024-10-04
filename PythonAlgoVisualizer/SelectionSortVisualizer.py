# Selection Sort by Elnathan Yoon
import pygame, sys, random

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# screen dimensions
WIDTH = 400
HEIGHT = 500
window_size = (WIDTH, HEIGHT)

# intializing pygame
pygame.init()

# initializing screen
window = pygame.display.set_mode(window_size)

# title 
pygame.display.set_caption('Selection Sort Visualization')

clock = pygame.time.Clock()
width_of_bars = 1
range_of_bars = int(WIDTH/width_of_bars)

#initializing lists with random integers
list_of_ints = list(range(1,400)) # list of integers from 1 to 400
random.shuffle(list_of_ints) # shuffling integers
#intializing lists for keeping track of state of integers
state = []
for i in range(range_of_bars):
    state.append(1)


counter = 0
bubble_counter = 0
bubble_sorted = False
sort_algo = 0 #0 is for Selection Sort and 1 is for Bubble Sort

def reset_sort():
    global list_of_ints, state, counter, bubble_counter, bubble_sorted
    list_of_ints = list(range(1, WIDTH))
    random.shuffle(list_of_ints)
    state = [1 for _ in range(range_of_bars)]
    counter = 0
    bubble_counter = 0
    bubble_sorted = False

# Game loop
while True:
    window.fill((10, 10, 10))

    if sort_algo == 0:
        # Selection Sort Implementation 
        if counter < len(list_of_ints):
            min_index = counter
            # Find the minimum element in the remaining unsorted lists 
            for j in range(counter+1, len(list_of_ints)):
                if list_of_ints[min_index] > list_of_ints[j]:
                    state[j] = 0
                    min_index = j
                else:
                    state[j] = 1
                    state[min_index] = 1
            # Swap the found minimum element with the first element 
            list_of_ints[counter], list_of_ints[min_index] = list_of_ints[min_index], list_of_ints[counter]
        counter+=1
    
        if counter - 1 < len(list_of_ints):
            state[counter - 1] = 2

    elif sort_mode == 1:
        # Bubble Sort Visualization
        if not bubble_sorted:
            swapped = False
            # Iterate through the array up to the sorted section
            for j in range(0, len(list_of_ints) - bubble_counter - 1):
                if list_of_ints[j] > list_of_ints[j + 1]:
                    # Swap elements if they are in the wrong order
                    list_of_ints[j], list_of_ints[j + 1] = list_of_ints[j + 1], list_of_ints[j]
                    swapped = True
                    state[j], state[j + 1] = 0, 0  # mark as swapped
                else:
                    state[j], state[j + 1] = 1, 1  # reset to unsorted state

            if not swapped:  # If no elements were swapped, array is sorted
                bubble_sorted = True

            bubble_counter += 1

        if bubble_counter < len(list_of_ints):
            state[len(list_of_ints) - bubble_counter - 1] = 2

    # Changing color of sorted ints in display
    for i in range(len(list_of_ints)):
        if state[i] == 0:
            color = RED
        elif state[i] == 2:
            color = GREEN  
        else:
            color = WHITE
        pygame.draw.rect(window, color, pygame.Rect(int(i*width_of_bars), HEIGHT - list_of_ints[i], width_of_bars, list_of_ints[i]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:  # Selection Sort
                sort_mode = 0
                reset_sort()
            elif event.key == pygame.K_b:  # Bubble Sort
                sort_mode = 1
                reset_sort()

    
    clock.tick(40) # runs program at 40 frames per second
    pygame.display.flip() # updates the entire display
