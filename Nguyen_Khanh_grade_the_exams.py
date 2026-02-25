import pandas as pd

def main():
    # Task 1: Nhập tên file
    while True:
        filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
        try:
            file = open("Data Files/" + filename + ".txt", "r")
            print("Successfully opened " + filename + ".txt")
            break
        except FileNotFoundError:
            print("File cannot be found.")

    # Task 2: Kiểm tra định dạng file
    lines = file.read().splitlines()
    file.close()

    print("**** ANALYZING ****")

    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".split(",")

    valid_count = 0
    invalid_count = 0
    scores = []

    for line in lines:
        values = line.split(",")
        valid_check = True

        # Kiểm tra số lượng giá trị có đúng là 26 không (1 N# + 25 câu trả lời)
        if len(values) != 26:
            print("Invalid line of data: does not contain exactly 26 values:")
            print(line)
            valid_check = False

        # Kiểm tra định dạng N#
        if valid_check:
            student_id = values[0]
            if len(student_id) != 9 or student_id[0] != "N" or not student_id[1:].isdigit():
                print("Invalid line of data: N# is invalid")
                print(line)
                valid_check = False

        if valid_check:
            valid_count += 1
            # Tính điểm để dùng cho Task 3
            score = 0
            for i in range(25):
                student_answer = values[i + 1]
                # # Đúng +4, bỏ +0, sai -1
                if student_answer == answer_key[i]:
                    score += 4
                elif student_answer == "":
                    score += 0
                else:
                    score -= 1
            scores.append((values[0], score))
        else:
            invalid_count += 1

    if invalid_count == 0:
        print("No errors found!")

    print("**** REPORT ****")
    print(f"Total valid lines of data: {valid_count}")
    print(f"Total invalid lines of data: {invalid_count}")

    # Task 3: Thống kê điểm
    if scores:
        df = pd.DataFrame(scores, columns=["student_id", "score"])
        median = df["score"].median()
        if median == int(median):
            median = int(median)

        print(f"Mean (average) score: {df['score'].mean():.2f}")
        print(f"Highest score: {df['score'].max()}")
        print(f"Lowest score: {df['score'].min()}")
        print(f"Range of scores: {df['score'].max() - df['score'].min()}")
        print(f"Median score: {median}")

        # Task 4: Ghi kết quả ra file
        df.to_csv(filename + "_grades.txt", index=False, header=False)

if __name__ == "__main__":
    main()