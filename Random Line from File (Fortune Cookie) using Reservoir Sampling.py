import random

def get_random_fortune(filename, delimiter='#'):
    """Get random fortune using reservoir sampling"""
    
    chosen = None
    count = 0
    current_fortune = []

    with open(filename, 'r') as f:
        for line in f:
            if line.strip() == delimiter:
                if current_fortune:
                    count += 1

                    # Reservoir sampling
                    if random.randint(1, count) == 1:
                        chosen = ' '.join(current_fortune)

                    current_fortune = []
            else:
                current_fortune.append(line.strip())

    # Handle last fortune if no trailing delimiter
    if current_fortune:
        count += 1
        if random.randint(1, count) == 1:
            chosen = ' '.join(current_fortune)

    return chosen