def numFriendRequests(ages):
    """Count valid friend requests based on age rules."""
    
    # Use counting sort for ages (max age = 120)
    age_count = [0] * 121
    for age in ages:
        age_count[age] += 1

    total_requests = 0

    # For each possible age combination
    for age_a in range(1, 121):
        count_a = age_count[age_a]
        if count_a == 0:
            continue

        for age_b in range(1, 121):
            count_b = age_count[age_b]
            if count_b == 0:
                continue

            # Friend request rules
            if age_b <= 0.5 * age_a + 7:
                continue
            if age_b > age_a:
                continue

            # Count valid requests
            if age_a == age_b:
                # Same age: each person can send request to others
                total_requests += count_a * (count_a - 1)
            else:
                # Different ages
                total_requests += count_a * count_b

    return total_requests