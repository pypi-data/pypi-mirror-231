import logging
import os
from pprint import pformat
import sys
import tomllib
import click
from resumer.engines import get_engine
from resumer.engines.base import ResumerEngine
from resumer.gen.data import ResumerData
from resumer.gen.filter import ResumerFilter
from importlib.util import module_from_spec, spec_from_file_location
import inspect

def parse_tags(tags : tuple, configData : dict):
    includes = []
    excludes = []

    if "tags" in configData:
        tags = set(configData["tags"]) + set(tags)
        tags = tuple(tags)

    for tag in tags:
        tag : str
        if tag.startswith("/"):
            excludes.append(tag[1:])
        else:
            includes.append(tag)

    rfilter = ResumerFilter(includes=includes, excludes=excludes)
    logging.debug(f"rfilter includes: {rfilter.includes}")
    logging.debug(f"rfilter excludes: {rfilter.excludes}")
    logging.debug(f"rfilter drillExIncludes: {rfilter.drillExIncludes}")
    logging.debug(f"rfilter drillExExcludes: {rfilter.drillExExcludes}")
    logging.debug(f"rfilter directIncludes: {rfilter.direct_includes}")
    logging.debug(f"rfilter directExcludes: {rfilter.direct_excludes}")
    logging.debug(f"rfilter structuredIncludes: {rfilter.structured_includes}")
    logging.debug(f"rfilter structuredExcludes: {rfilter.structured_excludes}")

    return rfilter

def _engine(engine, output):
    if engine is not None:
        # import
        spec = spec_from_file_location("engine", engine)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        # get engine type from module
        for name, member in inspect.getmembers(module):
            if not inspect.isclass(member):
                continue
            if member == ResumerEngine:
                continue
            if issubclass(member, ResumerEngine):
                return member
    else:
        return get_engine(output)


@click.group(invoke_without_command=True)
@click.option("--debug", "-d", is_flag=True)
def resumer(debug : bool):
    if debug:
        logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

@resumer.group()
def gen():
    pass

@gen.command()
@click.argument("path", type=str)
@click.argument("tags", type=str, nargs=-1, required=False)
@click.option("--openfile", "-of", is_flag=True)
@click.option("--engine","-e", type=str, help="custom engine type")
@click.option("--relative", "-r", is_flag=True, help="use relative path")
def viaConfig(path : str, tags, openfile, engine, relative):
    with open(path, "rb") as f:
        configData = tomllib.load(f)
        if "data" not in configData:
            raise ValueError(f"no data section in {path}")
        
        if "engine" not in configData:
            raise ValueError(f"no engine section in {path}")
        
    if relative:
        os.chdir(os.path.dirname(path))

    rfilter = parse_tags(tags, configData)
    if "output" not in configData["engine"]:
        raise ValueError("no output in config[engine]")
    
    output = configData["engine"]["output"]

    engineType = _engine(engine, output)

    rd = ResumerData.fromConfigDict(configData, useKey="data")

    result = rd.format(rfilter)
    logging.debug(f"result: {pformat(result)}")

    engine = engineType.fromConfigDict(configData, useKey="engine")
    engine.generate(output, result)

    if openfile:
        engine.openLastGenerated()
        input("Press Enter to exit...")

def main():
    try:
        resumer()
    except Exception as e:
        click.echo(f"Error: {e}")
        os._exit(1)


