def generate_id(prefix, existing_ids):
    highest = 0

    for id in existing_ids:
        if id.startswith(prefix):
            number_part = id[len(prefix):]

            if number_part.isdigit():
                number = int(number_part)

                if number > highest:
                    highest = number

    return prefix + str(highest + 1).zfill(3)