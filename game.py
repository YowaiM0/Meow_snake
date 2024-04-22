import pygame 
import random 
pygame.init()

HEIGHT = 600
FRAME_COLOR = (153,92,0)
RECT_COLOR=(225,225,225)
OTHER_RECT_COLOR = (253, 159, 24)
HEADER_COLOR= (204,133,0)
COLOR_SNAKE=(0,0,0)
FOOD_COLOR=(87,87,87)
SIZE_RECT = 20 
COUNT_RECTS=20
RETURN= 1
WIDTH= COUNT_RECTS *  SIZE_RECT +2 * SIZE_RECT + RETURN *SIZE_RECT
HEADER_RECT = 70 

pygame.mixer.init()

pygame.mixer.music.load('Cats.mp3')

app = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Meow Snake')


running = True 
pygame.mixer.music.play(-1)

def draw_rect(color, row, column):
    pygame.draw.rect(app, color, (SIZE_RECT + column*SIZE_RECT+RETURN*(column+1),
                                  HEADER_RECT+SIZE_RECT+ row*SIZE_RECT+RETURN*(row+1), SIZE_RECT, SIZE_RECT))
    
class Snake:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def inside(self):
        return 0 <= self.x < COUNT_RECTS and 0 <= self.y < COUNT_RECTS
    
    def __eq__(self, other):
        return isinstance(other, Snake) and self.x == other.x and self.y == other.y 

def random_food_block():
    x = random.randint(0, COUNT_RECTS -1)     
    y = random.randint(0, COUNT_RECTS -1) 

    food_block = Snake(x, y)

    while food_block in snake_rect:
        x = random.randint(0, COUNT_RECTS -1)     
        y = random.randint(0, COUNT_RECTS -1)

    return food_block 

snake_rect = [Snake(9, 9)]
food = random_food_block()
x_row=0
y_col=1
result=0

clock = pygame.time.Clock()
text = pygame.font.SysFont('courier', 36)

while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False


       elif event.type == pygame.KEYDOWN: 
           if event.key == pygame.K_UP and y_col != 0:
               x_row= -1
               y_col= 0
           if event.key == pygame.K_DOWN and y_col != 0:
               x_row= 1
               y_col= 0
           if event.key == pygame.K_RIGHT and x_row != 0:
               x_row= 0
               y_col= 1
           if event.key == pygame.K_LEFT and x_row != 0:
               x_row= 0
               y_col= -1
    
   app.fill(FRAME_COLOR)

   pygame.draw.rect(app, HEADER_COLOR, (0, 0, WIDTH, HEADER_RECT))

   for row in range(COUNT_RECTS):
       for column in range ( COUNT_RECTS):
           if ( row + column) % 2 == 0:
               color = RECT_COLOR
           else:
               color= OTHER_RECT_COLOR
           draw_rect(color, row, column)
    
       draw_rect(FOOD_COLOR, food.x, food.y)
   
   for rect in snake_rect:
        draw_rect(COLOR_SNAKE, rect.x, rect.y)

   head = snake_rect[-1]
   
   if not head.inside():
       running= False

   new_head = Snake(head.x + x_row, head.y + y_col)
   snake_rect.append(new_head) 
   snake_rect.pop(0)
   
   if food == head:
       result += 1
       snake_rect.append(food)
       food = random_food_block()
    
   text_result = text.render(f'Score: {result}', 0, RECT_COLOR)
   app.blit(text_result, (SIZE_RECT, SIZE_RECT))
   
   pygame.display.update()
   clock.tick(5)
   
pygame.mixer.music.stop()
pygame.mixer.music.unload()
pygame.quit()


