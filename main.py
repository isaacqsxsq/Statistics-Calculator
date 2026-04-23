import stats, sys

def menu():
    while True:
        option = input("------------Menu------------\n1. Summary of data set\n2. correlation of two data sets\nq to quit\nEnter number: ")

        match option:
            case '1':
                print_summary()
            case '2':
                print_correlation()
            case 'q':
                sys.exit("Program Successfully Terminated")
            case _:
                print("Please type valid number\n")
        
def help_check_arr(num):
    while True: 
        st = input(f"Data {num}: ")
        try:
            st = st.replace(" ", "")
            arr = st.split(",")
            n = len(arr)
            for i in range(n):
                arr[i] = float(arr[i])
            return arr
        except ValueError:
            print("Input must be number splited by comma")

def print_summary():
    arr = help_check_arr(1)
    arr.sort()
    print("\n----------Summary-------------\n")
    print(f"Mean:                {stats.mean(arr):.3f}")
    print(f"Median:              {stats.median(arr)}")
    print(f"Mode:                {stats.mode(arr)}")
    print(f"Variance:            {stats.variance(arr):.3f}")
    print(f"Standard Deviation:  {stats.std(arr):.3f}")
    print(f"Min Max:             {stats.min_max(arr)}")
    print("\n")

def print_correlation():
    # TODO get correlation func fron stats and print correlation
    while True:
        arr1 = help_check_arr(1)
        arr2 = help_check_arr(2)
        
        if len(arr1) == len(arr2):
            break
        else:
            print("data 1 and data 2 must have same length. \n")
    
    print("\n")
    print(f"Correlation: {stats.correlation(arr1, arr2):.3f}")
    print("\n")

def main():
    menu()
    
if __name__ == '__main__':
    main()