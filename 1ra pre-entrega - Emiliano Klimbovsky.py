database = [{
    "username":'asd',
    "password":'123'
},
{
    "username":'qwe',
    "password":'345'
}]

def registro(db):
    while (True):
        reg_user=input("Ingrese su nombre de usuario: ")
        reg_passw=input("Ingrese su contraseña: ")
        for reg_user0 in db:
            if reg_user==reg_user0["username"]:
                print("El nombre de usuario ya existe.")
                break
        else:
            user_record=dict()
            user_record["username"] = reg_user
            user_record["password"] = reg_passw
            db.append(user_record)
            print("Usario creado correctamente.")
            return menu()
        
def datareader(db):
    print(db)
    return menu()

def login(db):
    while (True):
        log_user=input("Ingrese su nombre de usuario: ")
        log_passw=input("Ingrese su contraseña: ")
        for log_user0 in db:
            if log_user==log_user0["username"]:
                if log_passw==log_user0["password"]:
                    print("Has iniciado sesión.")
                    return menu()
                else:
                    print("Contraseña incorrecta.")
                    break
        else:
            print("No se ha encontrado el usuario.")

def menu():
    while (True):
        try:
            print("Menú:\n1 = Registrar usuario.\n2 = Iniciar sesión.\n3 = Ver base de datos.")
            option=int(input("Seleccione la opción a la que quiere acceder: "))
            if option==1:
                registro(database)
            elif option==2:
                login(database)
            elif option==3:
                datareader(database)
        except:
            print("Por favor ingrese una opción correcta.")
menu()