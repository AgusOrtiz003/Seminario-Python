def clasificarVelocidad(time):
    cat="Categoría: "
    if(time<200):
        cat+="Rápido"
    elif(time<500):
        cat+="Normal"
    else:
        cat+="Lento"
    return cat