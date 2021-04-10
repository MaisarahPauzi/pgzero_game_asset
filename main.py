import pgzrun
import random

WIDTH = 600
HEIGHT = 600

rocket = Actor('rocket')
rocket.midbottom = WIDTH/2 , HEIGHT - 5

alien = Actor('alien')
alien.midbottom = (random.randint(40, WIDTH-40) , 80)

laser = Actor('laser')
shoot = False
laser_speed = 5

def draw():
    screen.clear()
    rocket.draw()
    alien.draw()
    
    if shoot:
        move_laser()
        laser.draw()
    detect_hit()

def update():
    global rocket, shoot, laser
    
    if keyboard.left:
        rocket.x -= 5
    
    if keyboard.right:
        rocket.x += 5
    
    if not shoot:
        if keyboard.space:
            laser.pos = (rocket.x, HEIGHT - 98)
            shoot = True

def move_laser():
    global shoot, laser_speed
    
    if shoot:
        laser.pos = (laser.x, laser.y - 2* laser_speed)
        if laser.y < 10:
            shoot = False

def detect_hit():
    global laser, shoot, alien
    
    if shoot and alien.collidepoint(laser.pos):
        alien.midbottom = (random.randint(40, WIDTH-40) , 80)
    

pgzrun.go()