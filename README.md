# Student Grade Evaluation Program

## Description

This Python program checks a student's mark and displays the correct grade based on the score entered.

The program uses:

* `if`
* `elif`
* `else`

statements to determine the grade category.

---

## Grade Categories

| Marks Range   | Grade       |
| ------------- | ----------- |
| 76 – 100      | Distinction |
| 61 – 75       | Pass        |
| 51 – 60       | Credit      |
| 36 – 50       | Almost      |
| 21 – 35       | Fail        |
| 1 – 20        | Ungraded    |
| Invalid Marks | Error       |

---

## Python Code

```python id="59fzr8"
student_mark = 57

# I am checking the range thats above 75 and awarding : Dist
if student_mark > 75 and student_mark <= 100:
    print("Distinction")

# checking the range thats above 60 awarding :Pass
elif student_mark > 60 and student_mark <= 75:
    print("Pass")

# checking the range thats above 50 awarding :Credit
elif student_mark > 50 and student_mark <= 60:
    print("Credit")

# checking the range thats above 35 awading :Almost
elif student_mark > 35 and student_mark <= 50:
    print("Almost")

# checking the range thats above 20 awading :Fail
elif student_mark > 20 and student_mark <= 35:
    print("Fail")

# checking the range thats above 0 awading :Ungraded
elif student_mark > 0 and student_mark <= 20:
    print("ungraded")

else:
    print("error")
```

---

## Features

* Uses conditional statements
* Evaluates student marks
* Displays grade automatically
* Handles invalid marks

---

## Requirements

* Python 3

Download Python from:

[Python Official Website](https://www.python.org?utm_source=chatgpt.com)

---

## How to Run the Program

1. Save the file as:

```bash id="2uw4hn"
student_grade.py
```

2. Open terminal or command prompt

3. Run the program:

```bash id="l1twdd"
python student_grade.py
```

---

## Example Output

```text id="ecy1y5"
Credit
```

---


