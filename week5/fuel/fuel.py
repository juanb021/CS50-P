def main():
    num = input("Fraction: ")
    percent = convert(num)
    print(gauge(percent))


def convert(fraction):
    while True:
        try:
            x, y = fraction.split('/')
            nx = int(x)
            ny = int(y)
            fraction = (nx / ny)
            p = int(fraction * 100)
            if p <= 100:
                return p
            else:
                fraction = input("Fraction: ")

        # Verificar si y != es 0 y Verificar si el input no es un int
        except (ZeroDivisionError, ValueError, TypeError):
            fraction = input("Fraction: ")
            raise

def gauge(percentage):
    if percentage <= 1:
        result = "E"
    elif percentage >= 99:
        result = "F"
    else:
        result = str(percentage)+"%"
    return result


if __name__ == "__main__":
    main()