import pandas as pd

def f(x):
    if x < 4:
        return 1
    if x < 7:
        return 2
    return 3


def rm_main(input0):
    df = input0

    # Modificar a numerico los valores booleanos nominales:
    df['Verified'] = df['Verified'].replace('VERDADERO',1)
    df['Verified'] = df['Verified'].replace('FALSO',0)

    df['Recommended'] = df['Recommended'].replace('yes',1)
    df['Recommended'] = df['Recommended'].replace('no',0)

    df['Overall_Rating'] = df['Overall_Rating'].apply(f)

    return df 

