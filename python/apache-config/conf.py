import yaml
from jinja2 import Environment, FileSystemLoader

with open("data.yml", "r") as f:
    data = yaml.safe_load(f)

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("vhosts.j2")

output = template.render(data)
with open("vhosts.conf", "w") as f:
    f.write(output)
