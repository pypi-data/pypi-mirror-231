import shutil
import os
from pathlib import Path


from . import docker_compose
from . import docker_file
from . import proxy_cfg
from . import config


def _prepareArchive(target):
    if Path(target).is_dir():
        shutil.make_archive(target, 'gztar', base_dir=target)
        return target, f'{target}.tar.gz'
    else:
        return Path(target).name.split('.')[0], target


def down():
    docker_compose.run(['down'])


def up():
    docker_compose.buildFile()
    docker_compose.run(['build'])
    docker_compose.run(['up', '-d', '--remove-orphans'])


def add(target):
    target, filePath = _prepareArchive(target)
    if os.path.isfile(filePath):
        dstPath = config.APP_PATH.joinpath(target)
        shutil.rmtree(dstPath, ignore_errors=True)
        shutil.unpack_archive(filePath, config.APP_PATH)
        docker_file.makeDockerFile(target)
        proxy_cfg.makeConfig(target)


def install(target):
    down()
    add(target)
    up()


def install_proxy(target):
    down()
    target, filePath = _prepareArchive(target)
    if os.path.isfile(filePath):
        tmpPath = config.APP_PATH.joinpath(target)
        dstPath = config.APP_PATH.joinpath('reverse_proxy')
        shutil.rmtree(dstPath, ignore_errors=True)
        shutil.rmtree(tmpPath, ignore_errors=True)
        shutil.unpack_archive(filePath, config.APP_PATH)
        shutil.move(tmpPath, dstPath)
    up()


def uninstall(target):
    down()
    targetPath = config.APP_PATH.joinpath(target)
    shutil.rmtree(targetPath)
    up()
