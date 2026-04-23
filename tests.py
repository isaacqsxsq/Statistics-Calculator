from stats import mean, median, mode, variance, std, min_max, correlation

data        = [4, 8, 15, 16, 23, 42]
data_mode   = [4, 8, 8, 15, 16, 16, 16, 23, 42]
x           = [4, 8, 15, 16, 23, 42]
y           = [1, 3, 6, 7, 9, 17]

def is_close(a, b, tol=0.001):
    return abs(a - b) < tol

print("=== Running Tests ===")
print(f"mean: {'PASS' if mean(data) == 18.0 else 'FAIL'}")
# print(f"median:      {'✅ PASS' if median(data) == 15.5 else '❌ FAIL'}")
# print(f"mode:        {'✅ PASS' if mode(data_mode) == [16] else '❌ FAIL'}")
# print(f"variance:    {'✅ PASS' if is_close(variance(data), 151.667) else '❌ FAIL'}")
# print(f"std_dev:     {'✅ PASS' if is_close(std(data), 12.315) else '❌ FAIL'}")
# print(f"std_dev:     {'✅ PASS' if min_max(data) == [4, 8, 15, 16, 23, 42] else '❌ FAIL'}")
# print(f"correlation: {'✅ PASS' if is_close(correlation(x, y), 0.9982) else '❌ FAIL'}")