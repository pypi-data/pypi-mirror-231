import shutil
from zipfile import ZipFile
import os
import yaml
import click
from beeprint import pp
from .utils import convert_to_pascalcase, detect_omoospace_yml, receding_path


@click.group()
def cli():
    pass


@click.command('test')
@click.argument("name", required=False)
@click.option("-c", "--contents", multiple=True,
              help="Where to create the OmooSpace")
def test(name, contents):
    print(name)
    click.echo(os.path.abspath("."))


@click.command('create', help="Create New OmooSpace🪐")
@click.argument("name")
@click.option("-d", "--directory", default=".",
              help="Where to create the OmooSpace🪐")
@click.option("-t", "--template", default=".",
              help="Where to create the OmooSpace🪐")
def create_omoospace(name, directory, contents):
    space_name = convert_to_pascalcase(name)
    space_root = os.path.join(directory, space_name)

    main_folders = [
        "Contents",
        "ExternalData",
        "SourceFiles",
        "References",
        "StagedData"
    ]
    contents_subfolders = [convert_to_pascalcase(
        folder) for folder in contents]

    try:
        # create root folder
        os.makedirs(space_root, exist_ok=True)

        # create main folders
        for folder in main_folders:
            os.makedirs(os.path.join(space_root, folder), exist_ok=True)

        # create contents subfolders
        for folder in contents_subfolders:
            os.makedirs(os.path.join(
                space_root, 'Contents', folder), exist_ok=True)

        spcae_info = {
            "name": space_name,
            "members": [],
            "softwares": [],
            "works": [],
        }

        space_yml_path = os.path.join(space_root, 'OmooSpace.yml')

        with open(space_yml_path, 'w') as file:
            yaml.safe_dump(spcae_info, file, sort_keys=False)
    except Exception as err:
        print('Fail to create folders', err)


@click.command('info', help="Get OmooSpace's info")
def print_omoospace_info():
    space_root, space_info = detect_omoospace_yml()
    if not space_info:
        return

    externaldata_dir = os.path.join(space_root, 'ExternalData')
    external_cargos = []
    subdirs = [f.path for f in os.scandir(externaldata_dir) if f.is_dir()]
    print(subdirs)
    for dir in subdirs:
        carge_yml_path = os.path.join(dir, 'OmooCargo.yml')
        if (os.path.exists(carge_yml_path)):
            with open(carge_yml_path, 'r') as file:
                cargo_info = yaml.safe_load(file)
            pp(cargo_info, sort_keys=False)
            external_cargos.append(
                "%s: %s" % (cargo_info['name'], cargo_info['version']))

    space_info['[cargos]'] = external_cargos
    print("(%s)" % space_root)
    pp(space_info, sort_keys=False)


@click.command('export', help="Export OmooCargo📦")
@click.argument("items_paths", nargs=-1, type=click.Path(exists=True, resolve_path=True))
@click.option("-o", "--output", default="..",
              help="Where to create the OmooSpace🪐")
@click.option("-n", "--name",
              help="Where to create the OmooSpace🪐")
@click.option("-d", "--description",
              help="Where to create the OmooSpace🪐")
@click.option("-v", "--version",
              help="Where to create the OmooSpace🪐")
def export_omoocargo(items_paths, output='..', name=None, description=None, version=None):
    space_root, space_info = detect_omoospace_yml()
    if not space_info:
        return
    if(len(items_paths)==0):
        print('Export Failed, at least one item')
        return
    cargo_root = space_root
    cargo_yml_path = os.path.join(cargo_root, 'OmooCargo.yml')
    cargo_md_path = os.path.join(cargo_root, 'README.md')
    cargo_name = space_info['name'] if not name else convert_to_pascalcase(
        name)
    cargo_path = os.path.join(output, cargo_name+'.zip')
    # TODO: Check if there is a OmooCargo on path

    # Gethering info
    cargo_items = []
    for path in items_paths:
        if (os.path.isfile(path)):
            cargo_items.append(os.path.relpath(path, space_root))
    cargo_description = "A OmooCargo for transporting creations" if not description else description
    cargo_version = "0.1.0" if not version else version

    cargo_info = {
        "name": cargo_name,
        "version": cargo_version,
        "description": cargo_description,
        "authors": [
            {"name": "Ma Nan"}
        ],
    }

    pp(cargo_info)
    pp(cargo_items)

    with open(cargo_yml_path, 'w') as file:
        yaml.safe_dump(cargo_info, file, sort_keys=False)

    with open(cargo_md_path, 'w') as file:
        file.write('# %s\n' % cargo_name)
        file.write(
            "A [OmooCargo]('https://uj6xfhbzp0.feishu.cn/wiki/wikcnb0w8Q5FgDyMcJiuK4zYfyd?from=from_copylink') for transporting creations\n")
        file.write('## Cargo Info\n')
        file.write('**version:** %s  \n' % cargo_info['version'])
        file.write('**authors:**\n')
        for author in cargo_info['authors']:
            file.write("- %s\n" % author['name'])
        file.write('## Items List\n')
        for item in cargo_items:
            file.write("- %s\n" % item)

    try:
        with ZipFile(cargo_path, 'w') as zip:
            # Add multiple files to the zip
            zip.write(cargo_yml_path, 'OmooCargo.yml')
            zip.write(cargo_md_path, 'README.md')
            for item in cargo_items:
                zip.write(os.path.abspath(item), item)
    except Exception as err:
        print('Fail to export OmooCargo', err)

    os.remove(cargo_yml_path)
    os.remove(cargo_md_path)


@click.command('import', help="Import OmooCargo📦")
@click.argument("cargo_path")
def import_omoocargo(cargo_path):
    space_root, space_info = detect_omoospace_yml()
    if not space_info:
        return

    with ZipFile(cargo_path, 'r') as zip:
        with zip.open('OmooCargo.yml') as file:
            cargo_info = yaml.safe_load(file)

        cargo_shipping_dir = os.path.join(
            space_root, 'ExternalData', cargo_info['name'])

        # Clean shipping dir before extract
        if (os.path.exists(cargo_shipping_dir)):
            shutil.rmtree(cargo_shipping_dir)

        zip.extractall(cargo_shipping_dir)


@click.group('add', help="Add stuffs to OmooSpace")
def add():
    pass


@click.command('folder')
def add_folder(root):
    pass


@click.command('work')
def add_work():
    pass


@click.command('member')
def add_member():
    pass


@click.command('software')
def add_software():
    pass


# cli.add_command(test)
cli.add_command(create_omoospace)
cli.add_command(print_omoospace_info)
cli.add_command(export_omoocargo)
cli.add_command(import_omoocargo)
cli.add_command(add)
add.add_command(add_folder)
add.add_command(add_work)
add.add_command(add_member)
add.add_command(add_software)

if __name__ == "__main__":
    cli()
