
__author__ = "Maximilian Geitner"
__date__ = "02.12.2024"

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

    # 2.) check conditions on all reports
    sum_safe_reports = 0
    for levels in reports:
        report_diff = 0     # monitor differences between two levels
        prev_report = None
        is_safe = True
        for level in levels:
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
            sum_safe_reports += 1

    print("Solution Day 2 Part 1: ", sum_safe_reports)