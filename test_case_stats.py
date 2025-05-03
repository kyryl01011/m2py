working_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

def test_case_stats():
    results = []
    for day in working_week:
        reply = int(input(f'How many test-cases you done at {day}\n'))
        results.append(reply)
    total_task_cases_done = sum(results)
    average_result = total_task_cases_done / len(results)
    print(f'Your results for this week: total task-cases done - {total_task_cases_done}, average per day: {average_result}')
    if average_result > 10:
        print('Well done!')
    else:
        print('Try to get better :)')

test_case_stats()