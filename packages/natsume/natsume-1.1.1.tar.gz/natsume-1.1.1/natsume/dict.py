import os
import shutil
import json
import pkg_resources
from urllib.request import urlretrieve
import zipfile
from tqdm.auto import tqdm


DICT_URLS = {
    "naist-jdic": "https://github.com/faruzan0820/natsume/releases/download/naist-jdic/naist-jdic.tar.gz",
    "naist-jdic-tdmelodic": "https://github.com/faruzan0820/natsume/releases/download/naist-jdic-tdmelodic/naist-jdic-tdmelodic.tar.gz"
}

# Reference: https://github.com/r9y9/pyopenjtalk/blob/master/pyopenjtalk/__init__.py    
class DictManager(object):
    """Dictionary manager.
    """

    def __init__(self):
        """Initialize dictionary manager.
        """

        self._config_path = pkg_resources.resource_filename(__name__, "config.json")   # hardcode
        self._config = self.load_config()
        self._dict_dir = self._config.get("dict_dir", "")

        self._available_dict_names = list(DICT_URLS.keys())
        self._default_dict_name = list(DICT_URLS.keys())[0]
        self._default_dict_dir = pkg_resources.resource_filename(__name__, self._default_dict_name)

    def get_dict_dir(self, dict_name=None) -> str:
        """Get dictionary directory path.

        Args:
            dict_name (str): Dictionary name. Defaults to None.

        Returns:
            str: dictionary Directory path.
        """

        if dict_name is None:
            # use most recently used dict or download a default dict
            if self.check_dict_dir(self._dict_dir):
                # most recently used dict is availabel
                return self._dict_dir
            
            if self.check_dict_dir(self._default_dict_dir):
                self._config["dict_name"] = self._default_dict_name
                self._config["dict_dir"] = self._default_dict_dir
                self.save_config()

                return self._default_dict_dir
            
            # download default dictionary
            print("No dictionary available, download {}.".format(self._default_dict_name))
            dict_dir = self.download_dict(self._default_dict_name)
        else:
            if dict_name not in self._available_dict_names:
                raise ValueError("No such dictionary available. Expected {}."
                                .format(", ".join(self._available_dict_names)))

            dict_dir = pkg_resources.resource_filename(__name__, dict_name)
            if not self.check_dict_dir(dict_dir):
                # not available
                print("{} is not downloaded.".format(dict_name))
                self.download_dict(dict_name)

        return dict_dir

    @staticmethod
    def check_dict_dir(dict_dir: str) -> bool:
        """Check availability of given dictionary directory path.

        Args:
            dict_dir (str): Dictionary directory path.

        Returns:
            bool: Whether the input directory path is available.
        """

        if os.path.exists(dict_dir) and os.path.isdir(dict_dir):
            return True
        return False
    
    def download_dict(self, dict_name: str) -> str:
        """Download dictionary.

        Args:
            dict_name (str): Dictionary name.

        Returns:
            str: Directory path of the downloaded dictionary.
        """

        if dict_name not in self._available_dict_names:
            raise ValueError("No such dictionary available. Expected {}."
                            .format(", ".join(self._available_dict_names)))
        
        dict_url = DICT_URLS[dict_name]
        self._config["dict_name"] = dict_name

        # download and show progress
        filename = pkg_resources.resource_filename(__name__, "dic.zip")
        print("Downloading dictionary from {}...".format(dict_url))
        with TqdmUpTo(unit='B', unit_scale=True, miniters=1, desc="dic.zip") as t: 
            urlretrieve(dict_url, filename=filename, reporthook=t.update_to, data=None)
            t.total = t.n

        print("Extracting file {}...".format(filename))
        with zipfile.ZipFile(filename, mode="r") as f:
            f.extractall(path=pkg_resources.resource_filename(__name__, dict_name))
        
        # save config
        dict_dir = pkg_resources.resource_filename(__name__, dict_name)
        self._config["dict_dir"] = dict_dir
        self.save_config()
        print("Successfully downloaded {} to {}.".format(dict_name, dict_dir))

        # remove zip file
        os.remove(filename) 

        return dict_dir
    
    def create_config(self) -> dict:
        """Creat config file.

        Returns:
            dict: Config dict.
        """

        config = {
            "dict_name": "",
            "dict_dir": ""
        }
        with open(self._config_path, "w", encoding="utf-8") as f:
            json.dump(config, f)

        return config

    def load_config(self) -> dict:
        """Load config from file.

        Returns:
            dict: Config dict.
        """

        if not os.path.exists(self._config_path):
            config = self.create_config()
        else:
            with open(self._config_path, "r", encoding="utf-8") as f:
                config = json.load(f)

        return config
    
    def save_config(self) -> None:
        """Save config to file.
        """
        
        with open(self._config_path, "w", encoding="utf-8") as f:
            json.dump(self._config, f)


# Reference: https://github.com/tqdm/tqdm#hooks-and-callbacks
class TqdmUpTo(tqdm):
    """Provides `update_to(n)` which uses `tqdm.update(delta_n)`."""
    def update_to(self, b=1, bsize=1, tsize=None):
        """
        b  : int, optional
            Number of blocks transferred so far [default: 1].
        bsize  : int, optional
            Size of each block (in tqdm units) [default: 1].
        tsize  : int, optional
            Total size (in tqdm units). If [default: None] remains unchanged.
        """

        if tsize is not None:
            self.total = tsize
        return self.update(b * bsize - self.n)  # also sets self.n = b * bsize