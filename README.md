# python_final_project
Repo for AAA python course final project

# How does it work?

Basically you have 2 main options:

## 1. menu

Run in the terminal: python pizza.py menu

![elderberry17_2](https://user-images.githubusercontent.com/67886861/199005102-a3aa1d57-a9a2-43e3-9509-1aaf37175dde.JPG)

 ## 2. order
 
Run in the terminal: python pizza.py order *pizza name* *size* [--delivery or --pickup]

![elderberry17_3](https://user-images.githubusercontent.com/67886861/199005574-6ac07d24-08ca-443e-ae49-a2e779f7be46.JPG)


***Default size is XL***, so you can not write this argument

Flags are optional too, because by default ***--pickup is true***, but you can implicit it or call with ***--delivery***

You have 3 types of pizza to choose and 2 sizes, although if smth is wrong, the script will tell you:

![elderberry17_4](https://user-images.githubusercontent.com/67886861/199005695-1c3f2e80-3867-462c-a518-02195eab2163.JPG)


P.S. I have tested annotations with ***mypy***:

![elderberry17_1](https://user-images.githubusercontent.com/67886861/199005849-7ecd6438-f0e1-42a4-bcc4-8c07b4efb518.JPG)



