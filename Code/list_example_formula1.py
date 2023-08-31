
def extend_list(list_old, list_new):
    list_old = list_old.extend(list_new)
    return list_old

def spell_check(list_verified):
    loop_index = 0
    for name in list_verified:
        list_verified[loop_index] = SpellChecker.correction(list_verified[loop_index] )
        loop_index+=1
# return corrected list
    return list_verified
# drivwers names
drivers = ["Charles", "Pierre", "Valterri", "Lewis", "George","Lando"]
# other group drives
others = ["Blue", "Elton", "Colt"]
# extneding the list
extend_list(drivers, others)

# spell check
spell_check(drivers)

print(drivers)


