import pgzrun
import random as rand
class Clouds:

    def __init__(self):
        self.clouds = []
        self.cloud_speed = 1.5
        self.cloud_min_y = 200
        self.cloud_max_y = 400
        self.cloud_cooldown = 2.0
        self.cloud_last_spawned_time = 0.0

    def spawn_clouds(self):
        clouds.append(Actor('cloud', (1100, rand.randint(self.cloud_min_y, self.cloud_max_y))))
    def update_clouds(time):
        global cloud_last_spawned_time
            if time - cloud_last_spawned_time > cloud_cooldown:
                clouds.append(Actor('cloud', (WIDTH, rand.randint(cloud_min_y, cloud_max_y))))
                cloud_last_spawned_time = time
            for cloud in clouds:
                cloud.x -= cloud_speed