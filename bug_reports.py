bug_reports_list = [
    'Issue 1 - High',
    'Issue 2 - Low',
    'Issue 3 - Critical',
    'Issue 4 - Low',
    'Issue 5 - Medium'
]

def add_new_bug_report(issue: str):
    bug_reports_list.append(issue)

def remove_low_prio_bug_report():
    for issue in bug_reports_list:
        if 'Low' in issue:
            bug_reports_list.remove(issue)
            print(f'Remove issue: {issue}')

def get_prio(issue):
    if 'Critical' in issue:
        return 1
    elif 'High' in issue:
        return 2
    elif 'Medium' in issue:
        return 3
    else:
        return 4

def sort_bug_reports_list_by_prio():
    bug_reports_list.sort(key=get_prio)

print('Initial: ', bug_reports_list)
add_new_bug_report('Issue 6 - Low')
print('Added new issue: ',bug_reports_list)
sort_bug_reports_list_by_prio()
print('Sort by prio: ',bug_reports_list)
remove_low_prio_bug_report()
print('Removed low prio: ',bug_reports_list)
