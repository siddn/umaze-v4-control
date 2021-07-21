
import microrobot

class uMAZE_Platform:
    def __init__(self, robots, corners) -> None:
        self.robots = robots
        self.corners = corners


    def move_robot(self, identifier, directon, step=1):
        for robot in self.robots:
            if robot.identifier == identifier:
                current_pos = robot.position
                quad = self.__get_quadrant(current_pos)
                coilx, coily = self.__get_coil(current_pos)
                zone = self.__get_zone(current_pos)
                if directon=='y':
                    next_zone = self.__get_zone((current_pos[0], current_pos[1]+1))
                    if next_zone == zone:
                        
                if directon=='x':
                    next_zone = self.__get_zone((current_pos[0]+1, current_pos[1]))

    
    def __get_quadrant(positon):
        pass
    
    def __get_zone(position):
        pass

    def __get_coil(position):
        pass
                
                  