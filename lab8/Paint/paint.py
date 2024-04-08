import pygame

# Queue for storing drawn shapes
queue = []

# Function to calculate rectangle coordinates
def getRectangle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x1-x2)
    h = abs(y1-y2)
    return (x, y, w, h)

# Function to calculate circle coordinates
def getCircle(x1, y1, x2, y2):
    x = x1
    y = y1
    r = int(((x2-x1)**2 + (y2-y1)**2)**0.5)
    return (x, y)

# Initialize pygame
pygame.init()
# Set screen dimensions
screen = pygame.display.set_mode((400, 300))
# Create another layer for drawing shapes
another_layer = pygame.Surface((400, 300))

# Initialize variables
done = False
clock = pygame.time.Clock()

# Initialize drawing tool
tool = 0
# 0 - rectangle
# 1 - circle
# 2 - eraser
# 3 - color selection
tools_count = 4

# Initialize coordinates and dimensions for drawing shapes
x1 = 10
y1 = 10
x2 = 10
y2 = 10

w = 100
h = 100
# Default color
color = (255,255,255)

# Flag to check if mouse button is pressed
isMouseDown = False
screen.fill((0,0,0))

# Dictionary for colors corresponding to key presses
colors = {
    pygame.K_1: (255, 0, 0),  # Red color for '1'
    pygame.K_2: (0, 255, 0),  # Green color for '2'
    pygame.K_3: (0, 0, 255),   # Blue color for '3'
    pygame.K_4: (255, 255, 0)   # Yellow color for '4'
}

# Main game loop
while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # Handle mouse button press
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click
                    if tool == 0:
                        x1 = event.pos[0]
                        y1 = event.pos[1]
                    elif tool == 1: # draw circle
                        x1 = event.pos[0]
                        y1 = event.pos[1]
                    elif tool == 2: # eraser
                        x1 = event.pos[0]
                        y1 = event.pos[1]
                        pygame.draw.circle(screen, (0,0,0), (x1, y1), 10)
                    elif tool == 3: # color selection
                        x1 = event.pos[0]
                        y1 = event.pos[1]
                        color = screen.get_at((x1, y1))
                            
                elif event.button == 3: # right click
                    tool = (tool + 1) % tools_count
                isMouseDown = True

            # Handle mouse button release
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    # Draw the shape on another layer
                    another_layer.blit(screen, (0, 0))
                isMouseDown = False
                
            # Handle mouse motion
            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    if tool == 0: # draw rectangle
                        screen.blit(another_layer, (0, 0))
                        x2 = event.pos[0]
                        y2 = event.pos[1]
                        pygame.draw.rect(screen, color, pygame.Rect(getRectangle(x1, y1, x2, y2)), 1)
                    
                    elif tool == 1: # draw circle
                        screen.blit(another_layer, (0, 0))
                        x2 = event.pos[0]
                        y2 = event.pos[1]
                        center = getCircle(x1, y1, x2, y2)
                        radius = int(((x2-x1)**2 + (y2-y1)**2)**0.5)
                        pygame.draw.circle(screen, color, center, radius, 1)

                    elif tool == 2: # eraser
                        x1 = event.pos[0]
                        y1 = event.pos[1]
                        pygame.draw.circle(screen, (0,0,0), (x1, y1), 30)
            # Handle key press for color selection
            if event.type == pygame.KEYDOWN:
                if event.key in colors:
                    color = colors[event.key]          
    # Update the display
    pygame.display.flip()
    # Control the frame rate
    clock.tick(60)
