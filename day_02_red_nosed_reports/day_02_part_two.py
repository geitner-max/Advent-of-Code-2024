
__author__ = "Maximilian Geitner"
__date__ = "02.12.2024"

def check_level(levels_report):
    # idea: Remove one level and check safety condition
    # stop check when one constellation is safe
    for i in range(len(levels_report)):
        modified_levels: list = []
        for index, x in enumerate(levels_report):
            if index != i:
                modified_levels.append(x)

        report_diff = 0
        prev_report = None
        is_safe = True
        for level in modified_levels:
            if prev_report is None:
                prev_report = level
            else:
                diff = level - prev_report
                if report_diff < 0 and diff > 0:
                    is_safe = False
                elif report_diff > 0 and diff < 0:
                    is_safe = False
                elif abs(diff) > 3 or diff == 0:
                    is_safe = False
                else:
                    report_diff = diff
                    prev_report = level
        if is_safe:
            return True
    return False

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    reports: list = []
    # 1.) Read Input

    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            parts = list(map(lambda x: int(x), line.split(' ')))
            reports.append(parts)

    sum_safe_reports = 0

    # 2.) apply modified safety check function
    for levels in reports:
        is_safe = check_level(levels)
        if is_safe:
            sum_safe_reports += 1

    print("Solution Day 2 Part Two", sum_safe_reports)