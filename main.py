def count_occurrences(list_of_numbers, number):
    count=0
    for number in list_of_numbers:
        if number == number:
            count +=1
    return count
if __name__=="__main__":

    list_of_numbers = []
    while True:
        number = input("Введіть число: ")
        if number == "":
            break
        list_of_numbers.append(int(number))

    number = int(input("Введіть число, кількість появ якого необхідно порахувати: "))
    print("Кількість разів,коли число {} присутнє в списку: {}".format(
        number,count_occurrences(list_of_numbers,number)))
