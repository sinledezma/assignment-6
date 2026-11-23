# Sinthia Ledezma - Assignment 6

def filter_critical_scores(score_list, min_severity=70):
    """
    Filter and cap scores according to the prompt
    """
    critical_scores = []
    for score in score_list:
        if score > min_severity: #Changed from >= to strictly greater than >
            if score > 100:
                score = 100
            critical_scores.append(score)
    return critical_scores
