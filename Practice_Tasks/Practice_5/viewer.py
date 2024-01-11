def read_file(file):
    f = open(file, mode='r', encoding='utf-8')
    count_numbers = int(f.readline())
    numbers_list = list(f.read().splitlines())
    int_numbers = []
    for i in range(count_numbers):
        int_numbers.append(int(i))

    print(numbers_list)


def Try():
    try:
        file_name = input('Введите название файла: ')
        read_file(file_name)

    except TypeError:
         print("Проверьте тип данных")

    except FileNotFoundError:
        print("Данного файла не существует")

    except OSError:
        print("Ошибка операционной системы")

    except ValueError:
        print("Проверьте символы в файле")

    except:
        print("Произошла тотальная ошибка!")


if __name__ == "__main__":
    Try()