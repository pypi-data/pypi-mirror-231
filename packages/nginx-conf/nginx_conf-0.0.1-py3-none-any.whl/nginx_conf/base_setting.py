import argparse
from pathlib import Path
import os


class BaseSetting(object):

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.args = None

    def args_func(self, parser):
        self.args = parser.parse_args()
        return self.args

    def base_path(self, path):
        return Path(path)

    def path_lib(self, path):
        return Path(path)

    @property
    def service_path(self):
        return self.base_path(self.args.service_dir)

    @property
    def logs_path(self, add_logs_name=True):
        assert self.args.logs_dir
        logs_path = self.base_path(self.args.service_dir)
        if add_logs_name:
            logs_path /= self.args.logs_dir
        logs_path.mkdir(parents=True, exist_ok=True)
        return logs_path

    @property
    def static_path(self):
        assert self.args.static_dir
        path = self.base_path(self.args.service_dir)
        path /= self.args.static_dir
        path.mkdir(parents=True, exist_ok=True)
        return path

    def folder_exists(self, folder_path):
        if os.path.exists(folder_path):
            return True
        else:
            return False

    @property
    def virtualenv_path(self):
        flag = self.folder_exists(self.args.virtualenv_dir)
        if flag:
            return self.args.virtualenv_dir
        else:
            raise "虚拟环境不存在"

    def traverse_nginx_directory(self, directory):
        conf = 'conf'
        for _, dirs, _ in os.walk(directory):
            if conf in dirs:
                nginx_conf_path = self.base_path(directory) / conf
                return nginx_conf_path
            else:
                nginx_conf_path = self.base_path(directory) / conf
                nginx_conf_path.mkdir(parents=True, exist_ok=True)
                return nginx_conf_path
    @property
    def nginx_conf_file(self):
        path = self.traverse_nginx_directory(self.args.nginx_conf_dir)
        return path / f"{self.args.service_name}.conf"
