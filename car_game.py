
import pygame
from pygame.locals import *
import random

pygame.init()

# Create the window
width = 500
height = 500
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Car Game')

# Colors
gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)
blue = (0, 128, 255)
light_blue = (0, 200, 255)

# Road and marker sizes
road_width = 300
marker_width = 10
marker_height = 50

# Lane coordinates
left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]

# Road and edge markers
road = (100, 0, road_width, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (395, 0, marker_width, height)

# For animating movement of the lane markers
lane_marker_move_y = 0

# Player's starting coordinates
player_x = 250
player_y = 400

# Frame settings
clock = pygame.time.Clock()
fps = 120

# Game settings
gameover = False
speed = 2
score = 0
ai_mode = False  # Default manual control

# Button properties for AI toggle
button_rect = pygame.Rect(10, 10, 100, 40)

class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Scale the image down so it's not wider than the lane
        image_scale = 45 / image.get_rect().width
        new_width = int(image.get_rect().width * image_scale)
        new_height = int(image.get_rect().height * image_scale)
        self.image = pygame.transform.scale(image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

class PlayerVehicle(Vehicle):
    def __init__(self, x, y):
        image = pygame.image.load('images/car.png').convert_alpha()
        super().__init__(image, x, y)

# Improved AI control logic
def ai_control(player, vehicles):
    current_lane = player.rect.center[0]
    lanes_status = {lane: True for lane in lanes}  # Assume all lanes are safe initially

    # Mark lanes with obstacles as unsafe
    for vehicle in vehicles:
        if player.rect.top - 150 < vehicle.rect.bottom < player.rect.bottom + 150:
            lanes_status[vehicle.rect.centerx] = False

    # Stay in the current lane if it's safe
    if lanes_status[current_lane]:
        return 0  # No movement needed
  
    # Determine the nearest safe lane
    safe_lanes = [lane for lane in lanes if lanes_status[lane]]
    if safe_lanes:
        closest_lane = min(safe_lanes, key=lambda x: abs(x - current_lane))
        return closest_lane - current_lane

    return 0  # No safe lanes found, stay in place

# Sprite groups
player_group = pygame.sprite.Group()
vehicle_group = pygame.sprite.Group()

# Create the player's car
player = PlayerVehicle(player_x, player_y)
player_group.add(player)

# Load vehicle images
image_filenames = ['pickup_truck.png', 'semi_trailer.png', 'taxi.png', 'van.png']
vehicle_images = [pygame.image.load(f'images/{img}').convert_alpha() for img in image_filenames]

# Load crash image
crash = pygame.image.load('images/crash.png').convert_alpha()
crash_rect = crash.get_rect()

# Game loop
running = True
while running:
    clock.tick(fps)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                ai_mode = not ai_mode

        if not ai_mode and event.type == KEYDOWN:
            if event.key == K_LEFT and player.rect.center[0] > left_lane:
                player.rect.x -= 100
            elif event.key == K_RIGHT and player.rect.center[0] < right_lane:
                player.rect.x += 100

    if ai_mode:
        move = ai_control(player, vehicle_group)
        if move < 0 and player.rect.center[0] > left_lane:
            player.rect.x -= 100  # Move left to the nearest safe lane
        elif move > 0 and player.rect.center[0] < right_lane:
            player.rect.x += 100  # Move right to the nearest safe lane


    # Drawing logic
    screen.fill(green)
    pygame.draw.rect(screen, gray, road)
    pygame.draw.rect(screen, yellow, left_edge_marker)
    pygame.draw.rect(screen, yellow, right_edge_marker)

    # Animate lane markers
    lane_marker_move_y += speed * 2
    if lane_marker_move_y >= marker_height * 2:
        lane_marker_move_y = 0
    for y in range(marker_height * -2, height, marker_height * 2):
        pygame.draw.rect(screen, white, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))

    # Draw the AI toggle button
    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.rect(screen, light_blue if button_rect.collidepoint(mouse_pos) else blue, button_rect)
    font = pygame.font.Font(None, 24)
    button_text = font.render('AI Mode', True, white)
    screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))

    ai_status_text = font.render('AI: ON' if ai_mode else 'AI: OFF', True, white)
    screen.blit(ai_status_text, (10, 60))

    # Draw sprites
    player_group.draw(screen)

    # Add vehicles
    if len(vehicle_group) < 2:
        add_vehicle = all(vehicle.rect.top > vehicle.rect.height * 1.5 for vehicle in vehicle_group)
        if add_vehicle:
            lane = random.choice(lanes)
            vehicle = Vehicle(random.choice(vehicle_images), lane, height / -2)
            vehicle_group.add(vehicle)

    # Move vehicles
    for vehicle in vehicle_group:
        vehicle.rect.y += speed
        if vehicle.rect.top >= height:
            vehicle.kill()
            score += 1
            if score % 5 == 0:
                speed += 1

    vehicle_group.draw(screen)

    # Display score
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render(f'Score: {score}', True, white)
    screen.blit(text, (50, 400))

    # Collision detection
    if pygame.sprite.spritecollide(player, vehicle_group, True):
        gameover = True
        crash_rect.center = [player.rect.center[0], player.rect.top]

    if gameover:
        screen.blit(crash, crash_rect)
        pygame.draw.rect(screen, red, (0, 50, width, 100))
        text = font.render('Game over. Play again? (Y/N)', True, white)
        screen.blit(text, (width // 2 - 80, 100))
        pygame.display.update()

        while gameover:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    gameover = False
                if event.type == KEYDOWN:
                    if event.key == K_y:
                        gameover = False
                        speed = 2
                        score = 0
                        vehicle_group.empty()
                        player.rect.center = [player_x, player_y]
                    elif event.key == K_n:
                        gameover = False
                        running = False

    pygame.display.update()

pygame.quit()
