from nginx_conf.base_setting import BaseSetting
from nginx_conf.utils import str2bool


class Uwsgi(BaseSetting):

    def __init__(self, uwsgi_conf):
        super().__init__()
        uwsgi_parser = self.parser
        uwsgi_parser.add_argument("--uwsgi_port", type=int, default=uwsgi_conf.get('uwsgi_port'), help="uwsgi端口号")
        uwsgi_parser.add_argument("--nginx_port", type=int,
                                  default=80 if not uwsgi_conf.get('nginx_port') else uwsgi_conf.get('nginx_port'),
                                  help="uwsgi端口号")
        uwsgi_parser.add_argument("--service_dir", type=str, default=uwsgi_conf.get('service_dir'), help="项目目录")
        uwsgi_parser.add_argument("--conf_dir", type=str, default=uwsgi_conf.get('conf_dir'), help="项目配置目录")
        uwsgi_parser.add_argument("--virtualenv_dir", type=str, default=uwsgi_conf.get('virtualenv_dir'),
                                  help="虚拟环境配置目录")
        uwsgi_parser.add_argument("--logs_dir", type=str, default=uwsgi_conf.get('logs_dir'), help="uwsgi日志目录")
        uwsgi_parser.add_argument("-u", "--gen_uwsgi", type=str2bool, default=True,
                                  help="生成uwsgi")
        self.uwsgi_args = self.args_func(uwsgi_parser)

    def gen_uwsgi(self):
        assert self.uwsgi_args.uwsgi_port != 0, "请设置uwsgi端口"
        project_name = self.uwsgi_args.service_dir.split('/')[-1]
        if self.uwsgi_args.conf_dir:
            uwsgi_file = self.path_lib(self.uwsgi_args.service_dir) / self.uwsgi_args.conf_dir / "uwsgi.ini"
            service_dir = self.path_lib(self.uwsgi_args.service_dir) / self.uwsgi_args.conf_dir
        else:
            uwsgi_file = self.path_lib(self.uwsgi_args.service_dir) / "uwsgi.ini"
            service_dir = self.uwsgi_args.service_dir
        uwsgi_file.write_text(f"""
[uwsgi]
uwsgi-socket=:{self.uwsgi_args.nginx_port}
env = IS_DEBUG=0
chdir={self.service_path}
module={project_name}.wsgi:application
master=True
processes=16
harakiri=1800
pidfile={service_dir}/uwsgi.pid
vacuum=True
max-requests=10000
max-requests-delta=100
#enable-threads=True
virtualenv = {self.virtualenv_path}
daemonize={self.logs_path}/uwsgi.log
log-maxsize=104857600
reload-on-rss=240
reload-mercy=180
max-worker-lifetime=3600
post-buffering=262144
post-buffering-bufsize=262144
#gevent=1000
stats={service_dir}/uwsgi_stat.sock
""", encoding='utf8')
        return uwsgi_file
