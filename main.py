from lista import Lista

def menu_val():
    Options = ['ListA',
                'ListB',
                'ListC',
                'ListD',
                'ListAns',
                'Operacion entre Listas',
                'Salir']
    Option = input('Seleccione la lista: ')
    return Option

if __name__ == '__main__':
    app = True
    action = True

    # Listas
    ListA = Lista("ListA")
    ListB = Lista("ListB")
    ListC = Lista("ListC")
    ListD = Lista("ListD")
    ListAns = Lista("ListAns")

    #Mapa
    Variables = {'ListA': ListA, 'ListB': ListB, 'ListC': ListC, 'ListD': ListD, 'ListAns': ListAns}

    #Punteros
    L=None
    S=None

    while(app):
        action=True
        option_p=menu_val()
        if option_p!="Operacion entre listas" and option_p!="Salir":
            Variables.get(option_p)
        else:
            if option_p=="Operacion entre listas":
                app=False
            elif option_p=="Salir":
                app=False
            else:
                print("Opcion incorrecta")

    ListD.insert_end(5)
    ListD.show_list_details()



