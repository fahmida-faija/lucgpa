def cgpa(gpa_list, credit_list):
    total_point = 0
    for gpa, credit in zip(gpa_list, credit_list):
        point = gpa * credit
        total_point += point

    total_credit = sum(credit_list)   

    return round((total_point / total_credit), 2)

