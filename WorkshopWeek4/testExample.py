teams=15*int(input("How many teams?"))

if (teams%48)>=20:
    print("Hire ", teams // 48+1, "Big buses and", 0, "small buses")
    print("cost=$", (teams // 48+1)*200.0)
else:
    print("Hire ", teams // 48, "Big buses and", (teams % 48 // 10)+1, "small buses")
    print("cost=$", ((teams // 48) * 200.0)+((teams % 48 // 10)+1)*95.0)
