while True:
    try: 
        x = int(input("¿Cuál es x? "))
    except ValueError:
        print("x no es entero")
    else: 
        break

print(f"x es {x}")

