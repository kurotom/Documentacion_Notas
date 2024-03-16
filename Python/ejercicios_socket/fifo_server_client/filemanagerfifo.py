"""
Clase encargada de la administración del fichero.
"""

import os
from hashlib import md5
from typing import List, Union

from models import UserData, File


class FileManager:
    """
    """

    def prepare_directory(
        self,
        directory_path: str,
        client_hash: str
    ) -> list:
        """
        """
        result = []
        for file in os.listdir(directory_path):
            path = os.path.join(directory_path, file)
            file_object = self.prepare_file(
                                    file_path=path,
                                    client_hash=client_hash
                                )
            result.append(file_object)
        return result

    def prepare_file(
        self,
        file_path: str,
        client_hash: str
    ) -> File:
        """
        """
        file_path = file_path
        file = File()
        file.client_hash = client_hash
        file.filepath = file_path
        file.filename = os.path.basename(file.filepath)
        file.size = file.get_size(file_path)
        file.md5 = file.get_md5_hash(file=file.filepath)
        file.chunks = file.chunkenizer(file=file.filepath)
        return file

    def find_file(
        self,
        directory: str,
        filename: str
    ) -> Union[File, None]:
        """
        """
        if os.path.exists(directory):
            for item in os.listdir(directory):
                if item == filename:
                    path_file = os.path.join(directory, item)
                    return self.prepare_file(
                                file_path=path_file,
                                client_hash=directory
                            )
        else:
            return None

    def delete_file(
        self,
        file: File,
    ) -> bool:
        """
        """
        if file is not None:
            if os.path.exists(file.filepath):
                os.remove(file.filepath)
                return True
        else:
            return False

    def list_directory(
        self,
        path: str
    ) -> Union[list, None]:
        """
        """
        data = []
        if os.path.exists(path):
            for item in os.listdir(path):
                file_path = os.path.join(path, item)
                print(file_path, os.path.exists(file_path))
                file = File()
                file.filepath = file_path
                file.filename = os.path.basename(file.filepath)
                file.size = file.get_size(file_path)
                file.md5 = file.get_md5_hash(file=file.filepath)

                file_data = {
                    'file': file.filename,
                    'size': file.size,
                    'md5': file.md5
                }
                data.append(file_data)
        return data

    def make_directory(
        self,
        directory: str
    ) -> str:
        path = os.path.abspath(directory)
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    def save_file(
        self,
        file: File,
        path: str = None,
    ) -> bool:
        """
        """
        file_path = ""
        if path is not None:
            file_path = os.path.join(path, file.filename)
            if file.filepath is None:
                file.filepath = os.path.abspath(file_path)

        return self.write(fileObj=file)

    def write(
        self,
        fileObj: File
    ) -> bool:
        """
        """
        with open(fileObj.filepath, 'wb') as file:
            file.writelines(fileObj.chunks)

        return self.check_integrity(fileObj.md5, fileObj.filepath)

    def check_integrity(
        self,
        hash_origin,
        path_file
    ) -> bool:
        """
        """
        file_hash = ''
        with open(path_file, 'rb') as fl:
            file_hash = md5(fl.read()).hexdigest()
        return file_hash == hash_origin
