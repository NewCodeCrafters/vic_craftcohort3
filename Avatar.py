def get_attribute(query, default):
    answer = input(query)
    if answer == "":
        answer = default 
    print('You chose', answer)
    return answer


hair_colour = get_attribute("What is the colour of your hair?:", 'Black')
hair_length = get_attribute(f"What is your hair length? [Long or Short]:", 'short')
eye_colour = get_attribute("What is your eye colour?:", 'brown')
gender = get_attribute("Are you a Male or Female?:", 'Male')