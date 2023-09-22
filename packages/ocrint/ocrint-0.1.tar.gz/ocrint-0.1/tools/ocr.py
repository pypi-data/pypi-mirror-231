from ocrint.tools.utils import *
from ocrint.tools.report import *


class Ocr:

    # Fonction qui ouvre la fenetre pour selectionner un dossier et renvoie la liste des paths des fichiers
    def get_files(self):
        """
        Fonction qui ouvre la fenetre pour selectionner un dossier et renvoie la liste des paths des fichiers
        :return: list
        """
        return get_folder_from_tk()

    def get_urls(self):
        """
        Fonction qui ouvre la fenetre pour entrer des urls et renvoie la liste des urls
        :return: list
        """
        return get_urls_from_tk()

    # Fonction qui renvoie le texte d'un fichier
    def get_text(self, filenames=list, parent_path=str):
        """
        Fonction qui renvoie le texte d'un fichier
        :param filenames: list
        :return: list
        """
        return ocr_space_file_multithread(filenames=filenames, parent_path=parent_path, language='eng')

    # Fonction pour récuperer le texte à partir d'une url
    def get_text_url(self, url):
        """
        Fonction pour récuperer le texte à partir d'une url
        :param url: str
        :return: str
        """
        return ocr_space_url(url=url, language='eng')

    def start_folder(self):
        """
        Fonction qui renvoie le texte de tous les fichiers d'un dossier
        :return: list
        """
        files = self.get_files()

        save_path = get_folder_save()

        get_text = self.get_text(filenames=files, parent_path=save_path)
        json_report = report_json(parent_path=save_path, data=get_text)

        return json_report

    def start_url(self):
        """
        Fonction qui renvoie le texte de tous les fichiers d'un dossier
        :return: list
        """
        urls = self.get_urls()

        return json.dumps(self.get_text_url(urls))

