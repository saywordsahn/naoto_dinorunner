import pgzrun
from enum import Enum
import random as rand
WIDTH = 1100
HEIGHT = 600
GRAVITY = 100.0
JUMP_POWER = -30.0
DINO_STARTING_Y = 425
DINO_DUCKING_Y = 450
SPEED_INCREASE_AMOUNT = .3
class State(Enum):
    RUNNING = 1
    DUCKING = 2
    JUMPING = 3
    DEAD = 4



class GameState(Enum):
    PLAYING = 1
    GAME_OVER = 2
    START_SCREEN = 3




RUNNING = ['dinorun1', "dinorun2"]
DUCKING = ['dinoduck1', "dinoduck2"]
FLAPPING = ['bird1', 'bird2']








dino = Actor('dinorun1', (90, DINO_STARTING_Y))
dino.highscore = 0
dino.animation_lengh = 0.1
dino.last_animation_changed = 0.0
dino.frame_count = 0
dino.state = State.RUNNING
dino.jump_verocity = 0.0

clouds = []
cloud_speed = 1.5
cloud_min_y = 200
cloud_max_y = 400
cloud_cooldown = 2.0
cloud_last_spawned_time = 0.0

cactus = Actor('smallcactus2', (WIDTH, 438))
bird = Actor('bird1', (WIDTH * 1.5, HEIGHT / 2))
reset_button = Actor('reset', (WIDTH / 2 - 75 / 2, HEIGHT / 2))
bird.animation_lengh = 0.4
bird.last_animation_changed = 0.0
bird.frame_count = 0
speed = 9


score = 0
last_score_update = 0

track_x = 0
track2_x = 2404
track_y = 450
WHITE = (255, 255, 255)
time = 0
last_speed_increase = 0
game_state = GameState.START_SCREEN


##################################################################
def draw():
    if game_state == GameState.GAME_OVER:
        screen.blit('gameover', (WIDTH / 2 - 386 / 2, HEIGHT / 2 - 100))
        reset_button.draw()
    elif game_state == GameState.START_SCREEN:
        screen.fill(WHITE)
        screen.draw.text('press any key to start', (WIDTH / 2 - 150, HEIGHT / 2 - 80), color='gray', fontsize=32)
        screen.blit('dinojump', (WIDTH / 2 - 120 / 2, HEIGHT / 2))

    else:
        screen.fill(WHITE)
        dino.draw()
        bird.draw()
        cactus.draw()
        screen.blit('track', (track_x, track_y))
        screen.blit('track', (track2_x, track_y))
        screen.draw.text('HI : ' + str(dino.highscore), (873, 60), color="gray", fontsize=32)
        screen.draw.text(str(score), (100, 30), color="gray", fontsize=32)
        for cloud in clouds:
            cloud.draw()


def reset_dino():
    dino.y = DINO_STARTING_Y
    dino.state = State.RUNNING
    dino.animation_lengh = 0.1
    dino.last_animation_changed = 0.0
    dino.frame_count = 0
    dino.state = State.RUNNING
    dino.jump_verocity = 0.0


def reset():
    global game_state, clouds, speed, score
    game_state = GameState.PLAYING
    cactus.left = WIDTH
    bird.x = WIDTH * 1.5
    reset_dino()
    speed = 9
    clouds = []
    score = 0


def update_track():
    # update track position
    global track_x, track2_x
    if game_state == GameState.PLAYING:
        track_x -= speed
        track2_x -= speed

        if track_x < -2404:
            track_x = 2404

        if track2_x < -2404:
            track2_x = 2404
def change_game_state(new_state):
    global game_state
    game_state = new_state
def change_state(new_state):
    dino.state = new_state
    if new_state == State.DUCKING:
        dino.image = "dinoduck1"
        dino.y = DINO_DUCKING_Y
    elif new_state == State.RUNNING:
        dino.image = 'dinorun1'
        dino.y = DINO_STARTING_Y
    elif new_state == State.JUMPING:
        dino.jump_verocity = JUMP_POWER
    else:
        dino.image = "dinodead"






def update_dino(time, dt):

    if dino.state == State.RUNNING:
        if time - dino.last_animation_changed > dino.animation_lengh:
            dino.frame_count += 1
            dino.image = RUNNING[dino.frame_count % len(RUNNING)]
            dino.last_animation_changed = time


        if keyboard.UP or keyboard.SPACE or keyboard.W:
            change_state(State.JUMPING)


        if keyboard.DOWN or keyboard.S:
            change_state(State.DUCKING)





    elif dino.state == State.JUMPING:
        dino.jump_verocity += GRAVITY * dt
        dino.y += dino.jump_verocity
        if dino.y >= DINO_STARTING_Y:
            change_state(State.RUNNING)

    else:

        if time - dino.last_animation_changed > dino.animation_lengh:
            dino.frame_count += 1
            dino.image = DUCKING[dino.frame_count % len(DUCKING)]
            dino.last_animation_changed = time


        if not (keyboard.DOWN or keyboard.S):
            change_state(State.RUNNING)





def update_clouds(time):
    global cloud_last_spawned_time
    if game_state == GameState.PLAYING:
        if time - cloud_last_spawned_time > cloud_cooldown:
            clouds.append(Actor('cloud', (WIDTH, rand.randint(cloud_min_y, cloud_max_y))))
            cloud_last_spawned_time = time
        for cloud in clouds:
            cloud.x -= cloud_speed

def handle_collision():
    global game_state
    if dino.colliderect(cactus) or dino.colliderect(bird):
        change_state(State.DEAD)
        game_state = GameState.GAME_OVER
        if score > dino.highscore:
            dino.highscore = score



def update_cactus():
    if game_state == GameState.PLAYING:
        cactus.x -= speed
        if cactus.x < 0:
            cactus.x = WIDTH


def update_bird():
    if game_state == GameState.PLAYING:
        bird.x -= speed
        if bird.x < 0:
            bird.x = WIDTH
        if bird.y < 0:
            bird.y = rand.randint(HEIGHT / 2, HEIGHT / 2 + 150)

        if time - bird.last_animation_changed > bird.animation_lengh:
            bird.frame_count += 1
            bird.image = FLAPPING[bird.frame_count % len(RUNNING)]
            bird.last_animation_changed = time

def on_mouse_down(pos):
    if reset_button.collidepoint(pos) and game_state == GameState.GAME_OVER:
        reset()
def on_key_down():
    change_game_state(GameState.PLAYING)
def update(dt):
    global time, speed, last_speed_increase, score, last_score_update
    if game_state != GameState.START_SCREEN:
        time += dt

        if time - last_speed_increase > 1:
            speed += SPEED_INCREASE_AMOUNT
            last_speed_increase = time

        if time - last_score_update > 0.1 and game_state == GameState.PLAYING:
            score += 1
            last_score_update = time


        update_track()
        update_dino(time, dt)
        update_clouds(time)
        update_cactus()
        handle_collision()
        update_bird()










pgzrun.go()