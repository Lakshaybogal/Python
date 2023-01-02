{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "U9qm6CTsdy3S",
        "outputId": "3a688588-36e0-4f2f-85c9-13e266c81251"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Functions\n"
          ]
        }
      ],
      "source": [
        "print(\"Functions\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "67Co5ftDeBvL"
      },
      "source": [
        "1.A)Write a function called showNumbers( ) that takes a parameter called limit. It should print\n",
        "all neon numbers between 0 and limit and identify the even and odd numbers out of the neon\n",
        "numbers.\n",
        "(Note:A neon number is a number where the sum of digits of square of the number is\n",
        "equal to the number. The task is to check and print neon numbers in a range.)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KtMiX7vSd9c0",
        "outputId": "4ad5ebed-1e6c-4a7a-b0dd-0e880d3225e8"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter the limit: 10000\n",
            "0 is Even\n",
            "1 is Odd\n",
            "9 is Odd\n"
          ]
        }
      ],
      "source": [
        "def checkneon(i):\n",
        "  # for i in range(limit):\n",
        "    s = i*i\n",
        "    sum = 0\n",
        "    while(s!=0):\n",
        "      sum = sum + s%10\n",
        "      s = s//10\n",
        "\n",
        "    if(sum == i):\n",
        "      shownumbers(i)\n",
        "\n",
        "\n",
        "def shownumbers(num):\n",
        "  if(num%2==0):\n",
        "    print(f\"{num} is Even\")\n",
        "  else:\n",
        "    print(f\"{num} is Odd\")\n",
        "\n",
        "\n",
        "n = int(input(\"Enter the limit: \"))\n",
        "for i in range(n+1):\n",
        "  checkneon(i)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EOG9TsGKmfTY"
      },
      "source": [
        "1.B) Write a menu driven code that will perform below tasks(use function for each task). Call\n",
        "appropriate function.\n",
        "-Input list of student name and total marks of students and find highest marks\n",
        "-Input student name: hobby for n students. Create dictionary and pass it to function ,\n",
        "function will return popular hobby."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "T89IceDxh-b5",
        "outputId": "95fd9763-b190-4e18-84a5-5a4651c16e1f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter 1 For Marks of Students\n",
            "Enter 2 For Hobbies of Students\n",
            "1\n",
            "Number of Students: 3\n",
            "Enter the Name and Marks of students: \n",
            "Name of student 1: lakshay\n",
            "Enter his/her marks: 100\n",
            "Name of student 2: anuj\n",
            "Enter his/her marks: 99\n",
            "Name of student 3: mahesh\n",
            "Enter his/her marks: 98\n",
            "{'lakshay': 100, 'anuj': 99, 'mahesh': 98}\n",
            "Higest marks 100\n"
          ]
        }
      ],
      "source": [
        "def marks():\n",
        "  n = int(input(\"Number of Students: \"))\n",
        "  print(\"Enter the Name and Marks of students: \")\n",
        "  students_marks = {}\n",
        "  higest = 0\n",
        "  for i in range(n):\n",
        "    name = input(f\"Name of student {i+1}: \")\n",
        "    marks = int(input(\"Enter his/her marks: \"))\n",
        "    students_marks[name] = marks\n",
        "  highest = max(students_marks.values())\n",
        "\n",
        "  print(students_marks)\n",
        "  print(f\"Higest marks {highest}\")\n",
        "  \n",
        "def hobby():\n",
        "  n = int(input(\"Number of Students: \"))\n",
        "  print(\"Enter the Name and Hobby of students: \")\n",
        "  students_hobby ={}\n",
        "  for i in range(n):\n",
        "    name = input(f\"Name of student {i+1} \")\n",
        "    hobby = int(input(\"Enter his/her Hobby\"))\n",
        "    students_hobby[name] = hobby\n",
        "  print(students_hobby)\n",
        "\n",
        "print(\"Enter 1 For Marks of Students\")\n",
        "print(\"Enter 2 For Hobbies of Students\")\n",
        "ch = int(input())\n",
        "if ch == 1:\n",
        "  marks()\n",
        "elif ch == 2:\n",
        "  hobby()\n",
        "else:\n",
        "  print(\"Error\")\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "59PnTxOLqghY"
      },
      "source": [
        "2. Scenario-: Use functions to calculate the trip&#39;s costs:\n",
        "- Define a function called hotel_cost with one argument nights as input.\n",
        "The hotel costs Rs.140 per night. So, the function hotel_cost should returns 140 * nights.\n",
        "- Define a function called plane_ride_cost that takes a string, city, as input.\n",
        "The function should return a different price depending on the location.\n",
        "Below are the valid destinations and their corresponding round-trip prices.\n",
        "o &quot;Charlotte&quot;: 183, &quot;Tampa&quot;: 220, &quot;Pittsburgh&quot;: 222, &quot;Los Angeles&quot;: 475\n",
        "- Below your existing code, define a function called rental_car_cost with an argument\n",
        "called days. Calculate the cost of renting the car: Every day you rent the car costs\n",
        "Rs.40.(cost=40*days)\n",
        "If you rent the car for 7 or more days, you get Rs.50 off your total(cost-=50).\n",
        "Alternatively (elif), if you rent the car for 3 or more days, you get Rs.20 off your total.\n",
        "You cannot get both of the above discounts. Return that cost."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "04lI2_jrqiio",
        "outputId": "cfdbfef2-65aa-4922-819b-0f29329f2dc7"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter Numbers of nights: 10\n",
            "Place's you can go\n",
            "Charlotte Tampa Pittsburgh Los Angeles\n",
            "Enter the Place to go: Los Angeles\n",
            "Enter number of days rent the car: 7\n",
            "Your Total Cost of Trip is 61730\n"
          ]
        }
      ],
      "source": [
        "def hotel_cost(nights):\n",
        "    cost = nights*1400\n",
        "    return cost\n",
        "\n",
        "def plane_ride_cost(place):\n",
        "    place1 = {\"Charlotte\": 18300, \"Tampa\": 22000, \"Pittsburgh\": 22200, \"Los Angeles\": 47500}\n",
        "    return place1[place]\n",
        "def rental_car_cost(days):\n",
        "    cost = days*40\n",
        "    if(days >= 7):\n",
        "      cost = cost - 50\n",
        "    elif(days >= 3):\n",
        "      cost = cost - 20\n",
        "    else:\n",
        "      cost\n",
        "    return cost\n",
        "def total(x,y,z):\n",
        "    return x+y+z\n",
        "\n",
        "nights = int(input(\"Enter Numbers of nights: \"))\n",
        "print(\"Place's you can go\\n\" \"Charlotte \"  \"Tampa \" \"Pittsburgh \" \"Los Angeles\")\n",
        "place = input(\"Enter the Place to go: \")\n",
        "days = int(input(\"Enter number of days rent the car: \"))\n",
        "x = hotel_cost(nights)\n",
        "y = plane_ride_cost(place)\n",
        "z = rental_car_cost(days)\n",
        "t = total(x,y,z)\n",
        "print(f\"Your Total Cost of Trip is {t}\")"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. Given a set of points in two dimensional plane as(x1,y1),(x2,y2),(x3,y3)……..(x|D|,y|D|).\n",
        "Use suitable python data structure to store values of Age(X) and glucose level(Y) of a\n",
        "person as given below .Write function lreg () to find the equation of best fit linear\n",
        "regression line for above data points. Return regression coefficient w0 and w1 from\n",
        "function. Predict the glucose level of a person with age as 39 yr.![image.png](data:image/png;base64,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)"
      ],
      "metadata": {
        "id": "9SJhTC6BLiGi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data = {40:99,21:65,25:79,42:75,57:87,59:81}\n",
        "age = []\n",
        "glucose_level = []\n",
        "product = []\n",
        "for i in data:\n",
        "  gl = data[i]\n",
        "  age.append(i)\n",
        "  glucose_level.append(gl)\n",
        "  product.append(gl*i)\n",
        "  square = list(map(lambda x:x*x,age))\n",
        "\n",
        "print(age)\n",
        "print(glucose_level)\n",
        "X = sum(age)\n",
        "Y = sum(glucose_level)\n",
        "XY = sum(product)\n",
        "XX = sum(square)\n",
        "N = len(data)\n",
        "b = ((N*XY)-X*Y)/(N*XX - X*X)\n",
        "a = ((Y-b*X)/N)\n",
        "AGE = int(input(\"Enter age: \"))\n",
        "glu = round(a+b*AGE,2)\n",
        "print(f\"Glucose level is: {glu}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ofZaEb5qLhq0",
        "outputId": "0b5145bc-80cc-4cfd-d0c4-e5dbcf858d1f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[40, 21, 25, 42, 57, 59]\n",
            "[99, 65, 79, 75, 87, 81]\n",
            "Enter age: 34\n",
            "Glucose level is: 78.72\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4. Consider a “Random Game”. Here, out of the list of Choosing_number =[1,2,3,4,5,6,7,8,9].\n",
        "To play the game, user will do the following task:\n",
        "a) Select a random integer from the above list between 2 to 9.\n",
        "b) Filter the number less than the above selected numbers excluding originally selected\n",
        "number\n",
        "c) Prepare a new list using map() where number less than the above selected numbers\n",
        "will be multiplied by 10.\n",
        "d) Then using reduce(), find sum of all these multiplied values of new list.\n",
        "e) On selected sum the user will get some valuable hamper: (use dictionary)\n",
        "If the sum is less than equal to 50, user will get hamper1.\n",
        "If the sum is less than equal to 100, user will get hampe2.\n",
        "If the sum is less than equal to 150, user will get hamper3.\n",
        "If the sum is less than equal to 360, user will get hamper4.\n"
      ],
      "metadata": {
        "id": "Xr1LjDfmLi90"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "from functools import reduce\n",
        "\n",
        "Choosing_number = [1,2,3,4,5,6,7,8,9]\n",
        "random_number = random.choice(Choosing_number)\n",
        "print(random_number)\n",
        "filter_list = list(filter(lambda num : num < random_number , Choosing_number))\n",
        "print(filter_list)\n",
        "map_list = list(map(lambda x : x * 10 , filter_list))\n",
        "print(map_list)\n",
        "reduce_list = reduce(lambda num1, num2: num1 + num2, map_list)\n",
        "print(reduce_list)\n",
        "hamper = {\n",
        "    50 : \"Hamper 1\",\n",
        "    100 : \"Hamper 2\",\n",
        "    150 : \"Hamper 3\",\n",
        "    360 : \"Hamper 4\"\n",
        "}\n",
        "if reduce_list <=50:\n",
        "  indx = 50\n",
        "elif reduce_list <=100:\n",
        "  indx = 100\n",
        "elif reduce_list <=150:\n",
        "  indx = 150\n",
        "elif reduce_list <=360:\n",
        "  indx = 360\n",
        "\n",
        "print(hamper[indx])\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "i514iLY-Lihu",
        "outputId": "1a5e18b9-f0cf-47f5-dfe2-4a2ac295a12a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "6\n",
            "[1, 2, 3, 4, 5]\n",
            "[10, 20, 30, 40, 50]\n",
            "150\n",
            "Hamper 3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "5. Using Recursion\n",
        "Consider you are given an array of integers ordered randomly. You are asked to check if the\n",
        "array is in ascending order, i.e., increasingly with the smallest number placed first and the\n",
        "other numbers following it. To implement a solution for this problem, given a string, we\n",
        "have first to calculate the length of the given array.\n",
        "As per recursive definition of an array, we consider 2 cases:\n",
        "Base case -\n",
        "a. Array of Length 0 - Empty Array (Need not be sorted)\n",
        "b. Array of Length 1 - Array with only one element (Already Sorted)\n",
        "In both these cases, we do not need to sort the array further, and thus return a True value.\n",
        "Recursive Case - This is triggered when our array has more than one element. So, we\n",
        "compare pairs of elements at each invocation of the recursive call and recursively call the\n",
        "next invocation as follows:\n",
        "arr[0] &lt;= arr [1] and isAscending(arr[1:])\n",
        "So, at the first invocation, the elements at positions 0 and 1 are compared, and\n",
        "the AND value of this and the comparison of the next elements of the array is returned.\n",
        "At the end of the unwinding phase, a True value is returned only if the entire array is in\n",
        "ascending order. Let us consider an array: 1, 2, 3, 4 5. The operations take place as follows:\n",
        " 1 &lt; = 2 and isAscending(2,3,4,5)\n",
        " True and 2&lt;=3 and isAscending(3,4,5)\n",
        " True and True and 3&lt;=4 and isAscending(4,5)\n",
        " True and True and True and 4&lt;=5 and True\n",
        " True\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "lS9hWsJSLjVR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def isAscending(arr):\n",
        "  i=0\n",
        "  if(len(arr)<2):\n",
        "    return True\n",
        "  else:\n",
        "    if(i+1<len(arr) and arr[i]<=arr[i+1]):\n",
        "      i+=1\n",
        "      return True*isAscending(arr[i:])\n",
        "    else:\n",
        "      return False\n",
        "\n",
        "\n",
        "arr1 = [1,2,3,4,5]\n",
        "arr2 = [5,4,3,2,1]\n",
        "print(f\"List 1: {arr1}\")\n",
        "if(isAscending(arr1)):\n",
        "  print(\"Ascending\")\n",
        "else:\n",
        "  print(\"Not Ascending\")\n",
        "\n",
        "print(f\"List 2:{arr2}\")\n",
        "if(isAscending(arr2)):\n",
        "  print(\"Ascending\")\n",
        "else:\n",
        "  print(\"Not Ascending\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u1MYhivgLjum",
        "outputId": "3f437c7a-eeb3-40d4-bd96-9a2f2858cf92"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "List 1: [1, 2, 3, 4, 5]\n",
            "Ascending\n",
            "List 2:[5, 4, 3, 2, 1]\n",
            "Not Ascending\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNtK/HHlWci3lzM6gmusSTS"
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
