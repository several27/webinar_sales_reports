from setuptools import setup, find_packages
setup(
    name = 'orders_cleanup',
    version = '1.0',
    packages = find_packages(include = ('orders_cleanup*', )) + ["prophecy_config_instances"],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.3.8'],
    entry_points = {
'console_scripts' : [
'main = orders_cleanup.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
