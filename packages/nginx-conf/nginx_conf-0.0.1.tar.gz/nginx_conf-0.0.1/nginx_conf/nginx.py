from nginx_conf.base_setting import BaseSetting
from nginx_conf.utils import str2bool


class Nginx(BaseSetting):
    def __init__(self, nginx_conf):
        super().__init__()
        nginx_parser = self.parser
        nginx_parser.add_argument("--nginx_host", type=str, help="nginx域名",
                                  default=0 if not nginx_conf.get('nginx_host') else nginx_conf.get('nginx_host'))
        nginx_parser.add_argument("--nginx_port", type=int, default=nginx_conf.get('nginx_port'), help="nginx端口")
        nginx_parser.add_argument("--uwsgi_port", type=int, default=nginx_conf.get('uwsgi_port'), help="uwsgi端口号")
        nginx_parser.add_argument("--nginx_conf_dir", type=str, default=nginx_conf.get('nginx_conf_dir'),
                                  help="nginx配置目录")
        nginx_parser.add_argument("--service_name", type=str, default=nginx_conf.get('service_name'),
                                  help="nginx配置文件名称/项目名称")
        nginx_parser.add_argument("--uwsgi_path", type=str, default=nginx_conf.get('uwsgi_path'),
                                  help="uwsgi.ini文件路径")
        nginx_parser.add_argument("--logs_dir", type=str, default=nginx_conf.get('logs_dir'), help="nginx日志目录")
        nginx_parser.add_argument("--static_dir", type=str, default=nginx_conf.get('static_dir'), help="静态文件目录")
        nginx_parser.add_argument("--service_dir", type=str, default=nginx_conf.get('service_dir'), help="项目目录")

        self.nginx_args = self.args_func(nginx_parser)

    def gen_nginx(self):
        assert self.folder_exists(self.args.uwsgi_path), '生成uwsgi才可以生成nginx配置'
        assert self.args.nginx_host, "请设置nginx域名"
        nginx_file_path = self.nginx_conf_file
        nginx_file_path.write_text(f"""
server{{
  listen {self.args.uwsgi_port};
  server_name {self.args.nginx_host};
  access_log {self.logs_path}/nginx-access.log;
  error_log {self.logs_path}/nginx-error.log;
  location /static/ {{
    alias {self.static_path}/;
  }}

  location / {{
    if ($request_method ~* HEAD)
    {{
      return 200;
    }}
    include uwsgi_params;
    uwsgi_connect_timeout   10;
    uwsgi_send_timeout      600;
    uwsgi_read_timeout      600;
    uwsgi_pass 127.0.0.1:{self.args.uwsgi_port};
  }}
}}
""", encoding='utf8')
        return nginx_file_path

