import csv
import deep_translator

if __name__ == '__main__':
    item_count = input("Item count: ")
    langs = input("Languages: ").split(",")
    menu_id = input("Menu ID: ")
    category_id = input("Category ID: ")
    with open('items.csv', mode='w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id","menu","category","title"] + [f"title_{lang}" for lang in langs] + ["ingredients"] + [f"ingredients_{lang}" for lang in langs] + ["price","compare_at_price","image","group","vegan","combo"])
    for i in range(int(item_count)):
        title = input("Title: ")
        ingredients = input("Ingredients: ")
        price = input("Price: ")
        group = input("Group? (Y/N) ") == "Y"
        vegan = input("Vegan? (Y/N) ") == "Y"
        combo = input("Combo? (Y/N) ") == "Y"
        # write to csv
        with open('items.csv', mode='a', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            # writer.writerow(["id","menu","category","title"] + [f"title_{lang}" for lang in langs] + ["ingredients"] + [f"ingredients_{lang}" for lang in langs] + ["price","compare_at_price","image","group","vegan","combo"])
            writer.writerow(["",menu_id,category_id,title] + [deep_translator.GoogleTranslator(source='auto', target=lang).translate(title) for lang in langs] + [ingredients] + [deep_translator.GoogleTranslator(source='auto', target=lang).translate(ingredients) for lang in langs] + [price,"","",group,vegan,combo])
    print("Done!")
