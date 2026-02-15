import csv
import os
import sys

import transforms
from extensions import registry
from maltego_trx.handler import handle_run
from maltego_trx.registry import register_transform_classes
from maltego_trx.server import app as application

register_transform_classes(transforms)

registry.write_transforms_config(include_output_entities=True)
registry.write_settings_config()

# print( f"quanti elementi in argv:  {len(sys.argv)} ")





def _ensure_brave_settings():
    settings_path = os.path.join(os.path.dirname(__file__), "settings.csv")
    required_settings = [
        ("count", "string", "count", "", "true", "true"),
        ("offset", "string", "offset", "", "true", "true"),
        ("freshness", "string", "freshness", "", "true", "true"),
        ("country", "string", "country", "", "true", "true"),
        ("search_lang", "string", "search_lang", "", "true", "true"),
        ("extra_snippets", "string", "extra_snippets", "", "true", "true"),
        ("goggles", "string", "goggles", "", "true", "true"),
    ]

    if os.path.exists(settings_path):
        with open(settings_path, newline="") as f:
            reader = csv.reader(f)
            rows = list(reader)
    else:
        rows = [["Name", "Type", "Display", "DefaultValue", "Optional", "Popup"]]

    header = rows[0] if rows else ["Name", "Type", "Display", "DefaultValue", "Optional", "Popup"]
    existing = {row[0] for row in rows[1:] if row}
    for setting in required_settings:
        if setting[0] not in existing:
            rows.append(list(setting))

    with open(settings_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in rows[1:]:
            writer.writerow(row)

    transforms_path = os.path.join(os.path.dirname(__file__), "transforms.csv")
    if not os.path.exists(transforms_path):
        return

    with open(transforms_path, newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []

    if "transformSettingIDs" not in fieldnames:
        return

    setting_map = {
        "getbraveaiwebsearch": "count;offset;freshness;country;search_lang;extra_snippets;goggles",
        "getbraveainewssearch": "count;offset;freshness;country;search_lang;extra_snippets;goggles",
        "getbraveaiimagesearch": "count;country;search_lang",
    }

    for row in rows:
        name = row.get("Name", "")
        if name in setting_map:
            row["transformSettingIDs"] = setting_map[name]

    with open(transforms_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


_ensure_brave_settings()

""" crea il file  mtz per le  trasformate """
registry.write_local_mtz()

# registry.write_local_mtz(
#     mtz_path: str = "./local.mtz", # path to the local .mtz file
#     working_dir: str = ".",
#     command: str = "python3", # for a venv you might want to use `./venv/bin/python3`
#     params: str = "project.py",
#     debug: bool = True
# )


if __name__ == '__main__':
    # handle_run(__name__, sys.argv, application,debug=True)
     # print("test ok stò provando")
    ssl_context = ('cert.pem', 'key.pem')  # Il tuo certificato e chiave
    # print( f"quanti elementi in argv:  {len(sys.argv)} ")
    
    # # Leggi il contenuto del file XML
    # with open("xml_Request.xml", 'r') as file:
    #     xml_data = file.read()


    # sys.argv.extend([xml_data])
    # print( f"quanti elementi in argv:  {len(sys.argv)} ")

  
    handle_run(__name__, sys.argv, application, ssl_context=ssl_context)

# print( f"quanti elementi in argv:  {len(sys.argv)} ")
# print  ('\n'.join(f" Valore:  {valore} "   for   valore  in  sys.argv)   )
