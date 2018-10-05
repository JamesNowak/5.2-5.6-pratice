def main():
    fat_con = float(input("How many grams of fat did you eat? "))
    carbs_con = float(input("How many grams of carbs did you eat? "))
    protein_con = float(input("How many grams of protein did you eat? "))
    print("You consumed", func_fat(fat_con), "fat calories." )
    print("You consumed", func_carb(carbs_con), "carbs calories." )
    print("You consumed", func_protein(protein_con), "fat calories." )
    print("You consumed", (func_protein(protein_con)+ func_carb(carbs_con)+ func_fat(fat_con)), "fat calories." )

def func_fat(fat_con):
    fat_cal = fat_con * 9
    return fat_cal


def func_carb(carbs_con):
    carb_cal = carbs_con *4
    return carb_cal


def func_protein(protein_con):
    protein_cal = protein_con *4
    return protein_cal

main()
