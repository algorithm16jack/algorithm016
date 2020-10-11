class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dict_i = collections.defaultdict(list)
        dict_j = collections.defaultdict(list)
        for obstacle in obstacles:
            dict_i[obstacle[1]].append(obstacle[0])
            dict_j[obstacle[0]].append(obstacle[1])
        
        flag = 'j'
        max_dist = 0
        current_i = 0
        current_j = 0
        for step in range(len(commands)):
            if commands[step] == -1:
                if flag == 'j':
                    flag = 'i'
                elif flag == 'i':
                    flag = '-j'
                elif flag == '-j':
                    flag = '-i'
                elif flag == '-i':
                    flag = 'j'
            elif commands[step] == -2:
                if flag == 'j':
                    flag = '-i'
                elif flag == '-i':
                    flag = '-j'
                elif flag == '-j':
                    flag = 'i'
                elif flag == 'i':
                    flag = 'j'
            elif commands[step] >= 1 and commands[step] <= 9:
                if flag == 'j':
                    move_range = range(current_i + 1, current_i + commands[step] + 1)
                    for move_target in move_range:
                        if move_target in dict_j[current_j]:
                            move_target -= 1
                            break
                    current_i = move_target
                elif flag == 'i':
                    move_range = range(current_j + 1, current_j + commands[step] + 1)
                    for move_target in move_range:
                        if move_target in dict_i[current_i]:
                            move_target -= 1
                            break
                    current_j = move_target
                elif flag == '-j':
                    move_range = range(current_i - 1, current_i - commands[step] - 1, -1)
                    for move_target in move_range:
                        if move_target in dict_j[current_j]:
                            move_target += 1
                            break
                    current_i = move_target
                elif flag == '-i':
                    move_range = range(current_j - 1, current_j - commands[step] - 1, -1)
                    for move_target in move_range:
                        if move_target in dict_i[current_i]:
                            move_target += 1
                            break
                    current_j = move_target

                current_square = current_i * current_i + current_j * current_j
                if current_square > max_dist:
                    max_dist = current_square
        
        return max_dist