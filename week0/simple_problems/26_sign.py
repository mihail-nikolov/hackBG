signs = {1: ["Capricorn", 20, "Aquarius"],
        2:  ["Aquarius", 19, "Pisces"],
        3:  ["Pisces", 20, "Aries"],
        4:  ["Aries", 20, "Taurus"],
        5:  ["Taurus", 21, "Gemini"],
        6:  ["Gemini", 21, "Cancer"],
        7:  ["Cancer", 22, "Leo"],
        8:  ["Leo", 22, "Virgo"],
        9:  ["Virgo", 23, "Libra"],
        10: ["Libra", 23, "Scorpio"],
        11: ["Scorpio", 22, "Saggitarius"],
        12: ["Saggitarius", 21, "Capricorn"]
}


def my_sign(month,day):
    for key in signs:
        if month == key:
            arr = signs[key]
            for i in range(len(arr)):
                if day <= arr[1]:
                    sign = arr[0]
                else:
                    sign = arr[2]
    return sign


print(my_sign(11, 24))
