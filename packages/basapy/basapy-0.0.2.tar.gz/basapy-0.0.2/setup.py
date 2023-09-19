from setuptools import setup, find_packages

setup(
    name='basapy',  # Nome único da sua biblioteca no PyPI
    version='0.0.2',  # Versão atual do seu pacote
    author='Abraão Pinto',  # Seu nome
    author_email='abraao.pinto@basa.com.br',  # Seu e-mail
    description='Uma biblioteca para formatar DataFrames Spark',  # Descrição curta
    long_description=open('README.md').read(),  # Descrição longa, geralmente um README
    long_description_content_type='text/markdown',  # Tipo de conteúdo da descrição longa
    url='https://github.com/abraaopinto/basapy',  # URL do repositório do GitHub ou outro
    packages=find_packages(),  # Pacotes a incluir no bundle de distribuição
    install_requires=[
        'pyspark',  # Dependências
    ],
    classifiers=[  # Classificadores para descrever a sua biblioteca
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # Escolha a licença apropriada
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
