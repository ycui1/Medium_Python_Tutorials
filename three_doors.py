from random import shuffle, choice

door_numbers = [1, 2, 3]
wanted_award = "car"
unwanted_award = "goat"
awards = [wanted_award, unwanted_award, unwanted_award]


def monty_hall_trial(initial_door_number, should_switch):
    shuffle(awards)
    doors = dict(zip(door_numbers, awards))
    remaining_door_numbers = [x for x in door_numbers if x != initial_door_number]
    for door_number in remaining_door_numbers:
        if doors[door_number] == unwanted_award:
            remaining_door_numbers.remove(door_number)
            break

    switched_door_number = remaining_door_numbers[0]
    final_door_number = switched_door_number if should_switch else initial_door_number
    won_car = doors[final_door_number] == wanted_award
    return won_car


def simulate_monty_hall(trial_number, should_switch):
    winning_counts = 0
    for trial_i in range(trial_number):
        initial_pick = choice(door_numbers)
        won_car = monty_hall_trial(initial_pick, should_switch)
        winning_counts += int(won_car)
    winning_prob = winning_counts/trial_number
    print(f"Trial Times: {trial_number} times\n"
          f"Switching: {should_switch}\n"
          f"Probability: {winning_prob:.2%}")


simulate_monty_hall(10000, True)
simulate_monty_hall(10000, False)