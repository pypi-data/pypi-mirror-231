import logging
import os
from pprint import pformat
import sys
import tomllib
import click
from resumer.engines import get_engine
from resumer.gen.data import ResumerData
from resumer.gen.filter import ResumerFilter

def parse_tags(tags : tuple):
    includes = []
    excludes = []

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
def viaConfig(path : str, tags, openfile):
    with open(path, "rb") as f:
        configData = tomllib.load(f)
        if "data" not in configData:
            raise ValueError(f"no data section in {path}")
        
        if "engine" not in configData:
            raise ValueError(f"no engine section in {path}")
        
    rfilter = parse_tags(tags)
    if "output" not in configData["engine"]:
        raise ValueError("no output in config[engine]")
    
    output = configData["engine"]["output"]

    engineType = get_engine(output)

    rd = ResumerData.fromDict(configData, useKey="data")

    result = rd.format(rfilter)
    logging.debug(f"result: {pformat(result)}")

    engine = engineType.fromDict(configData, useKey="engine")
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


