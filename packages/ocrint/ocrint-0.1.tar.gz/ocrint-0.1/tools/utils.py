import requests
import json
import os
import concurrent.futures
from dotenv import load_dotenv
load_dotenv()
from progress.spinner import MoonSpinner

SAVE_PATH_DIRECTORY = ''
OCR_API_KEY = os.environ.get('OCR_API_KEY')


def process_file(filename, overlay=False, api_key=OCR_API_KEY, language='eng'):
    spinner = MoonSpinner(f'Traitement en cours pour {filename}... ')
    spinner.start()

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language}
    print(filename)
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload)
        parsed_text = check_response(r.content.decode())

        if parsed_text:
            save_path = f'{SAVE_PATH_DIRECTORY}/{filename}.txt'
            print(f'Création du fichier {save_path}...')
            create_file(save_path, parsed_text)
            out = {
                'filename': filename,
                'text': parsed_text
            }
            spinner.finish()
            return out

    spinner.finish()
    return None


def ocr_space_file_multithread(filenames, parent_path=str, overlay=False, api_key=OCR_API_KEY, language='eng'):
    results_images_text = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_file, filename, overlay, api_key, language) for filename in filenames]

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                results_images_text.append(result)

    return results_images_text


def check_response(response):
    status = extract_ocr_data(response)
    if status:
        return status
    else:
        return False


def extract_ocr_data(json_string):
    try:
        # Analysez la chaîne JSON en un dictionnaire Python
        json_data = json.loads(json_string)
        print(json_data)
        # Vérifiez si le JSON contient des résultats d'OCR
        if "ParsedResults" in json_data and len(json_data["ParsedResults"]) > 0:
            # Récupérez le texte OCR à partir du premier élément de ParsedResults
            ocr_text = json_data["ParsedResults"][0]["ParsedText"]

            return ocr_text
        else:
            print("Error occurred. Details1: " + json_data["ErrorMessage"])
            return False
    except Exception as e:
        print("Error occurred. Details2: " + str(e))
        return False


def ocr_space_url(url, overlay=False, api_key=OCR_API_KEY, language='eng'):
    """ OCR.space API request with remote file.
        Python3.5 - not tested on 2.7
    :param url: Image url.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()


#  Fonction qui recupere tous les fichiers d'un dossier et renvoie une liste de leur path
def get_files(path):
    import os
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
    return files


# Fonction qui permet d'ouvrir une fenetre pour selectionner un dossier est renvoie le path du dossier
def get_folder_from_tk():
    import os
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()
    root.title("OCR folder")
    folder_selected = filedialog.askdirectory()
    files = []
    for r, d, f in os.walk(folder_selected):
        for file in f:
            files.append(os.path.join(r, file))
    return files


def get_folder_save():
    import os
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    #  title
    root.title("OCR save results directory")
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected


# Fonction qui permet d'ouvrir une fenetre avec une entrée type texte area pour entrée une liste d'urls et un bouton pour valider
# puis retourne un liste des urls entrées. Créer une vérification des urls entrées avec une regex
# est insere les urls valides dans la liste
def get_urls_from_tk():
    import tkinter as tk
    from tkinter import simpledialog
    root = tk.Tk()
    root.withdraw()
    urls = []
    while True:
        url = simpledialog.askstring(title="Urls", prompt="Entrez une url")
        if url == None:
            break

        urls.append(url)
    return urls
