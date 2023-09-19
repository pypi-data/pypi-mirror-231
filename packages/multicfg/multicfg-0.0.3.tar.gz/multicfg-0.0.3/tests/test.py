from config import ConfigParser

def show(args):
    print("a =",getattr(args,"a_param","arg is not specified"))
    print("b =",getattr(args,"b_param","arg is not specified"))
    print("c =",getattr(args,"c_param","arg is not specified"))
    
    print("t =",getattr(args,"toml_config","arg is not specified"))

""" Defining and parsing args """
parser = ConfigParser(
	prog="Test program",description="This program is here to test config",
)

parser.add_argument('-a', '--a-param', help='test A param', config_path="global.a", default=None)
parser.add_argument('-b', '--b-param', help='test B param', config_path="global.b", default=None)
parser.add_argument('-c', '--c-param', help='test C param', default=None)

parser.add_argument('-t', '--toml-config', is_config_file=True, help='toml test file', config_type="toml", default=None)

args = parser.parse_args()

""" Start job """
show(args)