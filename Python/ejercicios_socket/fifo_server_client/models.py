"""
Clases que represetan a usuarios (UserData) y ficheros (File).
"""

from hashlib import md5
import os


class UserData:
    """
    Clase representa a Usuario.
    """
    def __init__(
        self,
        username: str
    ) -> None:
        """
        Constructor.
        """
        self.username = username

    def genhash(self) -> str:
        """
        Retorna hash MD5 para el cliente.
        """
        return md5(self.username.encode()).hexdigest()

    def __str__(self) -> str:
        """
        """
        return '%s - %s' % (self.username, self.genhash())


class File:
    """
    Clase File, representa los ficheros de usuario. Almacena la metadata y
    los chunks del fichero original.
    """
    def __init__(self) -> None:
        """
        """
        self.client_hash = None
        self.filepath = None
        self.filename = None
        self.size = None
        self.md5 = None
        self.chunks = []

    def build(self) -> bytes:
        return b''.join(self.chunks)

    def chunkenizer(
        self,
        file: str,
        size_chunk: int = 1024
    ) -> list:
        """
        """
        chunks = []
        with open(file, 'rb') as fileb:
            while True:
                chunk = fileb.read(size_chunk)
                if not chunk:
                    break
                chunks.append(chunk)
        return chunks

    def get_md5_hash(
        self,
        file: str
    ) -> md5:
        with open(file, 'rb') as fl:
            return md5(fl.read()).hexdigest()

    def get_metadata(self) -> dict:
        return {
            'filename': self.filename,
            'size': self.size,
            'md5': self.md5,
        }

    def get_size(
        self,
        file: str
    ) -> int:
        return os.path.getsize(file)

    def __str__(self) -> str:
        return '%s, %s, %s' % (self.client_hash, self.md5, self.filename)

    def __repr__(self) -> str:
        return '%s, %s, %s' % (self.client_hash, self.md5, self.filename)
