def hamming_distance(slack_username, x_handle):
    distance = []
    max_length = max(len(slack_username), len(x_handle))
    slack_username = slack_username.ljust(max_length)
    x_handle = x_handle.ljust(max_length)


    for i in range(max_length):
        if slack_username [i] == x_handle[i]:
            distance.append(0)
        elif slack_username[i] != x_handle[i]:
            distance.append(1)
    return sum(distance)
slack_username = "chioma"
x_handle = "_azarya_m"
print(hamming_distance(slack_username, x_handle))
    
